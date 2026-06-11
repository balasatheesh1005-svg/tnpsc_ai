"""XP + Level System for TNPSC Nova AI"""

from core.supabase_client import supabase

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


def _ensure_user_xp_record(username):
    """Create XP record if user doesn't exist."""
    response = supabase.table(TABLE).select("*").eq("username", username).execute()
    rows = response.data or []

    if not rows:
        supabase.table(TABLE).insert(
            {
                "username": username,
                "xp": 0,
                "level": 1,
            }
        ).execute()


def get_user_xp(username):
    """
    Get current XP and level for user.

    Returns:
        dict: {"xp": int, "level": int}
    """
    _ensure_user_xp_record(username)

    response = (
        supabase.table(TABLE)
        .select("xp, level")
        .eq("username", username)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if not rows:
        return {"xp": 0, "level": 1}

    row = rows[0]
    return {
        "xp": int(row.get("xp", 0)),
        "level": int(row.get("level", 1)),
    }


def add_xp(username, amount, reward_type=None):
    """
    Add XP to user account. Updates level if threshold reached.

    Args:
        username: User identifier
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
    _ensure_user_xp_record(username)

    # Get current data
    current = get_user_xp(username)
    old_xp = current["xp"]
    old_level = current["level"]

    # Calculate new XP and level
    new_xp = old_xp + amount
    new_level = get_level_from_xp(new_xp)
    level_up = new_level > old_level

    # Update database
    supabase.table(TABLE).update(
        {
            "xp": new_xp,
            "level": new_level,
        }
    ).eq("username", username).execute()

    return {
        "new_xp": new_xp,
        "new_level": new_level,
        "level_up": level_up,
        "old_level": old_level,
    }


def get_level(username):
    """Get current level."""
    current = get_user_xp(username)
    return current["level"]


def get_next_level_target(username):
    """
    Get XP needed to reach next level.

    Returns:
        int: XP threshold for next level (0 if at max)
    """
    current = get_user_xp(username)
    current_level = current["level"]

    # Check if at max level
    max_level = max(LEVEL_THRESHOLDS.keys())
    if current_level >= max_level:
        return 0

    next_level = current_level + 1
    return LEVEL_THRESHOLDS[next_level]


def get_level_progress(username):
    """
    Get progress towards next level.

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
    current = get_user_xp(username)
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


def is_achievement_unlocked(username, achievement_type):
    """
    Check if achievement is unlocked (level-based).

    Args:
        achievement_type: "level_2", "level_5", "level_10"

    Returns:
        bool: True if achievement is unlocked
    """
    current_level = get_level(username)

    achievement_levels = {
        "level_2": 2,
        "level_5": 5,
        "level_10": 10,
    }

    required_level = achievement_levels.get(achievement_type, 0)
    return current_level >= required_level
