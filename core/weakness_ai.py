import logging
from core.session import current_user_id, current_username
from core.supabase_client import supabase

logger = logging.getLogger(__name__)


from core.user_identity import resolve_user_id as _resolve_user_id


# ==========================================
# ADD WEAKNESS
# ==========================================


def add_weakness(username=None, subject="", topic=""):
    """
    Increments weakness score for a subject/topic using user_id UUID.
    """
    user_id = _resolve_user_id(username)
    if not user_id:
        logger.error("[DATA INTEGRITY ALERT] add_weakness failed: user_id IS NULL.")
        return

    existing = (
        supabase.table("users_weakness")
        .select("*")
        .eq("user_id", user_id)
        .eq("subject", subject)
        .eq("topic", topic)
        .execute()
    )

    data = existing.data

    # ✅ already exists
    if data:
        row_id = data[0]["id"]
        weakness = data[0]["weakness"] + 1

        if data[0].get("user_id") is None:
            logger.error(f"[DATA INTEGRITY ALERT] Weakness record id={row_id} has user_id IS NULL!")

        supabase.table("users_weakness").update({"weakness": weakness}).eq(
            "id", row_id
        ).execute()

    # ✅ new row
    else:
        # Determine display username for audit/logging column only
        display_username = ""
        if isinstance(username, str) and not (len(username) == 36 and username.count("-") == 4):
            display_username = username
        else:
            display_username = current_username() or ""

        supabase.table("users_weakness").insert(
            {
                "user_id": user_id,
                "username": display_username,  # Audit column only
                "subject": subject,
                "topic": topic,
                "weakness": 1,
            }
        ).execute()


# ==========================================
# REDUCE WEAKNESS
# ==========================================


def reduce_weakness(username=None, subject="", topic=""):
    """
    Decrements weakness score for a subject/topic using user_id UUID.
    """
    user_id = _resolve_user_id(username)
    if not user_id:
        logger.error("[DATA INTEGRITY ALERT] reduce_weakness failed: user_id IS NULL.")
        return

    existing = (
        supabase.table("users_weakness")
        .select("*")
        .eq("user_id", user_id)
        .eq("subject", subject)
        .eq("topic", topic)
        .execute()
    )

    data = existing.data

    if not data:
        return

    row_id = data[0]["id"]
    if data[0].get("user_id") is None:
        logger.error(f"[DATA INTEGRITY ALERT] Weakness record id={row_id} has user_id IS NULL!")

    current = data[0]["weakness"]
    new_value = max(current - 1, 0)

    supabase.table("users_weakness").update({"weakness": new_value}).eq(
        "id", row_id
    ).execute()


# ==========================================
# GET WEAKNESS
# ==========================================


def get_weakness(username=None, context=None):
    """
    Retrieves all weakness records matching user_id UUID or pre-fetched context.
    """
    if context is not None and hasattr(context, "weakness") and context.weakness is not None:
        return context.weakness

    user_id = _resolve_user_id(username)
    if not user_id:
        logger.error("[DATA INTEGRITY ALERT] get_weakness failed: user_id IS NULL.")
        return {}

    response = (
        supabase.table("users_weakness").select("*").eq("user_id", user_id).execute()
    )

    rows = response.data or []
    result = {}

    for row in rows:
        if row.get("user_id") is None:
            logger.error(
                f"[DATA INTEGRITY ALERT] Weakness record id={row.get('id')} has user_id IS NULL!"
            )
        key = f"{row['subject']}-{row['topic']}"
        result[key] = row["weakness"]

    return result


# ==========================================
# MOST WEAK TOPIC
# ==========================================


def get_most_weak_topic(username=None, context=None):
    """
    Returns the most weak topic tuple (topic_key, weakness_count) for the user.
    """
    weak_data = get_weakness(username, context=context)

    if not weak_data:
        return ("polity-fundamental_rights", 0)

    most_weak_key = max(weak_data, key=weak_data.get)
    return (most_weak_key, weak_data[most_weak_key])
