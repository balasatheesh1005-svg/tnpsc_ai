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
    intelligence = get_learning_intelligence(user, context=ctx)
    study_plan = get_personal_study_plan(user, available_time=45, context=ctx)
    revision_plan = get_intelligent_revision_plan(user, context=ctx)
    revision_analytics = get_revision_analytics_v2(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)
    streak = get_streak(user, context=ctx)
    xp_data = get_user_xp(user, context=ctx)
    mission = get_today_mission(user, context=ctx)
    memory = get_memory(user, context=ctx)

    # Key Data Extracted
    subj = intelligence.get("subject", "History")
    topic = intelligence.get("topic", "Modern India")
    repo = intelligence.get("repository", "Hard Repository")
    qtype = intelligence.get("question_type", "Assertion & Reason")
    current_mastery = float(intelligence.get("current_mastery", 45.0))
    target_mastery = float(intelligence.get("mastery_probability", 80.0))
    root_cause = intelligence.get("root_cause", "Concept Application")
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

    # 2. Risk Detection System
    if overdue_count > 0 or has_overdue:
        risk_name = "Overdue Revision Risk"
        risk_level = "Critical" if overdue_count >= 3 else "High"
        risk_desc = f"You have {max(1, overdue_count)} overdue revision item(s) suffering memory decay."
    elif rev_pct < 50:
        risk_name = "Low Revision Habit"
        risk_level = "High"
        risk_desc = "Spaced revision frequency is below target threshold. High risk of forgetting previously studied concepts."
    elif avg_hard < 50:
        risk_name = "Weak Hard Repository Accuracy"
        risk_level = "High"
        risk_desc = f"Hard repository accuracy ({round(avg_hard, 1)}%) is preventing topic mastery in {format_subject_name(subj)}."
    elif avg_pyq < 55:
        risk_name = "Low PYQ Exam Performance"
        risk_level = "Medium"
        risk_desc = f"Previous Year Question accuracy ({round(avg_pyq, 1)}%) requires targeted practice before full mock test."
    elif streak == 0 and len(progress_rows) > 0:
        risk_name = "Broken Study Streak"
        risk_level = "Medium"
        risk_desc = "Daily study streak has reset. Complete today's mission to rebuild learning momentum."
    else:
        risk_name = "Optimal Progress"
        risk_level = "Low"
        risk_desc = "No critical learning risks detected. Progress is on track for topic mastery."

    # 3. Priority Order Cascade (Determines EXACTLY ONE Primary Recommendation)
    if has_overdue:
        priority = "Critical"
        recommendation_type = "Revise Today"
        primary_recommendation = f"Revise Overdue Topics: {format_subject_name(subj)} → {format_topic_name(topic)}"
        current_action = "Clear Overdue Spaced Revisions"
        next_action = "Attempt Targeted Bottleneck Practice Set"
        explanation = (
            f"Overdue revisions detected in {format_subject_name(subj)}. "
            f"Clearing these spaced recall items will prevent memory decay before starting new topics."
        )
    elif current_mastery < 60.0 or "Assertion" in qtype or "Statement" in qtype:
        priority = "High"
        recommendation_type = "Continue Recovery"
        primary_recommendation = f"Revise {format_subject_name(subj)} {format_topic_name(topic)} ({qtype})"
        current_action = "Complete Targeted Bottleneck Recovery Set"
        next_action = f"Attempt {format_subject_name(subj)} PYQ Repository"
        explanation = (
            f"Your current accuracy in {qtype} ({current_mastery}%) is identified as the primary learning bottleneck. "
            f"Executing this focused recovery set will elevate topic mastery to projected {target_mastery}%."
        )
    elif len(rec_plan) > 0:
        priority = "Medium-High"
        recommendation_type = "Complete Hard Repository"
        primary_recommendation = f"Execute Recovery Step: {rec_step}"
        current_action = "Guided Concept Notes & Hard Repository Practice"
        next_action = "Verify Readiness on PYQ Set"
        explanation = (
            f"You are currently executing the 4-step recovery plan for {format_topic_name(topic)}. "
            f"Completing this step directly addresses {root_cause}."
        )
    elif current_mastery < 75.0:
        priority = "Medium"
        recommendation_type = "Maintain Streak"
        today_tasks_count = len(study_plan.get("today_plan", []))
        primary_recommendation = f"Complete Today's Study Plan ({today_tasks_count} Tasks)"
        current_action = "Execute Today's Prioritized Study Plan"
        next_action = "Review Updated Topic Mastery Scores"
        explanation = (
            f"Today's plan is tailored to build steady topic progress in {format_subject_name(subj)}. "
            f"Completing all {today_tasks_count} tasks will maintain your study streak and earn bonus XP."
        )
    elif current_mastery >= 85.0:
        priority = "Standard"
        recommendation_type = "Start Next Topic"
        primary_recommendation = f"Mastery Achieved ({current_mastery}%) • Proceed to Next Topic in {format_subject_name(subj)}"
        current_action = "Start Concept Notes for Next Curriculum Topic"
        next_action = "Attempt Foundation Practice Set"
        explanation = (
            f"You have achieved high topic mastery ({current_mastery}%) in {format_topic_name(topic)}. "
            f"You are ready to advance to the next topic in the TNPSC syllabus."
        )
    else:
        priority = "Standard"
        recommendation_type = "Start Grand Test"
        primary_recommendation = f"Take Full Grand Mock Test in {format_subject_name(subj)}"
        current_action = "Simulate Full Length Exam Test"
        next_action = "Analyze Comprehensive Test Score & Speed"
        explanation = (
            f"Your foundational and application scores are solid ({current_mastery}%). "
            f"Taking a Grand Test will test your timed performance under exam conditions."
        )

    # 4. Estimated Benefit Calculation
    estimated_mastery_gain = min(20.0, max(5.0, round((100.0 - current_mastery) * 0.25, 1)))
    estimated_benefit = {
        "mastery": f"+{estimated_mastery_gain:.0f}%",
        "xp": "+50 XP" if priority == "Critical" else "+40 XP",
        "confidence": "High Confidence" if risk_level in ["Low", "Medium"] else "Medium Confidence",
        "completion_progress": "+15% Topic Progress",
    }

    # 5. Recommendation Confidence Score (70% - 98%)
    base_confidence = 90
    if risk_level == "Low":
        base_confidence += 4
    elif risk_level == "Critical":
        base_confidence -= 6

    if len(progress_rows) >= 10:
        base_confidence += 2
        confidence_reason = "High confidence based on rich historical attempt data across multiple repositories."
    elif len(progress_rows) >= 3:
        confidence_reason = "Solid confidence based on recent test performance trends and learning intelligence alignment."
    else:
        base_confidence -= 12
        confidence_reason = "Moderate confidence due to limited recent test activity. Complete more sets to refine precision."

    confidence_score = max(70, min(98, base_confidence))

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
        "confidence": confidence_score,
        "confidence_reason": confidence_reason,
        "explanation": explanation,
        "mentor_message": mentor_message,
        "learning_bottleneck": intelligence.get("learning_bottleneck", f"{subj} ↓ {topic}"),
    }

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result
