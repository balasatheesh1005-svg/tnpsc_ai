import datetime
import logging

from core.session import current_user_id, current_username
from core.supabase_client import supabase

logger = logging.getLogger(__name__)

TABLE = "user_revisions"


from core.user_identity import resolve_user_id as _resolve_user_id


def _split_topic_key(topic_key):
    subject, topic = topic_key.split("-", 1)
    return subject, topic


def _join_topic_key(row):
    return f"{row['subject']}-{row['topic']}"


def add_revision(user=None, topic=""):
    """Adds or updates a revision topic entry using user_id UUID."""
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] add_revision failed: user_id IS NULL for user={user}")
        return

    display_username = current_username() or (str(user) if user and not (len(str(user)) == 36 and str(user).count("-") == 4) else "unknown")
    subject, topic_name = _split_topic_key(topic)
    next_due = datetime.date.today() + datetime.timedelta(days=1)

    existing = (
        supabase.table(TABLE)
        .select("id")
        .eq("user_id", user_id)
        .eq("subject", subject)
        .eq("topic", topic_name)
        .limit(1)
        .execute()
    )

    if existing.data and len(existing.data) > 0:
        row_id = existing.data[0]["id"]
        supabase.table(TABLE).update({
            "level": 1,
            "next_due": next_due.isoformat(),
        }).eq("id", row_id).execute()
    else:
        supabase.table(TABLE).insert({
            "user_id": user_id,
            "username": display_username,
            "subject": subject,
            "topic": topic_name,
            "level": 1,
            "next_due": next_due.isoformat(),
        }).execute()


def add_revision_topic(user=None, subject="", topic="", priority="high"):
    """Add a revision queue entry for a user/topic if not already pending."""
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] add_revision_topic failed: user_id IS NULL for user={user}")
        return

    normalized_topic = topic.lower().replace(" ", "_")
    existing = (
        supabase.table(TABLE)
        .select("id")
        .eq("user_id", user_id)
        .eq("subject", subject)
        .eq("topic", normalized_topic)
        .limit(1)
        .execute()
    )

    if existing.data:
        return

    add_revision(user_id, f"{subject}-{normalized_topic}")


def update_revision(user=None, topic_key=""):
    """Updates spacing level and next due date for a topic using user_id UUID."""
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] update_revision failed: user_id IS NULL for user={user}")
        return

    subject, topic = _split_topic_key(topic_key)

    response = (
        supabase.table(TABLE)
        .select("*")
        .eq("user_id", user_id)
        .eq("subject", subject)
        .eq("topic", topic)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if not rows:
        return

    row = rows[0]
    if row.get("user_id") is None:
        logger.warning(f"[DATA INTEGRITY ALERT] Revision record id={row.get('id')} has user_id IS NULL!")

    level = min(int(row.get("level") or 1) + 1, 5)

    days_map = {
        1: 1,
        2: 3,
        3: 7,
        4: 15,
        5: 30,
    }

    next_due = datetime.date.today() + datetime.timedelta(days=days_map[level])

    supabase.table(TABLE).update(
        {
            "level": level,
            "next_due": next_due.isoformat(),
        }
    ).eq("id", row["id"]).execute()


def get_due_revisions(user=None, context=None):
    """Retrieves list of due revision topic keys and due dates for user_id UUID or pre-fetched context."""
    if context is not None and hasattr(context, "revision_overview") and context.revision_overview:
        due_topics = []
        for item in context.revision_overview.get("overdue", []) + context.revision_overview.get("due_today", []):
            key = f"{item.get('subject')}-{item.get('topic')}"
            due_topics.append((key, item.get("next_due")))
        return due_topics

    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] get_due_revisions failed: user_id IS NULL for user={user}")
        return []

    today = datetime.date.today().isoformat()

    try:
        response = (
            supabase.table(TABLE)
            .select("*")
            .eq("user_id", user_id)
            .execute()
        )
        rows = response.data or []
    except Exception as e:
        logger.warning(f"get_due_revisions query error: {e}")
        rows = []

    due_topics = []
    for row in rows:
        due_val = row.get("next_revision") or row.get("next_due")
        if due_val and str(due_val) <= today:
            due_topics.append((_join_topic_key(row), due_val))

    return due_topics


def _parse_due_date(value):
    if value is None:
        return None
    if isinstance(value, datetime.date):
        return value
    try:
        return datetime.date.fromisoformat(str(value))
    except ValueError:
        try:
            return datetime.datetime.fromisoformat(str(value)).date()
        except Exception:
            return None


def get_revision_topics(user=None, context=None):
    """Retrieves list of due revision topic keys for user_id UUID or pre-fetched context."""
    due = get_due_revisions(user, context=context)
    return [t[0] for t in due]


def get_revision_overview(user=None, context=None):
    """Retrieves overview dict of revisions grouped by status for user_id UUID or pre-fetched context."""
    if context is not None and hasattr(context, "revision_overview") and context.revision_overview:
        return context.revision_overview

    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] get_revision_overview failed: user_id IS NULL for user={user}")
        return {
            "total": 0,
            "overdue": [],
            "due_today": [],
            "upcoming": [],
            "queue": [],
        }

    today = datetime.date.today()
    try:
        response = (
            supabase.table(TABLE)
            .select("*")
            .eq("user_id", user_id)
            .execute()
        )
        rows = response.data or []
    except Exception as e:
        logger.warning(f"get_revision_overview query error: {e}")
        rows = []

    overview = {
        "total": 0,
        "overdue": [],
        "due_today": [],
        "upcoming": [],
        "queue": [],
    }

    for row in rows:
        due_val = row.get("next_revision") or row.get("next_due")
        due_date = _parse_due_date(due_val)
        if due_date is None:
            continue

        level_val = int(row.get("interval") or row.get("level") or 1)
        item = {
            "subject": row.get("subject") or "Unknown",
            "topic": row.get("topic") or "Unknown",
            "level": level_val,
            "next_due": due_date,
            "next_revision": due_date,
        }

        overview["queue"].append(item)

        if due_date < today:
            overview["overdue"].append(item)
        elif due_date == today:
            overview["due_today"].append(item)
        else:
            overview["upcoming"].append(item)

    overview["total"] = len(overview["queue"])
    return overview

