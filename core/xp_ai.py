"""XP + Level System for TNPSC Nova AI"""

import logging
from core.session import current_user_id, current_username
from core.supabase_client import supabase

logger = logging.getLogger(__name__)

TABLE = "user_xp"

# Level progression: Level X = threshold XP
LEVEL_THRESHOLDS = {
    1: 0,
    2: 100,
    3: 250,
    4: 500,
    5: 1000,
    6: 2000,
    7: 3500,
    8: 5000,
    9: 7500,
    10: 10000,
}

# XP Rewards mapping
XP_REWARDS = {
    "correct_answer": 10,
    "daily_test_completion": 50,
    "accuracy_100_bonus": 50,
    "revision_completion": 20,
    "streak_7_day": 100,
}


from core.user_identity import resolve_user_id as _resolve_user_id


def get_level_from_xp(xp):
    """
    Calculate level from total XP.

    Args:
        xp: Total XP amount

    Returns:
        Current level (1-10+)
    """
    level = 1
    for lv in sorted(LEVEL_THRESHOLDS.keys(), reverse=True):
        if xp >= LEVEL_THRESHOLDS[lv]:
            level = lv
            break
    return level


def _ensure_user_xp_record(user_id, username=None):
    """Create XP record if user doesn't exist, primary-keying on user_id."""
    if not user_id:
        logger.warning("_ensure_user_xp_record called with null user_id")
        return

    response = (
        supabase.table(TABLE)
        .select("id, user_id, username, xp, level")
        .eq("user_id", user_id)
        .execute()
    )
    rows = response.data or []

    # Backward compatibility / Data Integrity check: check for records with NULL user_id
    for row in rows:
        if row.get("user_id") is None:
            logger.warning(
                f"[DATA INTEGRITY ALERT] Record ID {row.get('id')} in user_xp has NULL user_id for user_id='{user_id}'"
            )

    if not rows:
        display_name = username or current_username() or ""
        insert_payload = {
            "user_id": user_id,
            "username": display_name,
            "xp": 0,
            "level": 1,
        }
        supabase.table(TABLE).insert(insert_payload).execute()


def get_user_xp(user_id=None):
    """
    Get current XP and level for user using user_id UUID.

    Args:
        user_id: UUID user identifier or legacy identifier (optional, defaults to current_user_id())

    Returns:
        dict: {"xp": int, "level": int}
    """
    resolved_id = _resolve_user_id(user_id)
    if not resolved_id:
        logger.warning("get_user_xp called without valid user_id")
        return {"xp": 0, "level": 1}

    display_name = current_username() if resolved_id == current_user_id() else None
    _ensure_user_xp_record(resolved_id, username=display_name)

    response = (
        supabase.table(TABLE)
        .select("xp, level, user_id")
        .eq("user_id", resolved_id)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if not rows:
        return {"xp": 0, "level": 1}

    row = rows[0]
    if row.get("user_id") is None:
        logger.warning(
            f"[DATA INTEGRITY ALERT] Found user_xp row with NULL user_id for resolved_id='{resolved_id}'"
        )

    return {
        "xp": int(row.get("xp", 0)),
        "level": int(row.get("level", 1)),
    }


def add_xp(user_id=None, amount=0, reward_type=None):
    """
    Add XP to user account using user_id UUID. Updates level if threshold reached.

    Args:
        user_id: UUID user identifier or legacy identifier (optional, defaults to current_user_id())
        amount: XP amount to add
        reward_type: Type of reward (for analytics, optional)

    Returns:
        dict: {
            "new_xp": int,
            "new_level": int,
            "level_up": bool,
            "old_level": int
        }
    """
    resolved_id = _resolve_user_id(user_id)
    if not resolved_id:
        logger.warning("add_xp called without valid user_id")
        return {
            "new_xp": 0,
            "new_level": 1,
            "level_up": False,
            "old_level": 1,
        }

    display_name = current_username() if resolved_id == current_user_id() else None
    _ensure_user_xp_record(resolved_id, username=display_name)

    # Get current data using user_id
    current = get_user_xp(resolved_id)
    old_xp = current["xp"]
    old_level = current["level"]

    # Calculate new XP and level
    new_xp = old_xp + amount
    new_level = get_level_from_xp(new_xp)
    level_up = new_level > old_level

    # Update database strictly using user_id UUID
    supabase.table(TABLE).update(
        {
            "xp": new_xp,
            "level": new_level,
        }
    ).eq("user_id", resolved_id).execute()

    return {
        "new_xp": new_xp,
        "new_level": new_level,
        "level_up": level_up,
        "old_level": old_level,
    }


def get_level(user_id=None):
    """Get current level by user_id UUID."""
    current = get_user_xp(user_id)
    return current["level"]


def get_next_level_target(user_id=None):
    """
    Get XP needed to reach next level by user_id UUID.

    Returns:
        int: XP threshold for next level (0 if at max)
    """
    current = get_user_xp(user_id)
    current_level = current["level"]

    # Check if at max level
    max_level = max(LEVEL_THRESHOLDS.keys())
    if current_level >= max_level:
        return 0

    next_level = current_level + 1
    return LEVEL_THRESHOLDS[next_level]


def get_level_progress(user_id=None):
    """
    Get progress towards next level by user_id UUID.

    Returns:
        dict: {
            "current_xp": int,
            "current_level": int,
            "next_level": int,
            "next_level_target": int,
            "xp_for_next": int,
            "progress_percent": float (0-100)
        }
    """
    current = get_user_xp(user_id)
    current_xp = current["xp"]
    current_level = current["level"]

    max_level = max(LEVEL_THRESHOLDS.keys())
    if current_level >= max_level:
        return {
            "current_xp": current_xp,
            "current_level": current_level,
            "next_level": current_level,
            "next_level_target": current_xp,
            "xp_for_next": 0,
            "progress_percent": 100.0,
        }

    next_level = current_level + 1
    current_level_threshold = LEVEL_THRESHOLDS[current_level]
    next_level_threshold = LEVEL_THRESHOLDS[next_level]

    xp_in_level = current_xp - current_level_threshold
    xp_needed_for_level = next_level_threshold - current_level_threshold

    progress_percent = (
        (xp_in_level / xp_needed_for_level) * 100.0 if xp_needed_for_level > 0 else 0
    )

    return {
        "current_xp": current_xp,
        "current_level": current_level,
        "next_level": next_level,
        "next_level_target": next_level_threshold,
        "xp_for_next": max(0, next_level_threshold - current_xp),
        "progress_percent": min(100.0, progress_percent),
    }


def is_achievement_unlocked(user_id=None, achievement_type=None):
    """
    Check if achievement is unlocked (level-based) by user_id UUID.

    Args:
        user_id: User UUID identifier (optional, defaults to current_user_id())
        achievement_type: "level_2", "level_5", "level_10"

    Returns:
        bool: True if achievement is unlocked
    """
    current_level = get_level(user_id)

    achievement_levels = {
        "level_2": 2,
        "level_5": 5,
        "level_10": 10,
    }

    required_level = achievement_levels.get(achievement_type, 0)
    return current_level >= required_level
