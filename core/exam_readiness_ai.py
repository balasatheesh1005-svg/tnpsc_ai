import logging
from typing import Dict, List, Any, Optional
import streamlit as st

from core.learning_intelligence_ai import (
    get_learning_intelligence,
    format_subject_name,
    format_topic_name,
)
from core.study_planner_ai import get_personal_study_plan
from core.recommendation_ai import get_ai_recommendation
from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
)
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.streak_ai import get_streak
from core.xp_ai import get_user_xp
from core.daily_mission_ai import get_today_mission
from core.mentor_memory import get_memory

logger = logging.getLogger(__name__)


def _classify_readiness_level(score: int) -> str:
    """Classify 0-100 readiness score into standard preparation levels."""
    if score <= 25:
        return "Beginning"
    elif score <= 50:
        return "Developing"
    elif score <= 75:
        return "Exam Ready"
    elif score <= 90:
        return "Highly Ready"
    else:
        return "Excellent Readiness"

def _determine_readiness_level(score: int) -> str:
    return _classify_readiness_level(score)


from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Exam Readiness Engine")
def get_exam_readiness(
    user: Optional[str] = None,
    context: Optional[Any] = None,
    force_refresh: bool = False,
) -> Dict[str, Any]:
    """
    Exam Readiness Engine V2 - Central Readiness Evaluation Engine.
    Synthesizes outputs from Learning Intelligence V2, Study Planner V2,
    Recommendation Engine V2, Revision V2, Progress, Weakness, Streak, and XP Engines.
    
    Evaluates student's CURRENT preparation level across 5 deterministic dimensions.
    Dashboard displays output ONLY. Zero evaluation calculations performed in UI.
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Exam Readiness Engine_{user_str}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Exam Readiness Engine")
        return st.session_state[cache_key]
    record_cache_miss("Exam Readiness Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    # 1. Fetch Master Engine Outputs (Zero duplicate logic)
    intelligence = get_learning_intelligence(user, context=ctx)
    intel_subject = intelligence.get("subject", "History")
    intel_mastery = float(intelligence.get("current_mastery", 50.0))
    study_plan = get_personal_study_plan(user, available_time=45, context=ctx)
    recommendation = get_ai_recommendation(user, context=ctx)
    revision_plan = get_intelligent_revision_plan(user, context=ctx)
    revision_analytics = get_revision_analytics_v2(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)
    streak = get_streak(user, context=ctx)
    xp_data = get_user_xp(user, context=ctx)

    # 2. Evaluate 5 Core Dimensions (0-100 each)
    # Dimension 1: Topic Mastery Dimension (30%)
    all_accuracies = [float(r.get("accuracy", 0)) for r in progress_rows if r.get("accuracy") is not None]
    avg_topic_mastery = round(sum(all_accuracies) / len(all_accuracies), 1) if all_accuracies else intel_mastery
    d1_mastery = max(10.0, min(100.0, avg_topic_mastery))

    # Dimension 2: Repository Completion Dimension (20%)
    hard_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "hard" in str(r.get("topic", "")).lower()]
    stmt_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "statement" in str(r.get("topic", "")).lower()]
    assert_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "assertion" in str(r.get("topic", "")).lower()]

    avg_hard = sum(hard_accs) / len(hard_accs) if hard_accs else (d1_mastery * 0.85)
    avg_stmt = sum(stmt_accs) / len(stmt_accs) if stmt_accs else (d1_mastery * 0.9)
    avg_assert = sum(assert_accs) / len(assert_accs) if assert_accs else (d1_mastery * 0.8)

    d2_repo_completion = max(10.0, min(100.0, (avg_hard + avg_stmt + avg_assert) / 3.0))

    # Dimension 3: Revision Health Dimension (20%)
    rev_prog = revision_analytics.get("progress", {})
    rev_pct = float(rev_prog.get("percentage", 75.0))
    d3_revision_health = max(10.0, min(100.0, rev_pct))

    # Dimension 4: Learning Consistency Dimension (15%)
    d4_consistency = max(10.0, min(100.0, (streak * 12.0) + 40.0))

    # Dimension 5: PYQ & Exam Readiness Dimension (15%)
    pyq_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "pyq" in str(r.get("topic", "")).lower()]
    avg_pyq = sum(pyq_accs) / len(pyq_accs) if pyq_accs else (d1_mastery * 0.9)
    d5_pyq = max(10.0, min(100.0, avg_pyq))

    # 3. Overall Readiness Score (0-100)
    weighted_score = (
        (0.30 * d1_mastery) +
        (0.20 * d2_repo_completion) +
        (0.20 * d3_revision_health) +
        (0.15 * d4_consistency) +
        (0.15 * d5_pyq)
    )
    overall_readiness = max(10, min(100, int(round(weighted_score))))
    readiness_level = _classify_readiness_level(overall_readiness)

    readiness_dimensions = {
        "topic_mastery": int(round(d1_mastery)),
        "repository_completion": int(round(d2_repo_completion)),
        "revision_health": int(round(d3_revision_health)),
        "consistency": int(round(d4_consistency)),
        "pyq_readiness": int(round(d5_pyq)),
    }

    # 4. Subject-wise Readiness Analysis
    standard_subjects = ["History", "Polity", "Geography", "Economy", "Science", "Current Affairs"]
    subject_scores = []

    # Map accuracies by subject from progress rows
    subj_acc_map = {}
    for r in progress_rows:
        s_name = format_subject_name(r.get("subject", "")).strip()
        acc = float(r.get("accuracy", 0))
        if s_name:
            if s_name not in subj_acc_map:
                subj_acc_map[s_name] = []
            subj_acc_map[s_name].append(acc)

    for subj_item in standard_subjects:
        if subj_item in subj_acc_map and subj_acc_map[subj_item]:
            s_score = int(round(sum(subj_acc_map[subj_item]) / len(subj_acc_map[subj_item])))
        elif subj_item == format_subject_name(intel_subject):
            s_score = int(round(intel_mastery))
        else:
            # Derived baseline for subjects with sparse data
            mod_offset = (len(subj_item) * 3) % 15 - 7
            s_score = max(35, min(95, overall_readiness + mod_offset))

        subject_scores.append({
            "subject": subj_item,
            "score": s_score,
        })

    # Sort subject scores to identify strongest and weakest
    sorted_subjects = sorted(subject_scores, key=lambda x: x["score"], reverse=True)
    strongest_subj = sorted_subjects[0]["subject"]
    strongest_score = sorted_subjects[0]["score"]
    weakest_subj = sorted_subjects[-1]["subject"]
    weakest_score = sorted_subjects[-1]["score"]

    # 5. Strength Analysis Logic (Identify Top Strengths)
    strengths = []
    if d4_consistency >= 70 or streak >= 3:
        strengths.append("Consistent Daily Study Habit")
    if d3_revision_health >= 70:
        strengths.append("Excellent Spaced Revision Discipline")
    if strongest_score >= 70:
        strengths.append(f"Strong {strongest_subj} Topic Mastery ({strongest_score}%)")
    if d1_mastery >= 70:
        strengths.append("Solid Foundational Accuracy")
    if d5_pyq >= 65:
        strengths.append("High Official PYQ Accuracy")

    if not strengths:
        strengths.append("Active Daily Platform Engagement")

    # 6. Improvement Analysis Logic (Identify Top Priority Improvements)
    improvements = []
    if d3_revision_health < 75 or len(revision_analytics.get("overdue", [])) > 0:
        improvements.append("Clear Overdue Spaced Revisions")
    if d2_repo_completion < 70 or avg_hard < 60:
        improvements.append("Complete Hard Repository Questions")
    if weakest_score < 70:
        improvements.append(f"Increase {weakest_subj} Revision Coverage ({weakest_score}%)")
    if d5_pyq < 70:
        improvements.append("Attempt More Official PYQ Practice Sets")
    if streak < 3:
        improvements.append("Maintain 5-Day Study Streak")

    if not improvements:
        improvements.append("Take Full Length Grand Test")

    # 7. Readiness Explanation Rationale
    readiness_reason = (
        f"Overall preparation level is currently {overall_readiness}% ({readiness_level}). "
        f"Strong performance in {strongest_subj} ({strongest_score}%) and daily consistency drive your readiness. "
        f"Increasing revision coverage in {weakest_subj} ({weakest_score}%) and hard repository completion "
        f"remains the primary path to elevating readiness."
    )

    # 8. AI Mentor Insight
    mentor_insight = (
        f"Your preparation in {strongest_subj} is driving your readiness score. "
        f"Focusing on {weakest_subj} will balance your portfolio and push your score higher."
    )

    # 9. Return Master Output Schema
    return {
        "overall_readiness": overall_readiness,
        "overall_readiness_score": overall_readiness,
        "overall_score": overall_readiness,
        "level": readiness_level,
        "readiness_dimensions": readiness_dimensions,
        "subjects": subject_scores,
        "strengths": strengths[:4],
        "improvements": improvements[:4],
        "readiness_reason": readiness_reason,
        "mentor_insight": mentor_insight,
        "strongest_subject": strongest_subj,
        "weakest_subject": weakest_subj,
    }

    return get_cached_engine_result(
        "Exam Readiness Engine", user, _compute, force_refresh=force_refresh
    )

