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
    
    # Observed subjects from actual progress
    observed_subjects = list(set(
        format_subject_name(r.get("subject", "")).strip()
        for r in (progress_rows or [])
        if r.get("subject")
    ))

    # Calculate subject priority metric based on genuine evidence
    all_subjects = list(
        set(
            list(STANDARD_SUBJECT_WEIGHTAGES.keys())
            + list(weak_subject_counts.keys())
            + list(mock_sections.keys())
        )
    )

    for subj in all_subjects:
        weak_penalty = weak_subject_counts.get(subj, 0) * 15.0
        mock_entry = mock_sections.get(subj) if isinstance(mock_sections, dict) else None
        mock_acc_val = mock_entry.get("accuracy") if isinstance(mock_entry, dict) else None
        if mock_acc_val is not None:
            mock_acc = float(mock_acc_val)
            mock_penalty = (100.0 - mock_acc) * 0.4
        else:
            mock_penalty = 0.0
        weightage = float(STANDARD_SUBJECT_WEIGHTAGES.get(subj, 65))
        
        # Priority score: Higher score means HIGHER revision urgency
        priority_score = weak_penalty + mock_penalty + (100.0 - weightage * 0.5)
        subject_scores[subj] = round(priority_score, 2)

    # Rank subjects by priority urgency
    priority_subjects = sorted(subject_scores.keys(), key=lambda s: subject_scores[s], reverse=True)

    # If user has observed subjects, prioritize observed practice topics and label coverage needs
    if observed_subjects:
        # Put observed subjects first if they have practice or need reinforcement
        top_priority_subjects = [s for s in observed_subjects if s in priority_subjects] + [s for s in priority_subjects if s not in observed_subjects]
        top_priority_subjects = top_priority_subjects[:3]
    else:
        top_priority_subjects = priority_subjects[:3] if len(priority_subjects) >= 3 else priority_subjects

    # 4. Priority Topics Identification (Evidence-driven)
    priority_topics = []
    # Pull from genuine recorded weakness
    if isinstance(weakness_data, dict) and weakness_data:
        for key in sorted(weakness_data.keys(), key=lambda k: weakness_data[k], reverse=True)[:3]:
            if "-" in key:
                parts = key.split("-")
                priority_topics.append(f"{format_subject_name(parts[0])}: {format_topic_name(parts[1])}")

    # If no recorded weakness, pull from genuine observed progress topics
    if not priority_topics and progress_rows:
        seen_topics = set()
        for r in reversed(progress_rows):
            s = format_subject_name(r.get("subject", "")).strip()
            t = format_topic_name(r.get("topic", "")).strip()
            if s and t and (s, t) not in seen_topics:
                seen_topics.add((s, t))
                priority_topics.append(f"{s}: {t}")
                if len(priority_topics) >= 3:
                    break

    # If still no topics (zero data user), explicitly label as Coverage recommendations
    if not priority_topics:
        priority_topics = [
            "Coverage Recommendation: Polity (Constitution of India)",
            "Coverage Recommendation: History (Early India)",
            "Coverage Recommendation: Economy (Fiscal Policy)",
        ]
    else:
        priority_topics = [t.replace("_", " ").title() for t in priority_topics[:3]]

    # 5. Revision Order Generation
    revision_order = [subj for subj in top_priority_subjects if subj in STANDARD_SUBJECT_WEIGHTAGES][:4]
    if not revision_order:
        revision_order = ["History", "Polity", "Economy", "Geography"]

    # 6. Daily Target & 4-Cycle Revision
    raw_readiness = readiness.get("overall_readiness_score")
    overall_readiness_score = int(raw_readiness) if raw_readiness is not None else None
    daily_target = _generate_daily_target(revision_phase, overall_readiness_score or 50)

    revision_cycles = [
        "Concept Reinforcement",
        "Practice Questions",
        "PYQ Revision",
        "Rapid Recall",
    ]

    # 7. Actionable Risk Analysis (Evidence-Based, No Synthetic Numbers)
    risk_analysis = []
    
    # Subject readiness risks: Only flag subjects that were genuinely assessed and scored < 70%
    assessed_subjs = [s for s in readiness.get("subjects", []) if s.get("score") is not None]
    low_scoring_subjs = [s for s in assessed_subjs if s["score"] < 70]
    if low_scoring_subjs:
        low_subj = low_scoring_subjs[0]
        risk_analysis.append(f"Low {low_subj['subject']} readiness ({low_subj['score']}%) — prioritize concept reinforcement in Cycle 1.")
    elif assessed_subjs:
        high_subj = assessed_subjs[0]
        risk_analysis.append(f"{high_subj['subject']} observed readiness is {high_subj['score']}% — expand syllabus coverage into other core subjects.")
    else:
        risk_analysis.append("Unassessed subjects — begin practice tests to identify strengths and weaknesses.")
    
    # Mock behavior risk
    mistakes = mock_data.get("mistake_breakdown", {})
    assert_wrong = mistakes.get("Assertion & Reason", 0) if isinstance(mistakes, dict) else 0
    if assert_wrong > 0:
        risk_analysis.append("Weak Assertion & Reason performance — incorporate focused 15-question daily drills.")
    elif mock_data.get("overall_accuracy") is not None:
        risk_analysis.append("Statement & Reason question speed — allocate dedicated PYQ timed drills.")
    else:
        risk_analysis.append("No mock exams attempted — attempt full-length mock tests to evaluate exam-day timing.")

    # Revision health risk (Strict Key Check)
    has_rev_records = bool(revision_analytics.get("total", 0) > 0 or revision_analytics.get("progress", {}).get("completed", 0) > 0)
    if has_rev_records:
        rev_progress = revision_analytics.get("progress", {}) if isinstance(revision_analytics, dict) else {}
        raw_rev_pct = rev_progress.get("percentage") if isinstance(rev_progress, dict) else None
        rev_pct = int(raw_rev_pct) if raw_rev_pct is not None else 70
        if rev_pct < 75:
            risk_analysis.append(f"Revision coverage at {rev_pct}% — increase spaced review frequency for overdue topics.")
    else:
        risk_analysis.append("No active spaced revisions scheduled — complete practice tests to populate revision schedule.")

    # Incomplete repository risk (Fixed Key Lookup)
    dim_breakdown = readiness.get("readiness_dimensions", {}) if isinstance(readiness, dict) else {}
    raw_repo_comp = dim_breakdown.get("repository_completion") if isinstance(dim_breakdown, dict) else None
    if raw_repo_comp is not None:
        repo_comp = int(raw_repo_comp)
        if repo_comp < 70:
            risk_analysis.append(f"Hard topic repository completion at {repo_comp}% — complete targeted hard sets before exam week.")
    else:
        risk_analysis.append("Hard repository questions not yet attempted — attempt challenging questions to establish depth.")

    # 8. Actionable Mentor Revision Advice
    top_subj1 = top_priority_subjects[0] if len(top_priority_subjects) > 0 else "History"
    top_subj2 = top_priority_subjects[1] if len(top_priority_subjects) > 1 else "Polity"
    
    if len(observed_subjects) < 2:
        mentor_advice = (
            f"Reinforce {top_subj1} and expand practice to at least 2 subjects "
            "to establish multi-subject readiness."
        )
    else:
        mentor_advice = (
            f"Focus on {top_subj1} and {top_subj2} first. "
            "Continue spaced revision and complete PYQ practice before moving to rapid recall."
        )

    # 9. Estimated Revision Completion (Gated behind genuine readiness)
    if overall_readiness_score is not None and readiness.get("is_eligible"):
        target_comp_pct = min(98, max(75, overall_readiness_score + 15))
        est_days = max(1, int(round(days_remaining * 0.8)))
        estimated_completion = f"{target_comp_pct}% estimated revision completion in {est_days} days"
    else:
        target_comp_pct = None
        estimated_completion = "Projected revision completion unlocks after completing multi-subject practice baseline."

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
        "completion_percentage": target_comp_pct,
        "dashboard_sections": dashboard_sections,
    }

    cache_name = f"Adaptive Revision Engine_{target_days}" if target_days else "Adaptive Revision Engine"
    return get_cached_engine_result(
        cache_name, user, _compute, force_refresh=force_refresh
    )
