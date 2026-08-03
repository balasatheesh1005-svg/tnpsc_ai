import datetime
import logging
from typing import Dict, List, Any, Optional

from core.progress_ai import get_progress
from core.revision_ai import (
    add_revision,
    add_revision_topic,
    get_due_revisions,
    get_revision_overview,
    update_revision,
)
from core.weakness_ai import get_weakness

logger = logging.getLogger(__name__)


def format_subject_name(subject: str) -> str:
    """Helper to format subject name cleanly."""
    if not subject:
        return "General"
    return str(subject).replace("_", " ").replace("-", " ").title()


def format_topic_name(topic: str) -> str:
    """Helper to format topic name cleanly."""
    if not topic:
        return "General"
    return str(topic).replace("_", " ").replace("-", " ").title()


# Standard Question Types & Repositories Mapping
QUESTION_TYPES = [
    "easy",
    "medium",
    "hard",
    "statement_based",
    "assertion_reason",
    "match_the_following",
    "chronology",
    "pyq",
    "grand_test",
]

TYPE_DISPLAY_NAMES = {
    "easy": "Easy Questions",
    "medium": "Medium Questions",
    "hard": "Hard Questions",
    "statement_based": "Statement Based",
    "assertion_reason": "Assertion & Reason",
    "match_the_following": "Match the Following",
    "chronology": "Chronology",
    "pyq": "PYQ Repository",
    "grand_test": "Grand Test",
}

REPOSITORY_DISPLAY_NAMES = {
    "easy": "Foundation Repository",
    "medium": "Medium Repository",
    "hard": "Hard Repository",
    "statement_based": "Statement Based Repository",
    "assertion_reason": "Analytical Repository",
    "match_the_following": "Match Matrix Repository",
    "chronology": "Timeline Repository",
    "pyq": "PYQ Repository",
    "grand_test": "Grand Test Repository",
}

DIFFICULTY_MAP = {
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard",
    "statement_based": "Hard",
    "assertion_reason": "Very Hard",
    "match_the_following": "Medium",
    "chronology": "Hard",
    "pyq": "Hard",
    "grand_test": "Very Hard",
}


def _analyze_5_level_target(subject: str, topic: str, progress_rows: List[Dict[str, Any]], weakness_data: Dict[str, int]) -> Dict[str, Any]:
    """
    Computes 5-level precision target:
    Level 1: Subject
    Level 2: Topic
    Level 3: Repository
    Level 4: Question Type
    Level 5: Difficulty
    """
    subj_clean = (subject or "polity").lower().strip()
    topic_clean = (topic or "general").lower().strip()

    # Find matching progress records for this topic
    matching_progress = []
    for row in progress_rows:
        row_subj = str(row.get("subject", "")).lower()
        row_topic = str(row.get("topic", "")).lower()
        if row_subj == subj_clean and (topic_clean in row_topic or row_topic in topic_clean):
            matching_progress.append(row)

    # Determine question type with lowest accuracy
    type_accuracies = {}
    for q_type in QUESTION_TYPES:
        type_rows = [r for r in matching_progress if q_type in str(r.get("topic", "")).lower()]
        if type_rows:
            accs = [float(r.get("accuracy", 0)) for r in type_rows if r.get("accuracy") is not None]
            if accs:
                type_accuracies[q_type] = sum(accs) / len(accs)

    # Default logic if no specific type breakdown
    if "assertion_reason" in type_accuracies and type_accuracies["assertion_reason"] < 60:
        target_qtype = "assertion_reason"
    elif "statement_based" in type_accuracies and type_accuracies["statement_based"] < 60:
        target_qtype = "statement_based"
    elif "pyq" in type_accuracies and type_accuracies["pyq"] < 65:
        target_qtype = "pyq"
    elif type_accuracies:
        target_qtype = min(type_accuracies, key=type_accuracies.get)
    else:
        # Check weakness entries for topic key hints
        weak_matches = [k for k in weakness_data.keys() if topic_clean in k.lower()]
        if any("assertion" in k for k in weak_matches):
            target_qtype = "assertion_reason"
        elif any("statement" in k for k in weak_matches):
            target_qtype = "statement_based"
        elif any("pyq" in k for k in weak_matches):
            target_qtype = "pyq"
        else:
            target_qtype = "medium"

    acc_val = round(type_accuracies.get(target_qtype, 55.0), 1)

    return {
        "level1_subject": format_subject_name(subj_clean),
        "level2_topic": format_topic_name(topic_clean),
        "level3_repository": REPOSITORY_DISPLAY_NAMES.get(target_qtype, "Medium Repository"),
        "level4_question_type": TYPE_DISPLAY_NAMES.get(target_qtype, "Medium Questions"),
        "level5_difficulty": DIFFICULTY_MAP.get(target_qtype, "Medium"),
        "raw_subject": subj_clean,
        "raw_topic": topic_clean,
        "raw_qtype": target_qtype,
        "accuracy": acc_val,
        "estimated_time_mins": 12,
    }


def get_intelligent_revision_plan(user: str = None, context: Optional[Any] = None) -> Dict[str, Any]:
    """
    Returns today's 5-level intelligent revision target recommendation.
    Reuses existing Revision Overview, Weakness, and Progress data.
    """
    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    overview = get_revision_overview(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)

    due_today = overview.get("due_today", [])
    overdue = overview.get("overdue", [])

    candidates = overdue + due_today

    if candidates:
        top_candidate = candidates[0]
        target = _analyze_5_level_target(
            top_candidate.get("subject", "polity"),
            top_candidate.get("topic", "general"),
            progress_rows,
            weakness_data,
        )
        target["status"] = "Overdue" if top_candidate in overdue else "Due Today"
        target["spacing_level"] = top_candidate.get("level", 1)
        return target

    # Fallback to weakness if no spaced revisions due
    if weakness_data:
        top_weak_key = max(weakness_data, key=weakness_data.get)
        if "-" in top_weak_key:
            subj, top = top_weak_key.split("-", 1)
        else:
            subj, top = "polity", top_weak_key
        target = _analyze_5_level_target(subj, top, progress_rows, weakness_data)
        target["status"] = "Weakness Focus"
        target["spacing_level"] = 1
        return target

    # Default fallback
    target = _analyze_5_level_target("polity", "fundamental_rights", progress_rows, weakness_data)
    target["status"] = "Recommended Focus"
    target["spacing_level"] = 1
    return target


def get_revision_analytics_v2(user: str = None, context: Optional[Any] = None) -> Dict[str, Any]:
    """
    Returns comprehensive 5-level analytics for Smart Revision Dashboard:
    - Overdue items
    - Due today items
    - Upcoming breakdown (Tomorrow, Next 3 Days, Future)
    - Revision Progress (Completed, Remaining, Percentage)
    - Weakest Revision Areas (down to Question Type)
    - Recently Revised History
    """
    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    overview = get_revision_overview(user, context=ctx)
    progress_rows = get_progress(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)

    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    three_days_later = today + datetime.timedelta(days=3)

    # Format overdue & due today items with 5-level targets
    overdue_formatted = []
    for item in overview.get("overdue", []):
        t = _analyze_5_level_target(item["subject"], item["topic"], progress_rows, weakness_data)
        t["next_due"] = item["next_due"]
        t["level"] = item["level"]
        overdue_formatted.append(t)

    due_today_formatted = []
    for item in overview.get("due_today", []):
        t = _analyze_5_level_target(item["subject"], item["topic"], progress_rows, weakness_data)
        t["next_due"] = item["next_due"]
        t["level"] = item["level"]
        due_today_formatted.append(t)

    # Group upcoming into Tomorrow, Next 3 Days, Future
    upcoming_grouped = {
        "tomorrow": [],
        "next_3_days": [],
        "future": [],
    }

    for item in overview.get("upcoming", []):
        t = _analyze_5_level_target(item["subject"], item["topic"], progress_rows, weakness_data)
        t["next_due"] = item["next_due"]
        t["level"] = item["level"]
        due_date = item["next_due"]

        if due_date == tomorrow:
            upcoming_grouped["tomorrow"].append(t)
        elif tomorrow < due_date <= three_days_later:
            upcoming_grouped["next_3_days"].append(t)
        else:
            upcoming_grouped["future"].append(t)

    # Calculate revision completion statistics
    total_revisions = len(overview.get("queue", []))
    due_total = len(overdue_formatted) + len(due_today_formatted)
    completed_today = max(0, total_revisions - due_total)
    remaining_today = due_total

    pct = int((completed_today / total_revisions) * 100) if total_revisions > 0 else 100

    # Weakest 5-level Revision Areas
    weakest_areas = []
    if weakness_data:
        sorted_weak = sorted(weakness_data.items(), key=lambda x: x[1], reverse=True)[:5]
        for key, w_val in sorted_weak:
            if "-" in key:
                s, tp = key.split("-", 1)
            else:
                s, tp = "polity", key
            target_info = _analyze_5_level_target(s, tp, progress_rows, weakness_data)
            target_info["weakness_score"] = w_val
            weakest_areas.append(target_info)

    # Recently Revised (last 5 progress items or queue items)
    recently_revised = []
    for r in progress_rows[-5:]:
        subj = r.get("subject", "polity")
        top = r.get("topic", "general")
        acc = r.get("accuracy", 0)
        recently_revised.append({
            "subject": format_subject_name(subj),
            "topic": format_topic_name(top),
            "accuracy": f"{acc}%",
            "date": "Recently",
        })

    return {
        "overdue": overdue_formatted,
        "due_today": due_today_formatted,
        "upcoming": upcoming_grouped,
        "progress": {
            "completed": completed_today,
            "remaining": remaining_today,
            "total": total_revisions,
            "percentage": pct,
        },
        "weakest_areas": weakest_areas,
        "recently_revised": recently_revised,
    }


def get_revision_mentor_message(user: str = None, context: Optional[Any] = None) -> str:
    """
    Returns rule-based mentor guidance template for Smart Revision Engine V2.
    No LLM used.
    """
    plan = get_intelligent_revision_plan(user, context=context)

    qtype = plan.get("level4_question_type", "Medium Questions")
    repo = plan.get("level3_repository", "Medium Repository")
    status = plan.get("status", "")

    if status == "Overdue":
        return f"⚠️ Urgent: Overdue revisions detected. Focus on {qtype} today."

    if "Statement Based" in qtype:
        return "📖 Revise only Statement Based questions today."
    elif "Assertion" in qtype:
        return "🔥 Focus on Assertion & Reason. Your Easy repository is already mastered."
    elif "Grand Test" in qtype or "PYQ" in qtype:
        return "🏆 Grand Test revision is now available."
    elif status == "Recommended Focus":
        return "⭐ You're fully caught up. Maintain consistency with a quick refresher."
    else:
        return f"📖 Focus on {qtype} in {repo} for maximum memory retention."
