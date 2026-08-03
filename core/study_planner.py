"""
Legacy adapter module for study_planner.
Delegates to core.study_planner_ai (Personal Study Planner Engine V2).
"""
from core.study_planner_ai import get_personal_study_plan

def get_today_plan(user=None):
    """Legacy helper function delegating to Study Planner Engine V2."""
    plan_v2 = get_personal_study_plan(user=user)
    today_tasks = plan_v2.get("today_plan", [])
    first_task = today_tasks[0] if today_tasks else {}
    
    return {
        "topic": first_task.get("topic", "Polity - Historical Background"),
        "subject": first_task.get("subject", "Polity"),
        "questions": 10,
        "mode": first_task.get("reason", "Weakness Focus 🔥"),
        "planner_v2": plan_v2
    }