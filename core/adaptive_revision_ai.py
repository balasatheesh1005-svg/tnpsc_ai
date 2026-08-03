import logging
from typing import Dict, List, Any, Optional
import streamlit as st

from core.learning_intelligence_ai import (
    get_learning_intelligence,
    format_subject_name,
    format_topic_name,
)
from core.exam_readiness_ai import get_exam_readiness
from core.mock_intelligence_ai import get_mock_intelligence
from core.predictive_performance_ai import get_predictive_performance
from core.recommendation_ai import get_ai_recommendation
from core.study_planner_ai import get_personal_study_plan
from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
)
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.streak_ai import get_streak
from core.xp_ai import get_user_xp

logger = logging.getLogger(__name__)

# Standard TNPSC High Weightage Subject Hierarchy
STANDARD_SUBJECT_WEIGHTAGES = {
    "Polity": 95,
    "History": 90,
    "Economy": 88,
    "Geography": 85,
    "Unit 8": 84,
    "Unit 9": 82,
    "Aptitude": 80,
    "Science": 75,
    "Current Affairs": 70,
}


def _determine_revision_phase(days_remaining: int) -> str:
    """
    Selects the single relevant revision phase based on remaining timeline.
    Skips longer phases if the exam is close.
    """
    if days_remaining >= 90:
        return "90-Day Plan"
    elif days_remaining >= 60:
        return "60-Day Plan"
    elif days_remaining >= 30:
        return "30-Day Plan"
    elif days_remaining >= 15:
        return "15-Day Plan"
    elif days_remaining >= 7:
        return "7-Day Plan"
    elif days_remaining >= 3:
        return "3-Day Plan"
    else:
        return "1-Day Rapid Recall"


def _generate_daily_target(phase: str, readiness_score: int) -> str:
    """
    Generates dynamic daily revision target based on current revision phase and readiness.
    """
    if "90-Day" in phase or "60-Day" in phase:
        return "Revise 2 Core Topics + 30 MCQs + 1 Spaced Review"
    elif "30-Day" in phase:
        return "Revise 3 topics + 40 MCQs + 1 PYQ set"
    elif "15-Day" in phase:
        return "Revise 4 topics + 50 MCQs + 2 PYQ sets"
    elif "7-Day" in phase:
        return "Revise 5 High-Yield Topics + 60 Speed MCQs"
    elif "3-Day" in phase:
        return "Rapid formula & key concept review + 30 High-Yield MCQs"
    else:
        return "1-Day Bullet Notes + Formula Sheets + Rapid Recall Flashcards"


from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Adaptive Revision Engine")
def get_adaptive_final_revision(
    user: Optional[str] = None,
    target_days: Optional[int] = None,
    context: Optional[Any] = None,
    force_refresh: bool = False,
) -> Dict[str, Any]:
    """
    Adaptive Final Revision Strategy Engine V2 - Master Revision Strategy Hub.
    Synthesizes outputs across ALL core AI engines:
    - Exam Readiness Engine V2
    - Mock Intelligence Engine V2
    - Predictive Performance Engine V2
    - Recommendation Engine V2
    - Learning Intelligence Engine V2
    - Study Planner Engine V2
    - Revision Engine V2
    - Weakness Engine
    - Progress Engine
    
    Generates a personalized final revision strategy using deterministic adaptive rules.
    Dashboard displays engine output ONLY. Zero planning or evaluation calculations in UI.
    """
    user_str = str(user or "Guest")
    days_str = str(target_days or "default")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Adaptive Revision Engine_{user_str}_{days_str}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Adaptive Revision Engine")
        return st.session_state[cache_key]
    record_cache_miss("Adaptive Revision Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    # 1. Fetch Engine Outputs (Zero duplicate calculations)
    readiness = get_exam_readiness(user, context=ctx)
    mock_data = get_mock_intelligence(user, context=ctx)
    predictive = get_predictive_performance(user, context=ctx)
    recommendation = get_ai_recommendation(user, context=ctx)
    intelligence = get_learning_intelligence(user, context=ctx)
    study_plan = get_personal_study_plan(user, available_time=45, context=ctx)
    revision_plan = get_intelligent_revision_plan(user, context=ctx)
    revision_analytics = get_revision_analytics_v2(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    streak = get_streak(user, context=ctx)

    if target_days is not None:
        days_remaining = max(1, target_days)
    else:
        days_remaining = 30

    revision_phase = _determine_revision_phase(days_remaining)

    # 3. Deterministic Priority Calculation
    # Priority Cascade: Weak Subject Score -> Low Mock Accuracy -> Low Revision Health -> Low Repo Completion -> High Weightage
    subject_scores = {}
    
    # Extract weakness score per subject
    weak_subject_counts: Dict[str, int] = {}
    if isinstance(weakness_data, dict):
        for key, count in weakness_data.items():
            if "-" in key:
                subj = format_subject_name(key.split("-")[0])
                weak_subject_counts[subj] = weak_subject_counts.get(subj, 0) + count

    # Extract mock accuracy per subject
    mock_sections = mock_data.get("subject_breakdown", {})
    
    # Calculate subject priority metric
    all_subjects = list(
        set(
            list(STANDARD_SUBJECT_WEIGHTAGES.keys())
            + list(weak_subject_counts.keys())
            + list(mock_sections.keys())
        )
    )

    for subj in all_subjects:
        weak_penalty = weak_subject_counts.get(subj, 0) * 15.0
        mock_acc = float(mock_sections.get(subj, {}).get("accuracy", 70)) if isinstance(mock_sections.get(subj), dict) else 70.0
        mock_penalty = (100.0 - mock_acc) * 0.4
        weightage = float(STANDARD_SUBJECT_WEIGHTAGES.get(subj, 65))
        
        # Priority score: Higher score means HIGHER revision urgency
        priority_score = weak_penalty + mock_penalty + (100.0 - weightage * 0.5)
        subject_scores[subj] = round(priority_score, 2)

    # Rank subjects by priority urgency
    priority_subjects = sorted(subject_scores.keys(), key=lambda s: subject_scores[s], reverse=True)

    # Top priority subjects (top 3-4)
    top_priority_subjects = priority_subjects[:3] if len(priority_subjects) >= 3 else priority_subjects

    # 4. Priority Topics Identification
    priority_topics = []
    # Pull from weakness, recommendation, and top subjects
    if isinstance(weakness_data, dict) and weakness_data:
        for key in sorted(weakness_data.keys(), key=lambda k: weakness_data[k], reverse=True)[:3]:
            if "-" in key:
                parts = key.split("-")
                priority_topics.append(f"{format_subject_name(parts[0])}: {format_topic_name(parts[1])}")

    # Ensure fallback topics if weakness data is sparse
    if not priority_topics:
        priority_topics = [
            "Geography: Physical Geography & Climate",
            "Economy: Indian Economy & Planning",
            "Environment: Biodiversity & Ecology",
        ]
    else:
        # Normalize display format
        priority_topics = [t.replace("_", " ").title() for t in priority_topics[:3]]

    # 5. Revision Order Generation
    # Systematic sequence covering urgent priorities first, then foundational subjects
    revision_order = [subj for subj in priority_subjects if subj in STANDARD_SUBJECT_WEIGHTAGES][:4]
    if not revision_order:
        revision_order = ["Economy", "Geography", "Science", "History"]

    # 6. Daily Target & 4-Cycle Revision
    overall_readiness_score = int(readiness.get("overall_readiness_score", 68))
    daily_target = _generate_daily_target(revision_phase, overall_readiness_score)

    revision_cycles = [
        "Concept Reinforcement",
        "Practice Questions",
        "PYQ Revision",
        "Rapid Recall",
    ]

    # 7. Actionable Risk Analysis (Non-Fear Language)
    risk_analysis = []
    
    # Subject readiness risks
    lowest_subj = priority_subjects[0] if priority_subjects else "Geography"
    risk_analysis.append(f"Low {lowest_subj} readiness — prioritize concept reinforcement in Cycle 1.")
    
    # Mock behavior risk
    mistakes = mock_data.get("mistake_breakdown", {})
    assert_wrong = mistakes.get("Assertion & Reason", 0) if isinstance(mistakes, dict) else 0
    if assert_wrong > 0 or "Assertion" in str(mock_data):
        risk_analysis.append("Weak Assertion & Reason performance — incorporate focused 15-question daily drills.")
    else:
        risk_analysis.append("Statement & Reason question speed — allocate dedicated PYQ timed drills.")

    # Revision health risk
    rev_pct = revision_analytics.get("progress", {}).get("percentage", 70) if isinstance(revision_analytics, dict) else 70
    if rev_pct < 75:
        risk_analysis.append(f"Revision coverage at {rev_pct}% — increase spaced review frequency for overdue topics.")

    # Incomplete repository risk
    repo_comp = readiness.get("dimension_breakdown", {}).get("repository_completion", 65) if isinstance(readiness.get("dimension_breakdown"), dict) else 65
    if repo_comp < 70:
        risk_analysis.append(f"Hard topic repository completion at {repo_comp}% — complete targeted hard sets before exam week.")

    # 8. Actionable Mentor Revision Advice
    top_subj1 = top_priority_subjects[0] if len(top_priority_subjects) > 0 else "Geography"
    top_subj2 = top_priority_subjects[1] if len(top_priority_subjects) > 1 else "Economy"
    
    mentor_advice = (
        f"Focus on {top_subj1} and {top_subj2} first. "
        "Continue spaced revision and complete PYQ practice before moving to rapid recall."
    )

    # 9. Estimated Revision Completion
    target_comp_pct = min(98, max(75, overall_readiness_score + 15))
    est_days = max(1, int(round(days_remaining * 0.8)))
    estimated_completion = f"{target_comp_pct}% estimated revision completion in {est_days} days"

    # 10. Dashboard Sections Payload
    dashboard_sections = {
        "current_phase": revision_phase,
        "days_remaining": days_remaining,
        "priority_subjects": top_priority_subjects,
        "priority_topics": priority_topics,
        "revision_order": revision_order,
        "daily_target": daily_target,
        "revision_cycles": revision_cycles,
        "risk_analysis": risk_analysis,
        "mentor_advice": mentor_advice,
        "estimated_completion": estimated_completion,
        "completion_percentage": target_comp_pct,
        "readiness_score": overall_readiness_score,
    }

    return {
        "revision_phase": revision_phase,
        "days_remaining": days_remaining,
        "priority_subjects": top_priority_subjects,
        "priority_topics": priority_topics,
        "revision_order": revision_order,
        "daily_target": daily_target,
        "revision_cycles": revision_cycles,
        "risk_analysis": risk_analysis,
        "mentor_advice": mentor_advice,
        "estimated_completion": estimated_completion,
        "dashboard_sections": dashboard_sections,
    }

    cache_name = f"Adaptive Revision Engine_{target_days}" if target_days else "Adaptive Revision Engine"
    return get_cached_engine_result(
        cache_name, user, _compute, force_refresh=force_refresh
    )
