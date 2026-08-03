import logging

from core.session import current_user_id, current_username
from core.supabase_client import supabase

logger = logging.getLogger(__name__)

TABLE = "mentor_memory"


from core.user_identity import resolve_user_id as _resolve_user_id


def update_memory(user=None, score=0, total=0, weak_data=None):
    """Updates mentor memory record for a user using user_id UUID."""
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] update_memory failed: user_id IS NULL for user={user}")
        return

    display_username = current_username() or (str(user) if user and not (len(str(user)) == 36 and str(user).count("-") == 4) else "unknown")
    percent = int((score / total) * 100) if total else 0
    weak_topics = list(weak_data.keys())[:3] if weak_data else []

    memory_dict = {
        "last_score": percent,
        "weak_topics": weak_topics,
    }

    existing = (
        supabase.table(TABLE)
        .select("id, memory_data")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if existing.data and len(existing.data) > 0:
        row_id = existing.data[0]["id"]
        current_data = existing.data[0].get("memory_data") or {}
        if isinstance(current_data, dict):
            current_data.update(memory_dict)
        else:
            current_data = memory_dict
        supabase.table(TABLE).update({
            "memory_data": current_data,
        }).eq("id", row_id).execute()
    else:
        supabase.table(TABLE).insert({
            "user_id": user_id,
            "username": display_username,
            "memory_data": memory_dict,
        }).execute()


def get_memory(user=None, context=None):
    """Retrieves mentor memory record for a user using user_id UUID or pre-fetched context."""
    if context is not None and hasattr(context, "memory"):
        return context.memory

    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] get_memory failed: user_id IS NULL for user={user}")
        return {}

    response = (
        supabase.table(TABLE)
        .select("memory_data,user_id,id")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if not rows:
        return {}

    row = rows[0]
    if row.get("user_id") is None:
        logger.warning(f"[DATA INTEGRITY ALERT] Mentor memory record id={row.get('id')} has user_id IS NULL!")

    mem_data = row.get("memory_data") or {}
    if isinstance(mem_data, dict):
        return {
            "last_score": mem_data.get("last_score", 0),
            "weak_topics": mem_data.get("weak_topics") or [],
        }

    return {}

