import logging
from core.session import current_user_id, current_username
from core.supabase_client import supabase
from core.topics_loader import get_topic_metadata_by_id

logger = logging.getLogger(__name__)


from core.user_identity import resolve_user_id as _resolve_user_id


def save_progress(user=None, subject="", topic="", accuracy=0, topic_id=None, repository_id=None):
    """
    Saves user progress record to public.users_progress using user_id UUID.
    """
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error("[DATA INTEGRITY ALERT] save_progress failed: user_id IS NULL.")
        return []

    subj = str(subject or "").lower().strip()
    lookup = topic_id or repository_id or topic
    meta = get_topic_metadata_by_id(subj, lookup)

    r_id = meta.get("repository_id", lookup)

    # Determine display username for audit/logging column only
    display_username = ""
    if isinstance(user, str) and not (len(user) == 36 and user.count("-") == 4):
        display_username = user
    else:
        display_username = current_username() or ""

    data = {
        "user_id": user_id,
        "username": display_username,  # Audit column only
        "subject": subj,
        "topic": r_id,
        "accuracy": accuracy,
    }

    response = supabase.table("users_progress").insert(data).execute()
    return response.data or []


def get_progress(user=None, context=None):
    """
    Retrieves user progress records from public.users_progress matching user_id UUID or pre-fetched context.
    """
    if context is not None and hasattr(context, "progress") and context.progress is not None:
        return context.progress

    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error("[DATA INTEGRITY ALERT] get_progress failed: user_id IS NULL.")
        return []

    response = (
        supabase.table("users_progress").select("*").eq("user_id", user_id).execute()
    )

    rows = response.data or []
    for row in rows:
        if row.get("user_id") is None:
            logger.error(
                f"[DATA INTEGRITY ALERT] Progress record id={row.get('id')} has user_id IS NULL!"
            )

    return rows

