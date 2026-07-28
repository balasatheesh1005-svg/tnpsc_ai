import datetime
import logging

from core.session import current_user_id, current_username
from core.supabase_client import supabase
from core.xp_ai import add_xp

logger = logging.getLogger(__name__)

TABLE = "daily_missions"
DAILY_MISSION_REWARD_XP = 100


from core.user_identity import resolve_user_id as _resolve_user_id


def _today():
    return datetime.date.today().isoformat()


def _mission_defaults(user_id, display_username, mission_date):
    return {
        "user_id": user_id,
        "username": display_username,
        "mission_date": mission_date,
        "daily_test_completed": False,
        "revision_count": 0,
        "questions_answered": 0,
        "reward_claimed": False,
    }


def get_today_mission(user=None):
    """Get or create today's mission row for a user using user_id UUID."""
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] get_today_mission failed: user_id IS NULL for user={user}")
        return _mission_defaults(None, "unknown", _today())

    display_username = current_username() or (str(user) if user and not (len(str(user)) == 36 and str(user).count("-") == 4) else "unknown")
    mission_date = _today()

    response = (
        supabase.table(TABLE)
        .select("*")
        .eq("user_id", user_id)
        .eq("mission_date", mission_date)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if rows:
        if rows[0].get("user_id") is None:
            logger.warning(f"[DATA INTEGRITY ALERT] Daily mission record id={rows[0].get('id')} has user_id IS NULL!")
        return rows[0]

    defaults = _mission_defaults(user_id, display_username, mission_date)
    supabase.table(TABLE).insert(defaults).execute()

    response = (
        supabase.table(TABLE)
        .select("*")
        .eq("user_id", user_id)
        .eq("mission_date", mission_date)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if rows:
        if rows[0].get("user_id") is None:
            logger.warning(f"[DATA INTEGRITY ALERT] Daily mission record id={rows[0].get('id')} has user_id IS NULL!")
        return rows[0]

    return defaults


def update_daily_test(user=None):
    """Mark today's daily test mission as complete."""
    mission = get_today_mission(user)
    if not mission or not mission.get("id"):
        return

    supabase.table(TABLE).update({"daily_test_completed": True}).eq(
        "id", mission["id"]
    ).execute()


def _increment_today_field(user=None, field_name=""):
    mission = get_today_mission(user)
    if not mission or not mission.get("id"):
        return
    current_value = int(mission.get(field_name) or 0)

    supabase.table(TABLE).update({field_name: current_value + 1}).eq(
        "id", mission["id"]
    ).execute()


def update_revision(user=None):
    """Increment today's completed revision count."""
    _increment_today_field(user, "revision_count")


def update_question_count(user=None):
    """Increment today's answered question count."""
    _increment_today_field(user, "questions_answered")


def get_mission_progress(user=None):
    """Return today's daily mission progress."""
    mission = get_today_mission(user)

    daily_test_completed = bool(mission.get("daily_test_completed"))
    revision_count = int(mission.get("revision_count") or 0)
    questions_answered = int(mission.get("questions_answered") or 0)
    reward_claimed = bool(mission.get("reward_claimed"))

    completed_count = 0
    if daily_test_completed:
        completed_count += 1
    if revision_count >= 2:
        completed_count += 1
    if questions_answered >= 20:
        completed_count += 1

    return {
        "daily_test_completed": daily_test_completed,
        "revision_count": revision_count,
        "questions_answered": questions_answered,
        "reward_claimed": reward_claimed,
        "completed_count": completed_count,
    }


def mission_completed(user=None):
    """Return True only when all three daily missions are complete."""
    progress = get_mission_progress(user)
    return progress["completed_count"] == 3


def claim_reward(user=None):
    """Claim the daily mission reward once all missions are complete."""
    user_id = _resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] claim_reward failed: user_id IS NULL for user={user}")
        return False

    mission = get_today_mission(user_id)

    if not mission or not mission.get("id"):
        return False

    if bool(mission.get("reward_claimed")):
        return False

    if not mission_completed(user_id):
        return False

    response = (
        supabase.table(TABLE)
        .update({"reward_claimed": True})
        .eq("id", mission["id"])
        .eq("reward_claimed", False)
        .execute()
    )

    if not response.data:
        return False

    add_xp(user_id, DAILY_MISSION_REWARD_XP, reward_type="daily_mission_completion")

    return True
