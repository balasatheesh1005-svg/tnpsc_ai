import hashlib
import logging
import re
from typing import Optional
import uuid

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


def is_safe_public_username(username: Optional[str]) -> bool:
    """
    Evaluates whether a string is safe to display as a public leaderboard identity.
    Strictly forbids emails, UUIDs, phone numbers, auth tokens, and empty/whitespace values.
    """
    if username is None:
        return False
    u = str(username).strip()
    if not u or u.lower() in ("none", "null", "undefined", "unknown"):
        return False

    # 1. Reject any email address or email-like string (contains '@')
    if "@" in u:
        return False

    # 2. Reject UUIDs (prevents auth user UUID leakage)
    if is_valid_uuid(u):
        return False

    # 3. Reject JWT tokens or long hashes / secrets
    if len(u) > 35 or u.startswith("ey") or u.startswith("sb-"):
        return False

    # 4. Reject phone numbers (10+ digits with optional separators)
    digits_only = re.sub(r"[\s\-\+\(\)]", "", u)
    if digits_only.isdigit() and len(digits_only) >= 10:
        return False

    return True


def generate_safe_learner_label(seed: Optional[str] = None) -> str:
    """
    Generates a deterministic, privacy-safe learner label (e.g. 'Learner 4821').
    Uses a one-way SHA-256 hash to ensure the original seed (email, UUID, etc.)
    can NEVER be reversed or extracted from the public label.
    """
    if not seed or not str(seed).strip():
        return "Learner"

    seed_str = str(seed).strip().lower()
    h = hashlib.sha256(seed_str.encode("utf-8")).hexdigest()
    # Map to 4-digit code between 1000 and 9999
    code = (int(h[:6], 16) % 9000) + 1000
    return f"Learner {code}"


def get_safe_public_identity(
    raw_identifier: Optional[str] = None,
    full_name: Optional[str] = None,
    seed: Optional[str] = None,
) -> str:
    """
    Determines a safe public display identity following strict privacy hierarchy:
    1. Explicit learner-chosen username, if non-empty and privacy-safe (not email/UUID/phone).
    2. Profile full_name, if available and privacy-safe.
    3. Neutral deterministic generated learner label (e.g. 'Learner 4821').

    Guarantees raw email, phone number, auth UUID, or secret tokens are NEVER exposed publicly.
    """
    # 1. Explicit username check
    if is_safe_public_username(raw_identifier):
        return str(raw_identifier).strip()

    # 2. Profile full_name check
    if is_safe_public_username(full_name):
        return str(full_name).strip()

    # 3. Deterministic safe neutral fallback
    effective_seed = seed or raw_identifier or full_name
    return generate_safe_learner_label(effective_seed)


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
    from core.session import current_user_id, current_username

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
