import logging
import uuid

from core.session import current_user_id, current_username
from core.supabase_client import supabase

logger = logging.getLogger(__name__)


def is_valid_uuid(user_identifier):
    """
    Checks if a given string is a valid UUID using uuid.UUID.
    Returns True if valid, False otherwise.
    """
    if not user_identifier:
        return False
    try:
        val_uuid = uuid.UUID(str(user_identifier).strip())
        return str(val_uuid) == str(user_identifier).strip().lower()
    except (ValueError, AttributeError, TypeError):
        return False


def resolve_user_id(user_identifier=None):
    """
    Resolves the authoritative UUID user_id for database operations.
    
    Identity resolution precedence:
    1. If user_identifier is a valid UUID string -> return UUID string.
    2. If user_identifier matches session username -> return session user_id UUID.
    3. Profile lookup fallback: query public.profiles by username to resolve UUID.
    4. Session fallback: return current session user_id UUID.
    
    Never returns a username string for database operations.
    """
    if user_identifier:
        user_str = str(user_identifier).strip()

        # 1. Valid UUID check using uuid.UUID
        try:
            val_uuid = uuid.UUID(user_str)
            return str(val_uuid)
        except (ValueError, AttributeError, TypeError):
            pass

        # 2. If user_identifier matches session username, return session user_id if available
        if user_str == current_username() and current_user_id():
            return str(current_user_id())

        # 3. Profile lookup fallback: resolve username string to UUID user_id
        try:
            res = (
                supabase.table("profiles")
                .select("id")
                .eq("username", user_str)
                .limit(1)
                .execute()
            )
            if res.data and len(res.data) > 0 and res.data[0].get("id"):
                return str(res.data[0]["id"])
        except Exception as e:
            logger.warning(f"Failed to lookup profile UUID for username '{user_str}': {e}")

    # 4. Fallback to current session user_id
    session_uid = current_user_id()
    if session_uid:
        return str(session_uid)

    logger.error(
        f"[DATA INTEGRITY ALERT] Unable to resolve user_id UUID for database operation (input: {user_identifier})"
    )
    return None
