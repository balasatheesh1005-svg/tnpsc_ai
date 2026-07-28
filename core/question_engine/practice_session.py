import logging
import time
from typing import Dict, List, Any, Optional
import streamlit as st

logger = logging.getLogger(__name__)

from core.question_loader import load_questions
from core.progress_ai import get_progress, save_progress
from core.xp_ai import add_xp, is_achievement_unlocked, get_user_xp
from core.navigation_v2.navigation_state import check_repository_availability
from core.weakness_ai import add_weakness, get_weakness
from core.revision_ai import add_revision_topic
from core.daily_mission_ai import update_question_count
from core.streak_ai import update_streak
from core.mentor_memory import update_memory

PRACTICE_REPO_ORDER = [
    "easy",
    "medium",
    "hard",
    "statement_based",
    "assertion_reason",
    "match_the_following",
    "chronology",
    "pyq",
]


def start_practice_session(
    subject: str,
    topic_id: str,
    repository_id: str,
    display_title: str,
    repository_type: str = "easy",
) -> bool:
    """
    Initializes an isolated Practice session.
    Loads the COMPLETE question repository without capping at 10.
    Does NOT touch or pollute Daily Test session variables.
    """
    subj = subject.lower().strip()
    repo_type = repository_type.lower().strip()
    questions = load_questions(repository_id, repo_type)

    if not questions:
        print(f"⚠️ Practice Session: No questions found for repo_id='{repository_id}', type='{repo_type}'")
        return False

    st.session_state["practice_active"] = True
    st.session_state["practice_subject"] = subj
    st.session_state["practice_topic_id"] = topic_id
    st.session_state["practice_repository_id"] = repository_id
    st.session_state["practice_repository_type"] = repo_type
    st.session_state["practice_display_title"] = display_title
    st.session_state["practice_questions"] = questions
    st.session_state["practice_current_index"] = 0
    st.session_state["practice_score"] = 0
    st.session_state["practice_answers"] = {}
    st.session_state["practice_start_time"] = time.time()
    st.session_state["practice_end_time"] = None
    st.session_state["practice_completed"] = False
    st.session_state["practice_results_processed"] = False
    st.session_state["practice_review_mode"] = False
    st.session_state["active_practice_setup"] = None

    # Universal Renderer session keys for practice prefix
    st.session_state["practice_index"] = 0
    st.session_state["practice_answered"] = False
    st.session_state["practice_selected_answer"] = None
    st.session_state["practice_attempts"] = []
    st.session_state["practice_score"] = 0
    st.session_state["practice_bookmarks"] = set()
    st.session_state["practice_started_at"] = time.time()

    return True


def get_practice_state() -> Dict[str, Any]:
    """Returns the current Practice session state dictionary."""
    return {
        "active": st.session_state.get("practice_active", False),
        "subject": st.session_state.get("practice_subject", "polity"),
        "topic_id": st.session_state.get("practice_topic_id", ""),
        "repository_id": st.session_state.get("practice_repository_id", ""),
        "repository_type": st.session_state.get("practice_repository_type", "easy"),
        "display_title": st.session_state.get("practice_display_title", ""),
        "questions": st.session_state.get("practice_questions", []),
        "current_index": st.session_state.get("practice_current_index", 0),
        "score": st.session_state.get("practice_score", 0),
        "answers": st.session_state.get("practice_answers", {}),
        "start_time": st.session_state.get("practice_start_time", 0),
        "end_time": st.session_state.get("practice_end_time"),
        "completed": st.session_state.get("practice_completed", False),
        "results_processed": st.session_state.get("practice_results_processed", False),
        "review_mode": st.session_state.get("practice_review_mode", False),
    }


def record_practice_answer(
    question_index: int,
    selected_option: str,
    is_correct: bool,
    question_id: str,
):
    """Records user answer selection for a specific question in practice session."""
    answers = dict(st.session_state.get("practice_answers", {}))
    answers[question_index] = {
        "selected_option": selected_option,
        "is_correct": is_correct,
        "question_id": question_id,
        "timestamp": time.time(),
    }
    st.session_state["practice_answers"] = answers

    # Recalculate total score
    score = sum(1 for a in answers.values() if a.get("is_correct"))
    st.session_state["practice_score"] = score


def next_practice_question() -> bool:
    """
    Advances to the next question in practice session.
    If all questions completed, sets practice_completed = True.
    """
    questions = st.session_state.get("practice_questions", [])
    total_q = len(questions)
    curr_i = st.session_state.get("practice_current_index", 0)

    if curr_i + 1 < total_q:
        st.session_state["practice_current_index"] = curr_i + 1
        st.session_state["practice_index"] = curr_i + 1
        st.session_state["practice_answered"] = False
        st.session_state["practice_selected_answer"] = None
        return True
    else:
        st.session_state["practice_completed"] = True
        st.session_state["practice_end_time"] = time.time()
        return False


def set_practice_question_index(index: int):
    """Sets the current practice question index (for palette jump navigation)."""
    questions = st.session_state.get("practice_questions", [])
    if 0 <= index < len(questions):
        st.session_state["practice_current_index"] = index
        st.session_state["practice_index"] = index
        
        # Restore answered state for this index if recorded
        answers = st.session_state.get("practice_answers", {})
        if index in answers:
            st.session_state["practice_answered"] = True
            st.session_state["practice_selected_answer"] = answers[index]["selected_option"]
        else:
            st.session_state["practice_answered"] = False
            st.session_state["practice_selected_answer"] = None


def complete_practice_session(user: str) -> Dict[str, Any]:
    """
    Processes final practice statistics, saves progress to DB, awards practice XP,
    triggers Weakness, Revision, Daily Mission, Streak, and Mentor Memory engines,
    and returns session performance summary.
    """
    if st.session_state.get("practice_results_processed"):
        return get_practice_summary()

    questions = st.session_state.get("practice_questions", [])
    total_questions = len(questions)
    score = st.session_state.get("practice_score", 0)
    accuracy = int((score / max(1, total_questions)) * 100)

    subject = st.session_state.get("practice_subject", "polity")
    topic_id = st.session_state.get("practice_topic_id", "")
    repository_id = st.session_state.get("practice_repository_id", "")
    display_title = st.session_state.get("practice_display_title", "")
    answers = st.session_state.get("practice_answers", {})
    topic_ref = (topic_id or repository_id or "").lower().strip().replace(" ", "_")

    # 0. Check if repository was already completed in a prior session
    already_completed = False
    try:
        progress_records = get_progress(user)
        r_id = repository_id.lower().strip()
        s_id = subject.lower().strip()
        for rec in progress_records:
            if rec.get("subject", "").lower().strip() == s_id and rec.get("topic", "").lower().strip() == r_id:
                already_completed = True
                break
    except Exception as e:
        logger.error(f"Practice Session: Failed to check repository completion history: {e}", exc_info=True)

    # 1. Save Practice progress to DB
    try:
        save_progress(
            user=user,
            subject=subject,
            topic=display_title,
            accuracy=accuracy,
            topic_id=topic_id,
            repository_id=repository_id,
        )
    except Exception as e:
        logger.error(f"Practice Session: Failed to save progress to DB: {e}", exc_info=True)

    # 2. Award Practice XP (+10 XP per correct answer if first completion)
    if already_completed:
        xp_earned = 0
        xp_already_awarded = True
    else:
        xp_earned = score * 10
        if accuracy == 100:
            xp_earned += 25  # Perfect practice bonus
        xp_already_awarded = False

        try:
            add_xp(user, xp_earned, reward_type="practice_completion")
        except Exception as e:
            logger.error(f"Practice Session: Failed to add XP: {e}", exc_info=True)

    # 3. Trigger Weakness Engine for wrong answers
    wrong_count = 0
    try:
        for ans in answers.values():
            if isinstance(ans, dict) and not ans.get("is_correct", False):
                wrong_count += 1
                add_weakness(user, subject, topic_ref)
    except Exception as e:
        logger.error(f"Practice Session: Failed to update Weakness Engine: {e}", exc_info=True)

    # 4. Trigger Revision Engine if incorrect answers exist or accuracy < 100%
    try:
        if wrong_count > 0 or accuracy < 100:
            add_revision_topic(user, subject, topic_ref)
    except Exception as e:
        logger.error(f"Practice Session: Failed to update Revision Engine: {e}", exc_info=True)

    # 5. Trigger Daily Mission Engine (increment question count for answered practice questions)
    try:
        answered_q_count = len(answers) if answers else total_questions
        for _ in range(answered_q_count):
            update_question_count(user)
    except Exception as e:
        logger.error(f"Practice Session: Failed to update Daily Mission Engine: {e}", exc_info=True)

    # 6. Trigger Streak Engine
    streak_count = 0
    try:
        streak_count = update_streak(user)
    except Exception as e:
        logger.error(f"Practice Session: Failed to update Streak Engine: {e}", exc_info=True)

    # 7. Trigger Mentor Memory Engine
    try:
        weak_data = get_weakness(user)
        update_memory(user, score, max(1, total_questions), weak_data)
    except Exception as e:
        logger.error(f"Practice Session: Failed to update Mentor Memory: {e}", exc_info=True)

    # 8. Trigger Achievement System Evaluation
    unlocked_achievements = []
    try:
        repo_type = st.session_state.get("practice_repository_type", "easy")
        is_grand_test = (repo_type == "grand_test")

        # First Practice Completed
        if not already_completed:
            unlocked_achievements.append({
                "title": "First Practice Completed",
                "description": f"Completed {display_title} ({repo_type.replace('_', ' ').title()}) practice session!",
                "unlocked": True,
                "level": "bronze",
            })

        # First Perfect Score
        if accuracy == 100:
            unlocked_achievements.append({
                "title": "First Perfect Score",
                "description": f"Achieved 100% accuracy in {display_title}!",
                "unlocked": True,
                "level": "gold",
            })

        # 7-Day Streak
        if streak_count >= 7:
            unlocked_achievements.append({
                "title": "7-Day Streak",
                "description": "Maintained a 7 day continuous practice streak!",
                "unlocked": True,
                "level": "gold",
            })

        # Level achievements
        if is_achievement_unlocked(user, "level_2"):
            unlocked_achievements.append({
                "title": "🌟 Level 2 Mastery",
                "description": "Reached Level 2 proficiency in TNPSC preparation.",
                "unlocked": True,
                "level": "silver",
            })
        if is_achievement_unlocked(user, "level_5"):
            unlocked_achievements.append({
                "title": "⭐ Level 5 Mastery",
                "description": "Reached Level 5 proficiency in TNPSC preparation.",
                "unlocked": True,
                "level": "gold",
            })
        if is_achievement_unlocked(user, "level_10"):
            unlocked_achievements.append({
                "title": "🌠 Level 10 Mastery",
                "description": "Reached Level 10 master status!",
                "unlocked": True,
                "level": "gold",
            })

        # Topic Mastered (only after Grand Test completion)
        if is_grand_test:
            unlocked_achievements.append({
                "title": "🏆 Topic Mastered",
                "description": f"Successfully completed full learning roadmap for {display_title}!",
                "unlocked": True,
                "level": "gold",
            })

    except Exception as e:
        logger.error(f"Practice Session: Failed to evaluate Achievement System: {e}", exc_info=True)

    st.session_state["practice_results_processed"] = True
    st.session_state["practice_earned_xp"] = xp_earned
    st.session_state["practice_xp_already_awarded"] = xp_already_awarded
    st.session_state["practice_streak"] = streak_count
    st.session_state["practice_unlocked_achievements"] = unlocked_achievements

    return get_practice_summary()


def get_practice_summary() -> Dict[str, Any]:
    """Returns summary dictionary of completed practice session."""
    questions = st.session_state.get("practice_questions", [])
    total_questions = len(questions)
    score = st.session_state.get("practice_score", 0)
    correct = score
    wrong = max(0, total_questions - correct)
    accuracy = int((correct / max(1, total_questions)) * 100)

    start_t = st.session_state.get("practice_start_time", time.time())
    end_t = st.session_state.get("practice_end_time") or time.time()
    time_taken_sec = max(1, int(end_t - start_t))

    return {
        "subject": st.session_state.get("practice_subject", "polity"),
        "topic_id": st.session_state.get("practice_topic_id", ""),
        "repository_id": st.session_state.get("practice_repository_id", ""),
        "repository_type": st.session_state.get("practice_repository_type", "easy"),
        "display_title": st.session_state.get("practice_display_title", ""),
        "total_questions": total_questions,
        "correct": correct,
        "wrong": wrong,
        "accuracy": accuracy,
        "score": score,
        "time_taken": time_taken_sec,
        "xp_earned": st.session_state.get("practice_earned_xp", 0),
        "xp_already_awarded": st.session_state.get("practice_xp_already_awarded", False),
        "streak": st.session_state.get("practice_streak", 0),
        "unlocked_achievements": st.session_state.get("practice_unlocked_achievements", []),
    }


def get_next_repository_type(current_type: str, availability_dict: Dict[str, bool]) -> Optional[str]:
    """Finds the next available practice repository type in sequential difficulty order."""
    curr = current_type.lower().strip()
    if curr not in PRACTICE_REPO_ORDER:
        return None

    curr_idx = PRACTICE_REPO_ORDER.index(curr)
    for next_type in PRACTICE_REPO_ORDER[curr_idx + 1:]:
        if availability_dict.get(next_type, False):
            return next_type

    return None


def clear_practice_session():
    """Completely resets all practice session keys without touching Daily Test."""
    practice_keys = [
        "practice_active",
        "practice_subject",
        "practice_topic_id",
        "practice_repository_id",
        "practice_repository_type",
        "practice_display_title",
        "practice_questions",
        "practice_current_index",
        "practice_score",
        "practice_answers",
        "practice_start_time",
        "practice_end_time",
        "practice_completed",
        "practice_results_processed",
        "practice_review_mode",
        "practice_earned_xp",
        "practice_index",
        "practice_answered",
        "practice_selected_answer",
        "practice_attempts",
        "practice_bookmarks",
        "practice_started_at",
        "practice_unlocked_achievements",
    ]
    for key in practice_keys:
        st.session_state.pop(key, None)
