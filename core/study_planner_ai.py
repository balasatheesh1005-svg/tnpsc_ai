import logging
from typing import Dict, List, Any, Optional
import streamlit as st

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

    # 1. Fetch Engine Outputs (Zero duplicate logic)
    intelligence = get_learning_intelligence(user, context=ctx)
    revision_plan = get_intelligent_revision_plan(user, context=ctx)
    revision_analytics = get_revision_analytics_v2(user, context=ctx)
    mission = get_today_mission(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)
    streak = get_streak(user, context=ctx)
    xp_data = get_user_xp(user, context=ctx)
    memory = get_memory(user, context=ctx)


    # Extract Key Parameters from Engines
    subj = intelligence.get("subject", "History")
    topic = intelligence.get("topic", "Modern India")
    repo = intelligence.get("repository", "Hard Repository")
    qtype = intelligence.get("question_type", "Assertion & Reason")
    bottleneck_acc = intelligence.get("current_mastery", 45.0)
    target_mastery = intelligence.get("mastery_probability", 80.0)

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

    # Priority 2: Current Learning Bottleneck
    candidate_tasks.append({
        "priority": 2,
        "priority_label": _determine_priority_label(2),
        "task": "Weakness Practice",
        "subject": format_subject_name(subj),
        "topic": format_topic_name(topic),
        "repository": repo,
        "question_type": qtype,
        "duration": 18,
        "reason": f"Current Bottleneck ({intelligence.get('root_cause', 'Concept Application')})",
        "expected_benefit": f"Elevate Mastery from {bottleneck_acc}% to {target_mastery}%",
        "reward": "+35 XP",
        "xp_num": 35,
    })

    # Priority 3: Recovery Plan Step
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
    # Select tasks that fit within available_time
    selected_tasks = []
    accumulated_time = 0

    for candidate in candidate_tasks:
        candidate_dur = candidate["duration"]
        # If adding candidate fits within available_time or if it's the very first critical task
        if accumulated_time + candidate_dur <= available_time or not selected_tasks:
            selected_tasks.append(candidate)
            accumulated_time += candidate_dur
        elif available_time <= 20 and len(selected_tasks) >= 1:
            # 20 min cap: max 1-2 critical tasks
            break
        elif available_time <= 45 and accumulated_time >= 35:
            break
        elif available_time <= 90 and accumulated_time >= 80:
            break

    # Re-index task priority sequentially for the selected plan
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

    # 4. Expected Outcome Logic
    current_m = round(bottleneck_acc, 1)
    # Estimate mastery gain based on number of tasks completed
    mastery_gain_val = round(min(25.0, 4.0 * len(today_plan) + (total_duration * 0.15)), 1)
    expected_m = round(min(98.0, current_m + mastery_gain_val), 1)

    if current_m < 50:
        curr_conf = "Low"
        exp_conf = "Medium" if expected_m >= 60 else "Low-Medium"
    elif current_m < 75:
        curr_conf = "Medium"
        exp_conf = "High"
    else:
        curr_conf = "High"
        exp_conf = "Mastery / Expert"

    expected_outcome = {
        "current_mastery": f"{current_m}%",
        "expected_mastery": f"{expected_m}%",
        "expected_mastery_gain": f"+{mastery_gain_val}%",
        "current_confidence": curr_conf,
        "expected_confidence": exp_conf,
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
    if has_overdue and len(today_plan) <= 2:
        next_action = "Continue Recovery Session for Weakest Topics"
    elif any(t["task"] == "Weakness Practice" for t in today_plan):
        next_action = f"Attempt {subj} PYQ Repository to verify mastery"
    elif any(t["task"] == "PYQ Practice Set" for t in today_plan):
        next_action = "Take full Grand Test session"
    else:
        next_action = f"Move to next topic in {subj}"

    # 7. Mentor Message
    mentor_message = intelligence.get(
        "mentor_insight",
        f"Today's plan is tailored for {available_time} minutes of focused preparation on {topic}."
    )

    # 8. Master JSON Output
    result = {
        "subject": subj,
        "topic": topic,
        "today_plan": today_plan,
        "estimated_time": total_duration,
        "available_time": available_time,
        "expected_mastery_gain": f"+{mastery_gain_val}%",
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
            "expected_mastery_gain": f"+{mastery_gain_val}%",
        },
    }

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result

