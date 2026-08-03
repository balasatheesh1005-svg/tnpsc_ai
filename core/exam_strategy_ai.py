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
from core.adaptive_revision_ai import get_adaptive_final_revision
from core.recommendation_ai import get_ai_recommendation
from core.study_planner_ai import get_personal_study_plan
from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
)
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.streak_ai import get_streak

logger = logging.getLogger(__name__)

# TNPSC Standard Weightage reference for section allocation
TNPSC_SUBJECT_QUESTION_WEIGHTS = {
    "History": 35,
    "Polity": 35,
    "Aptitude": 25,
    "Economy": 25,
    "Geography": 20,
    "Science": 20,
    "Current Affairs": 20,
    "Unit 8": 10,
    "Unit 9": 10,
}


def _determine_overall_strategy(readiness_score: int, mock_accuracy: int) -> str:
    """
    Selects overarching execution theme based on current readiness and mock accuracy.
    """
    if readiness_score >= 80 and mock_accuracy >= 80:
        return "Strength-First High-Velocity Execution"
    elif readiness_score >= 65:
        return "Balanced Systematic Progression"
    else:
        return "High-Accuracy Tactical Focus"


from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Exam Strategy Engine")
def get_exam_strategy(
    user: Optional[str] = None,
    context: Optional[Any] = None,
    force_refresh: bool = False,
) -> Dict[str, Any]:
    """
    Exam Execution Strategy Engine V2 - Master Exam Execution Hub.
    Synthesizes outputs across ALL core AI engines:
    - Exam Readiness Engine V2
    - Mock Intelligence Engine V2
    - Predictive Performance Engine V2
    - Adaptive Final Revision Strategy Engine V2
    - Recommendation Engine V2
    - Learning Intelligence Engine V2
    - Study Planner Engine V2
    - Revision Engine V2
    - Progress & Weakness Engines
    
    Generates a personalized pre-exam execution strategy using deterministic rules.
    Dashboard displays engine output ONLY. Zero evaluation calculations in UI.
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Exam Strategy Engine_{user_str}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Exam Strategy Engine")
        return st.session_state[cache_key]
    record_cache_miss("Exam Strategy Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    readiness = get_exam_readiness(user, context=ctx)
    mock_data = get_mock_intelligence(user, context=ctx)
    predictive = get_predictive_performance(user, context=ctx)
    adaptive_revision = get_adaptive_final_revision(user, context=ctx)
    recommendation = get_ai_recommendation(user, context=ctx)
    intelligence = get_learning_intelligence(user, context=ctx)
    study_plan = get_personal_study_plan(user, available_time=45, context=ctx)
    weakness_data = get_weakness(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    streak = get_streak(user, context=ctx)

    readiness_score = int(readiness.get("overall_readiness_score", 70))
    mock_accuracy = int(mock_data.get("overall_accuracy", 74))

    overall_strategy = _determine_overall_strategy(readiness_score, mock_accuracy)

    # Rank subjects by strength, accuracy, and speed to build early exam momentum
    mock_sections = mock_data.get("subject_breakdown", {})
    
    weak_subject_counts: Dict[str, int] = {}
    if isinstance(weakness_data, dict):
        for key, count in weakness_data.items():
            if "-" in key:
                subj = format_subject_name(key.split("-")[0])
                weak_subject_counts[subj] = weak_subject_counts.get(subj, 0) + count

    # All active candidate subjects
    candidate_subjects = list(
        set(
            list(TNPSC_SUBJECT_QUESTION_WEIGHTS.keys())
            + list(weak_subject_counts.keys())
            + list(mock_sections.keys())
        )
    )

    subject_strength_scores = {}
    for subj in candidate_subjects:
        mock_acc = float(mock_sections.get(subj, {}).get("accuracy", 70)) if isinstance(mock_sections.get(subj), dict) else 70.0
        weak_count = weak_subject_counts.get(subj, 0)
        base_weight = TNPSC_SUBJECT_QUESTION_WEIGHTS.get(subj, 15)
        
        # Strength score: Higher means ATTEMPT FIRST (stronger mastery, lower weakness)
        strength_score = (mock_acc * 1.5) - (weak_count * 10.0) + (base_weight * 0.2)
        subject_strength_scores[subj] = round(strength_score, 2)

    # Sort subjects descending by strength score (strongest first)
    subject_order = sorted(subject_strength_scores.keys(), key=lambda s: subject_strength_scores[s], reverse=True)
    top_subject_order = subject_order[:5] if len(subject_order) >= 5 else subject_order

    # 4. Section-Wise Time Allocation Methodology
    total_exam_minutes = 180
    # Reserve explicit Review & Buffer time (e.g. 15-25 mins based on exam length)
    review_buffer_minutes = max(10, min(30, int(round(total_exam_minutes * 0.12))))
    available_subject_minutes = total_exam_minutes - review_buffer_minutes

    # Allocate subject minutes proportional to TNPSC question weightages
    selected_subjects = top_subject_order
    total_weights = sum(TNPSC_SUBJECT_QUESTION_WEIGHTS.get(s, 20) for s in selected_subjects)
    if total_weights <= 0:
        total_weights = 100

    time_plan = []
    allocated_sum = 0
    for idx, subj in enumerate(selected_subjects):
        weight = TNPSC_SUBJECT_QUESTION_WEIGHTS.get(subj, 20)
        # Calculate raw proportional minutes
        if idx == len(selected_subjects) - 1:
            # Last subject gets exact remainder of available_subject_minutes
            mins = available_subject_minutes - allocated_sum
        else:
            mins = int(round((weight / total_weights) * available_subject_minutes))
            allocated_sum += mins
        
        mins = max(5, mins)
        time_plan.append({"subject": subj, "minutes": mins})

    # Add explicit review & buffer time entry
    time_plan.append({"subject": "Review & Buffer", "minutes": review_buffer_minutes})

    # 5. Question Decision Framework (Guidance only, zero answers generated)
    top_subj = selected_subjects[0] if selected_subjects else "History"
    lowest_subj = selected_subjects[-1] if len(selected_subjects) > 1 else "Economy"

    question_strategy = [
        f"Answer Easy direct questions in {top_subj} & Polity immediately on Pass 1.",
        "Think briefly (max 45s) on Moderate statement-based questions.",
        "Mark Hard Assertion & Reason questions for review in Pass 2.",
        f"Skip completely unknown topics in {lowest_subj} and move forward without lingering.",
    ]

    # 6. Skip & Return Strategy (Prevent Time-Traps)
    skip_strategy = [
        "If any single Economy calculation takes > 75 seconds, skip immediately and mark for Pass 2.",
        "Do not spend > 90 seconds on complex multi-statement matching questions during Pass 1.",
        "Maintain a steady pace of 45-50 seconds per question on standard direct MCQs.",
    ]

    # 7. Review Strategy (Priority sequence for marked questions)
    review_order = [
        "Assertion & Reason Questions",
        "Statement Questions",
        "Chronology Questions",
        "Match the Following",
        "Marked Calculation Questions",
    ]

    # 8. Risk Awareness (Constructive & Actionable Guidance, Non-Fear Wording)
    risk_alerts = []
    
    # Overthinking Risk
    risk_alerts.append("Overthinking Risk: Avoid changing initial answers on direct factual questions unless clear evidence is found.")
    
    # Time Pressure Risk
    if review_buffer_minutes < 15:
        risk_alerts.append("Time Pressure Risk: Strictly enforce the section time limits to preserve a 15-minute final review buffer.")
    else:
        risk_alerts.append("Time Pressure Risk: Monitor elapsed time at the 60-minute mark to ensure pace matches targets.")

    # Weak Subject Risk
    risk_alerts.append(f"Weak Subject Risk: Avoid spending excessive time on {lowest_subj} early in the exam.")

    # Guessing / Fatigue Risk
    risk_alerts.append("Fatigue & Guessing Risk: Take a 5-second mental reset between section transitions to maintain accuracy.")

    # 9. Strategy Confidence Calculation
    # Deterministic confidence based on mock history consistency, readiness, and streak
    streak_val = float(streak) if isinstance(streak, (int, float)) else 5.0
    raw_confidence = (readiness_score * 0.45) + (mock_accuracy * 0.45) + min(10.0, streak_val * 0.8)
    strategy_confidence = max(65, min(98, int(round(raw_confidence))))

    confidence_reason = (
        "The strategy is supported by consistent mock history, "
        "stable readiness evaluation, and deterministic performance trends."
    )

    # 10. Mentor Strategy Advice
    mentor_strategy = (
        f"Begin with {top_subj} to build early momentum and confidence. "
        f"Stick strictly to time allocations and reserve the final {review_buffer_minutes} minutes for systematic review."
    )

    # 11. Dashboard Sections Payload
    dashboard_sections = {
        "overall_strategy": overall_strategy,
        "subject_order": top_subject_order,
        "time_plan": time_plan,
        "question_strategy": question_strategy,
        "skip_strategy": skip_strategy,
        "review_order": review_order,
        "risk_alerts": risk_alerts,
        "strategy_confidence": strategy_confidence,
        "confidence_reason": confidence_reason,
        "mentor_strategy": mentor_strategy,
        "total_exam_minutes": total_exam_minutes,
        "review_buffer_minutes": review_buffer_minutes,
    }

    return {
        "overall_strategy": overall_strategy,
        "subject_order": top_subject_order,
        "time_plan": time_plan,
        "question_strategy": question_strategy,
        "skip_strategy": skip_strategy,
        "review_order": review_order,
        "risk_alerts": risk_alerts,
        "strategy_confidence": strategy_confidence,
        "confidence_reason": confidence_reason,
        "mentor_strategy": mentor_strategy,
        "dashboard_sections": dashboard_sections,
    }

    return get_cached_engine_result(
        "Exam Strategy Engine", user, _compute, force_refresh=force_refresh
    )
