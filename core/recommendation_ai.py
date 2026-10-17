import logging
from typing import Dict, List, Any, Optional
import streamlit as st

from core.learning_intelligence_ai import (
    get_learning_intelligence,
    format_subject_name,
    format_topic_name,
)
from core.study_planner_ai import get_personal_study_plan
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


from core.performance import measure_time
from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Recommendation Engine")
def get_ai_recommendation(
    user: Optional[str] = None,
    context: Optional[Any] = None,
    force_refresh: bool = False,
) -> Dict[str, Any]:
    """
    AI Recommendation Engine V2 - Single Recommendation Authority.
    Synthesizes outputs from Learning Intelligence V2, Study Planner V2,
    Revision Engine V2, Progress, Weakness, Streak, and XP Engines.
    
    Generates ONE primary recommendation following a strict priority cascade.
    Dashboard displays output ONLY. Zero calculations performed in UI.
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Recommendation Engine_{user_str}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Recommendation Engine")
        return st.session_state[cache_key]
    record_cache_miss("Recommendation Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    # 1. Fetch Master Engine Outputs (Zero duplicate logic)
    intelligence = get_learning_intelligence(user, context=ctx) or {}
    study_plan = get_personal_study_plan(user, available_time=45, context=ctx) or {}
    revision_plan = get_intelligent_revision_plan(user, context=ctx) or {}
    revision_analytics = get_revision_analytics_v2(user, context=ctx) or {}
    progress_rows = get_progress(user, context=ctx) or []
    weakness_data = get_weakness(user, context=ctx) or {}
    streak = get_streak(user, context=ctx) or 0
    xp_data = get_user_xp(user, context=ctx) or {}
    mission = get_today_mission(user, context=ctx) or {}
    memory = get_memory(user, context=ctx) or {}

    # Key Data Extracted
    has_history = len(progress_rows) > 0 or bool(weakness_data)
    if not has_history:
        subj = "Indian Polity"
        topic = "Fundamental Rights"
        repo = "Easy Repository"
        qtype = "Standard MCQ"
        current_mastery = 0.0
        target_mastery = 80.0
        root_cause = "No Test History"
        rec_plan = []
        rec_step = "Attempt first practice set"
    else:
        subj = intelligence.get("subject") or "History"
        topic = intelligence.get("topic") or "General"
        repo = intelligence.get("repository") or "Medium Repository"
        qtype = intelligence.get("question_type") or "Standard MCQ"
        raw_mastery = intelligence.get("current_mastery")
        current_mastery = float(raw_mastery) if raw_mastery is not None else 50.0
        raw_target = intelligence.get("mastery_probability")
        target_mastery = float(raw_target) if raw_target is not None else 80.0
        root_cause = intelligence.get("root_cause") or "Concept Application"
        rec_plan = intelligence.get("recovery_plan", [])
        rec_step = rec_plan[0] if rec_plan else f"Revise {qtype} notes"

    overdue_items = revision_analytics.get("overdue", [])
    due_today_items = revision_analytics.get("due_today", [])
    has_overdue = len(overdue_items) > 0 or revision_plan.get("status") == "Overdue"
    overdue_count = len(overdue_items)

    rev_prog = revision_analytics.get("progress", {})
    rev_pct = rev_prog.get("percentage", 80)

    # Analyze performance metrics
    hard_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "hard" in str(r.get("topic", "")).lower()]
    avg_hard = sum(hard_accs) / len(hard_accs) if hard_accs else (current_mastery * 0.8)
    pyq_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "pyq" in str(r.get("topic", "")).lower()]
    avg_pyq = sum(pyq_accs) / len(pyq_accs) if pyq_accs else 60.0

    # Coach Maturity / Evidence Tier integration
    try:
        from core.coach_maturity_ai import get_coach_maturity
        maturity = get_coach_maturity(user, context=ctx)
        tier_label = maturity.get("tier_label", "No Data")
        tier_key = maturity.get("tier", "TIER_0_NO_DATA")
    except Exception as e:
        logger.warning(f"Error fetching coach maturity in recommendation_ai: {e}")
        if not progress_rows and not weakness_data:
            tier_label = "No Data"
            tier_key = "TIER_0_NO_DATA"
        elif len(progress_rows) < 5:
            tier_label = "Early Signal"
            tier_key = "TIER_1_EARLY_SIGNAL"
        else:
            tier_label = "Developing"
            tier_key = "TIER_2_DEVELOPING"

    # 2. Risk Detection System (Strictly grounded in observed evidence)
    if not progress_rows and not weakness_data:
        risk_name = "No Diagnostic Baseline"
        risk_level = "Low"
        risk_desc = "No test history recorded yet. Complete your first practice test to begin building your baseline."
    elif overdue_count > 0 or has_overdue:
        risk_name = "Overdue Revision Risk"
        risk_level = "Critical" if overdue_count >= 3 else "High"
        risk_desc = f"You have {max(1, overdue_count)} overdue revision item(s) requiring review."
    elif weakness_data:
        risk_name = "Concept Weakness Identified"
        risk_level = "High"
        top_weak = sorted(weakness_data.items(), key=lambda x: x[1], reverse=True)[0][0]
        weak_display = top_weak.split("-", 1)[1].replace("_", " ").title() if "-" in top_weak else top_weak.replace("_", " ").title()
        risk_desc = f"Identified recurring errors in {weak_display}. Targeted practice recommended."
    elif avg_hard < 50 and hard_accs:
        risk_name = "Weak Hard Repository Accuracy"
        risk_level = "High"
        risk_desc = f"Hard repository accuracy ({round(avg_hard, 1)}%) indicates higher-order questions need practice in {format_subject_name(subj)}."
    elif avg_pyq < 55 and pyq_accs:
        risk_name = "Low PYQ Exam Performance"
        risk_level = "Medium"
        risk_desc = f"Previous Year Question accuracy ({round(avg_pyq, 1)}%) requires targeted practice before full mock test."
    elif len(progress_rows) >= 5 and rev_pct < 50 and (len(overdue_items) > 0 or len(due_today_items) > 0):
        risk_name = "Revision Schedule Behind"
        risk_level = "Medium"
        risk_desc = "Spaced revision completion is below target threshold for scheduled topics."
    elif len(progress_rows) < 5:
        # Early learner with low data: do NOT infer a habit!
        risk_name = "Early Learning Baseline"
        risk_level = "Low"
        risk_desc = f"Early baseline established ({len(progress_rows)} test(s)). Continue consistent practice to build reliable performance trends."
    elif streak == 0 and len(progress_rows) >= 5:
        risk_name = "Study Streak Reset"
        risk_level = "Medium"
        risk_desc = "Daily study streak has reset. Complete today's practice set to rebuild learning momentum."
    else:
        risk_name = "Optimal Progress"
        risk_level = "Low"
        risk_desc = "No critical learning risks detected. Progress is on track for topic mastery."

    # 3. Priority Order Cascade (Determines EXACTLY ONE Primary Recommendation)
    if not progress_rows and not weakness_data:
        priority = "Standard"
        recommendation_type = "Starter Path"
        primary_recommendation = "Begin Practice: Indian Polity → Fundamental Rights"
        current_action = "Start First Practice Test"
        next_action = "Review Diagnostic Accuracy"
        explanation = "Start with Fundamental Rights to begin building your baseline learning profile."
        learning_focus = "Diagnostic Baseline"
    elif has_overdue:
        priority = "Critical"
        recommendation_type = "Revise Today"
        primary_recommendation = f"Revise Overdue Topics: {format_subject_name(subj)} → {format_topic_name(topic)}"
        current_action = "Clear Overdue Spaced Revisions"
        next_action = "Attempt Targeted Bottleneck Practice Set"
        explanation = (
            f"Overdue revisions detected in {format_subject_name(subj)}. "
            f"Clearing these spaced recall items will prevent memory decay before starting new topics."
        )
        learning_focus = "Spaced Retention"
    elif weakness_data:
        priority = "High"
        recommendation_type = "Continue Recovery"
        weak_topic_display = format_topic_name(intelligence.get("weak_topic") or topic)
        primary_recommendation = f"Revise Weak Area: {format_subject_name(subj)} → {weak_topic_display}"
        current_action = "Complete Targeted Weakness Practice Set"
        next_action = f"Attempt {format_subject_name(subj)} PYQ Repository"
        explanation = (
            f"Weakness detected in {weak_topic_display}. "
            f"Executing a focused practice set will help eliminate errors and raise your score."
        )
        learning_focus = "Concept Reinforcement"
    elif current_mastery < 60.0 and len(progress_rows) >= 5:
        priority = "High"
        recommendation_type = "Continue Recovery"
        primary_recommendation = f"Revise {format_subject_name(subj)} {format_topic_name(topic)}"
        current_action = "Complete Targeted Concept Practice Set"
        next_action = f"Attempt {format_subject_name(subj)} PYQ Repository"
        explanation = (
            f"Your current accuracy in {format_topic_name(topic)} ({current_mastery}%) is identified as a learning bottleneck. "
            f"Executing this focused recovery set will help address concept gaps."
        )
        learning_focus = "Concept Reinforcement"
    elif len(rec_plan) > 0 and len(progress_rows) >= 5:
        priority = "Medium-High"
        recommendation_type = "Complete Hard Repository"
        primary_recommendation = f"Execute Recovery Step: {rec_step}"
        current_action = "Guided Concept Notes & Hard Repository Practice"
        next_action = "Verify Readiness on PYQ Set"
        explanation = (
            f"You are currently executing the 4-step recovery plan for {format_topic_name(topic)}. "
            f"Completing this step directly addresses {root_cause}."
        )
        learning_focus = "Advanced Application"
    elif current_mastery < 75.0 and len(progress_rows) > 0:
        priority = "Medium"
        recommendation_type = "Maintain Streak"
        today_tasks_count = len(study_plan.get("today_plan", []))
        primary_recommendation = f"Complete Today's Study Plan ({today_tasks_count} Tasks)"
        current_action = "Execute Today's Prioritized Study Plan"
        next_action = "Review Updated Topic Mastery Scores"
        explanation = (
            f"Today's plan is tailored to build steady topic progress in {format_subject_name(subj)}. "
            f"Completing today's tasks will maintain your study consistency."
        )
        learning_focus = "Study Consistency"
    elif current_mastery >= 85.0 and len(progress_rows) >= 5:
        priority = "Standard"
        recommendation_type = "Start Next Topic"
        primary_recommendation = f"Mastery Achieved ({current_mastery}%) • Proceed to Next Topic in {format_subject_name(subj)}"
        current_action = "Start Concept Notes for Next Curriculum Topic"
        next_action = "Attempt Foundation Practice Set"
        explanation = (
            f"You have achieved high topic mastery ({current_mastery}%) in {format_topic_name(topic)}. "
            f"You are ready to advance to the next topic in the TNPSC syllabus."
        )
        learning_focus = "Syllabus Progression"
    else:
        priority = "Standard"
        recommendation_type = "Practice Path"
        primary_recommendation = f"Practice {format_subject_name(subj)} Topics"
        current_action = "Attempt Practice Questions"
        next_action = "Review Performance"
        explanation = f"Continue consistent daily practice in {format_subject_name(subj)} to build topic mastery."
        learning_focus = "Concept Reinforcement"

    # 4. Estimated Benefit Calculation (Qualitative evidence-backed focus; no synthetic mastery or fixed XP claims)
    if not progress_rows and not weakness_data:
        estimated_benefit = {
            "focus": "Diagnostic Baseline",
            "impact": "Baseline Calibration",
            "mastery": "Diagnostic Baseline",
            "xp": "Rule-based XP",
            "confidence": f"Evidence: {tier_label}",
            "completion_progress": "Diagnostic Start",
        }
    else:
        estimated_benefit = {
            "focus": learning_focus,
            "impact": learning_focus,
            "mastery": learning_focus,
            "xp": "Rule-based XP",
            "confidence": f"Evidence: {tier_label}",
            "completion_progress": "Topic Progression",
        }

    # 5. Recommendation Evidence & Confidence Grounding
    if tier_key == "TIER_0_NO_DATA":
        confidence_reason = "No test history available. Complete your first practice test to establish baseline performance."
    elif tier_key == "TIER_1_EARLY_SIGNAL":
        confidence_reason = f"Early signal based on {len(progress_rows)} test attempt(s). Complete more practice sets to establish reliable patterns."
    elif tier_key == "TIER_2_DEVELOPING":
        confidence_reason = f"Developing profile based on {len(progress_rows)} attempts. Continue across more subjects and mock tests to establish reliable trends."
    else:
        confidence_reason = f"Reliable profile supported by {len(progress_rows)} attempts across multiple subjects and mock tests."

    # 6. Mentor Message
    mentor_message = intelligence.get(
        "mentor_insight",
        f"Focus on {primary_recommendation} today to maximize score growth."
    )

    # 7. Return Master Output Schema
    result = {
        "current_action": current_action,
        "next_action": next_action,
        "recommendation": primary_recommendation,
        "recommendation_type": recommendation_type,
        "priority": priority,
        "subject": format_subject_name(subj),
        "topic": format_topic_name(topic),
        "repository": repo,
        "question_type": qtype,
        "risk": risk_name,
        "risk_level": risk_level,
        "risk_description": risk_desc,
        "estimated_benefit": estimated_benefit,
        "confidence": None,
        "confidence_reason": confidence_reason,
        "evidence_tier": tier_key,
        "evidence_label": tier_label,
        "explanation": explanation,
        "mentor_message": mentor_message,
        "learning_bottleneck": intelligence.get("learning_bottleneck", "No critical bottleneck detected"),
        "is_eligible": len(progress_rows) > 0 or bool(weakness_data),
    }

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result
