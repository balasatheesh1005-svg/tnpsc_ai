import logging
from typing import Dict, List, Any, Optional
import streamlit as st

from core.coach_maturity_ai import get_coach_maturity
from core.learning_intelligence_ai import (
    get_learning_intelligence,
    format_subject_name,
    format_topic_name,
)
from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
)
from core.daily_mission_ai import get_today_mission
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness, get_most_weak_topic
from core.streak_ai import get_streak
from core.xp_ai import get_user_xp
from core.mentor_memory import get_memory

logger = logging.getLogger(__name__)


def _determine_priority_label(priority: int) -> str:
    """Map numeric priority (1-6) to human readable priority label."""
    if priority == 1:
        return "Critical"
    elif priority == 2:
        return "High"
    elif priority == 3:
        return "Medium-High"
    elif priority == 4:
        return "Medium"
    elif priority == 5:
        return "Standard"
    else:
        return "Optional"


from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Study Planner Engine")
def get_personal_study_plan(
    user: Optional[str] = None,
    available_time: int = 45,
    context: Optional[Any] = None,
    force_refresh: bool = False,
) -> Dict[str, Any]:
    """
    Personal Study Planner Engine V2 - Central Planning Engine.
    Converts Learning Intelligence, Revision Engine, Mission Engine, Progress Engine,
    and available study time into a personalized, deterministic daily study plan.
    
    Dashboard displays output ONLY. Zero calculations performed in UI.
    Truth & Safety Contract:
    - Truthfully distinguishes observed learner performance from future projections.
    - Never fabricates arbitrary percentage gains or guaranteed mastery targets.
    - Low-evidence/zero-data learners receive structured foundational plans without fake metrics.
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Study Planner Engine_{user_str}_{available_time}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Study Planner Engine")
        return st.session_state[cache_key]
    record_cache_miss("Study Planner Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    # Sanitize available_time
    try:
        available_time = int(available_time)
        if available_time <= 0:
            available_time = 45
    except (TypeError, ValueError):
        available_time = 45

    # 1. Fetch Engine Outputs (Zero duplicate logic with resilient exception handling)
    try:
        maturity = get_coach_maturity(user, context=ctx)
    except Exception as e:
        logger.warning(f"Error retrieving coach maturity for {user}: {e}")
        maturity = {
            "attempt_count": 0,
            "tier": "TIER_0_NO_DATA",
            "tier_label": "No Data",
        }
    try:
        intelligence = get_learning_intelligence(user, context=ctx)
    except Exception as e:
        logger.warning(f"Error retrieving learning intelligence for {user}: {e}")
        intelligence = {}
    try:
        revision_plan = get_intelligent_revision_plan(user, context=ctx)
    except Exception as e:
        logger.warning(f"Error retrieving revision plan for {user}: {e}")
        revision_plan = {}
    try:
        revision_analytics = get_revision_analytics_v2(user, context=ctx)
    except Exception as e:
        logger.warning(f"Error retrieving revision analytics for {user}: {e}")
        revision_analytics = {}
    try:
        mission = get_today_mission(user, context=ctx)
    except Exception as e:
        logger.warning(f"Error retrieving mission for {user}: {e}")
        mission = {}
    progress_rows = get_progress(user, context=ctx) or []
    weakness_data = get_weakness(user, context=ctx) or {}
    streak = get_streak(user, context=ctx) or 0
    xp_data = get_user_xp(user, context=ctx) or {}
    memory = get_memory(user, context=ctx)

    attempt_count = maturity.get("attempt_count", 0)
    tier = maturity.get("tier", "TIER_0_NO_DATA")
    tier_label = maturity.get("tier_label", "No Data")
    has_history = attempt_count > 0 or len(progress_rows) > 0

    # Extract Key Parameters from Engines with Truthful Fallbacks
    if not has_history:
        subj = "Indian Polity"
        topic = "Fundamental Rights"
        repo = "Foundation Repository"
        qtype = "Concept Questions"
        observed_acc = None
    else:
        raw_subj = intelligence.get("subject")
        subj = raw_subj if raw_subj and raw_subj != "Not enough data yet" else "History"
        raw_topic = intelligence.get("topic")
        topic = raw_topic if raw_topic and raw_topic != "Not enough data yet" else "Indus Valley"
        raw_repo = intelligence.get("repository")
        repo = raw_repo if raw_repo and raw_repo != "N/A" else "Foundation Repository"
        raw_qtype = intelligence.get("question_type")
        qtype = raw_qtype if raw_qtype and raw_qtype != "N/A" else "Concept Questions"

        # Calculate genuine observed accuracy from progress rows
        all_accuracies = [float(r.get("accuracy", 0)) for r in progress_rows if r.get("accuracy") is not None]
        if all_accuracies:
            observed_acc = round(sum(all_accuracies) / len(all_accuracies), 1)
        else:
            raw_m = intelligence.get("current_mastery")
            try:
                observed_acc = round(float(raw_m), 1) if raw_m is not None else None
            except (ValueError, TypeError):
                observed_acc = None

    # Check Revision Status
    overdue_items = revision_analytics.get("overdue", [])
    due_today_items = revision_analytics.get("due_today", [])
    has_overdue = len(overdue_items) > 0 or revision_plan.get("status") == "Overdue"

    # 2. Build Candidate Task Queue strictly by Priority Rules
    candidate_tasks = []

    # Priority 1: Overdue Revision
    if has_overdue or due_today_items:
        rev_item = overdue_items[0] if overdue_items else (due_today_items[0] if due_today_items else {})
        rev_subj = rev_item.get("subject", subj)
        rev_top = rev_item.get("topic", topic)
        candidate_tasks.append({
            "priority": 1,
            "priority_label": _determine_priority_label(1),
            "task": "Revision",
            "subject": format_subject_name(rev_subj),
            "topic": format_topic_name(rev_top),
            "repository": "Revision Queue",
            "question_type": revision_plan.get("level4_question_type", "Spaced Recall"),
            "duration": 12,
            "reason": "Overdue Revision",
            "expected_benefit": "Prevent Memory Decay & Solidify Recall",
            "reward": "+25 XP",
            "xp_num": 25,
        })

    # Priority 2: Learning Focus / Bottleneck
    if has_history:
        root_cause_label = intelligence.get("root_cause", "Concept Application")
        candidate_tasks.append({
            "priority": 2,
            "priority_label": _determine_priority_label(2),
            "task": "Weakness Practice",
            "subject": format_subject_name(subj),
            "topic": format_topic_name(topic),
            "repository": repo,
            "question_type": qtype,
            "duration": 18,
            "reason": f"Current Focus ({root_cause_label})",
            "expected_benefit": f"Target high-yield concepts & strengthen consistency in {format_topic_name(topic)}",
            "reward": "+35 XP",
            "xp_num": 35,
        })
    else:
        candidate_tasks.append({
            "priority": 2,
            "priority_label": _determine_priority_label(2),
            "task": "Foundational Practice",
            "subject": format_subject_name(subj),
            "topic": format_topic_name(topic),
            "repository": repo,
            "question_type": qtype,
            "duration": 18,
            "reason": "Initial Baseline Assessment",
            "expected_benefit": "Establish initial diagnostic baseline with foundational concepts",
            "reward": "+35 XP",
            "xp_num": 35,
        })

    # Priority 3: Recovery / Concept Notes Review
    if has_history:
        rec_plan_steps = intelligence.get("recovery_plan", [])
        rec_step_text = rec_plan_steps[0] if rec_plan_steps else f"Revise {qtype} notes & key concepts"
        candidate_tasks.append({
            "priority": 3,
            "priority_label": _determine_priority_label(3),
            "task": "Recovery Notes & Set",
            "subject": format_subject_name(subj),
            "topic": format_topic_name(topic),
            "repository": "Concept Notes",
            "question_type": "Guided Practice",
            "duration": 15,
            "reason": "Recovery Plan",
            "expected_benefit": rec_step_text,
            "reward": "+20 XP",
            "xp_num": 20,
        })
    else:
        candidate_tasks.append({
            "priority": 3,
            "priority_label": _determine_priority_label(3),
            "task": "Concept Notes Review",
            "subject": format_subject_name(subj),
            "topic": format_topic_name(topic),
            "repository": "Concept Notes",
            "question_type": "Guided Practice",
            "duration": 15,
            "reason": "Syllabus Orientation",
            "expected_benefit": "Review core definitions and high-weightage TNPSC concepts",
            "reward": "+20 XP",
            "xp_num": 20,
        })

    # Priority 4: Mission Task
    is_mission_complete = mission.get("daily_test_completed", False)
    if not is_mission_complete:
        candidate_tasks.append({
            "priority": 4,
            "priority_label": _determine_priority_label(4),
            "task": "Daily Mission Test",
            "subject": format_subject_name(subj),
            "topic": format_topic_name(topic),
            "repository": "Daily Mission Repo",
            "question_type": "Mixed Standard Set",
            "duration": 20,
            "reason": "Daily Mission",
            "expected_benefit": "Maintain Daily Streak & Earn Mission Bonus",
            "reward": "+50 XP",
            "xp_num": 50,
        })

    # Priority 5: Topic Progress (PYQ / Next Topic)
    candidate_tasks.append({
        "priority": 5,
        "priority_label": _determine_priority_label(5),
        "task": "PYQ Practice Set",
        "subject": format_subject_name(subj),
        "topic": format_topic_name(topic),
        "repository": "PYQ Repository",
        "question_type": "Previous Year Questions",
        "duration": 25,
        "reason": "Topic Progress",
        "expected_benefit": "Test Exam Readiness against Official TNPSC PYQs",
        "reward": "+40 XP",
        "xp_num": 40,
    })

    # Priority 6: Optional Practice (Grand Test)
    candidate_tasks.append({
        "priority": 6,
        "priority_label": _determine_priority_label(6),
        "task": "Grand Mock Test",
        "subject": format_subject_name(subj),
        "topic": format_topic_name(topic),
        "repository": "Grand Test",
        "question_type": "Full Syllabus Simulation",
        "duration": 30,
        "reason": "Optional Practice",
        "expected_benefit": "Simulate Exam Speed & Full Length Accuracy",
        "reward": "+60 XP",
        "xp_num": 60,
    })

    # 3. Deterministic Available Time Adaptation
    selected_tasks = []
    accumulated_time = 0

    for candidate in candidate_tasks:
        candidate_dur = candidate["duration"]
        if accumulated_time + candidate_dur <= available_time or not selected_tasks:
            selected_tasks.append(candidate)
            accumulated_time += candidate_dur
        elif available_time <= 20 and len(selected_tasks) >= 1:
            break
        elif available_time <= 45 and accumulated_time >= 35:
            break
        elif available_time <= 90 and accumulated_time >= 80:
            break

    today_plan = []
    total_xp = 0
    total_duration = 0

    for idx, t in enumerate(selected_tasks, 1):
        item = dict(t)
        item["priority"] = idx
        item["priority_label"] = _determine_priority_label(idx)
        today_plan.append(item)
        total_xp += t["xp_num"]
        total_duration += t["duration"]

    # 4. Truthful Outcome & Mastery Semantics (Zero Arbitrary Predictions)
    if not has_history or observed_acc is None:
        curr_m_display = "No Data"
        exp_m_display = "Diagnostic Baseline"
        curr_conf = "No Data"
        exp_conf = "Initial Baseline"
        mastery_gain_display = "Baseline Setup"
        goal_text = "Establish Diagnostic Baseline"
        focus_text = "Foundational Concepts + Practice"
        learning_focus_msg = "Begin with foundational syllabus review and initial practice questions to establish your baseline."
    else:
        curr_m_display = f"{observed_acc}%"
        exp_m_display = "Strengthen Retention"
        curr_conf = tier_label
        exp_conf = "Structured Practice"
        mastery_gain_display = "Retention Boost"
        goal_text = f"Strengthen {format_topic_name(topic)}"
        focus_text = f"Revision + Targeted Practice in {format_subject_name(subj)}"
        learning_focus_msg = f"Completing today's plan focuses on active recall and deliberate practice in {format_topic_name(topic)} to reinforce concept retention and exam consistency."

    expected_outcome = {
        "current_mastery": curr_m_display,
        "observed_accuracy": observed_acc,
        "observed_accuracy_str": curr_m_display,
        "expected_mastery": exp_m_display,
        "expected_mastery_gain": mastery_gain_display,
        "current_confidence": curr_conf,
        "expected_confidence": exp_conf,
        "goal": goal_text,
        "focus": focus_text,
        "learning_focus_msg": learning_focus_msg,
        "evidence_tier": tier,
        "evidence_tier_label": tier_label,
        "projection_available": False,
        "projection_note": "Projection unavailable — more practice data needed to model predictive trajectories.",
    }

    # 5. Study Sequence Timeline
    study_sequence = []
    for step_num, task_item in enumerate(today_plan, 1):
        study_sequence.append({
            "step": step_num,
            "action": task_item["task"],
            "subject": task_item["subject"],
            "topic": task_item["topic"],
            "repository": task_item["repository"],
            "question_type": task_item["question_type"],
            "duration": task_item["duration"],
            "duration_str": f"{task_item['duration']} Mins",
            "reward": task_item["reward"],
        })

    # 6. Next Recommended Action
    if not has_history:
        next_action = "Complete initial practice questions to unlock diagnostic baseline"
    elif has_overdue and len(today_plan) <= 2:
        next_action = "Continue Recovery Session for Weakest Topics"
    elif any(t["task"] in ["Weakness Practice", "Foundational Practice"] for t in today_plan):
        next_action = f"Attempt {format_subject_name(subj)} PYQ Repository to verify mastery"
    elif any(t["task"] == "PYQ Practice Set" for t in today_plan):
        next_action = "Take full Grand Test session"
    else:
        next_action = f"Move to next topic in {format_subject_name(subj)}"

    # 7. Mentor Message
    if not has_history:
        mentor_message = f"Welcome! Today's plan is tailored for {available_time} minutes of foundational preparation in {format_subject_name(subj)}."
    else:
        mentor_message = intelligence.get(
            "mentor_insight",
            f"Today's plan is tailored for {available_time} minutes of focused preparation on {format_topic_name(topic)}."
        )

    # 8. Master JSON Output
    result = {
        "subject": format_subject_name(subj),
        "topic": format_topic_name(topic),
        "today_plan": today_plan,
        "estimated_time": total_duration,
        "available_time": available_time,
        "expected_mastery_gain": mastery_gain_display,
        "expected_xp": total_xp,
        "expected_outcome": expected_outcome,
        "study_sequence": study_sequence,
        "next_action": next_action,
        "mentor_message": mentor_message,
        "daily_summary": {
            "today_goal": f"Complete {len(today_plan)} Tasks",
            "total_tasks": len(today_plan),
            "estimated_time": total_duration,
            "potential_xp": total_xp,
            "expected_mastery_gain": mastery_gain_display,
        },
    }

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result

