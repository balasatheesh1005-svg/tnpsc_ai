import datetime

from core.supabase_client import supabase
from core.xp_ai import add_xp

TABLE = "daily_missions"
DAILY_MISSION_REWARD_XP = 100


def _today():
    return datetime.date.today().isoformat()


def _mission_defaults(username, mission_date):
    return {
        "username": username,
        "mission_date": mission_date,
        "daily_test_completed": False,
        "revision_count": 0,
        "questions_answered": 0,
        "reward_claimed": False,
    }


def get_today_mission(username):
    """Get or create today's mission row for a user."""
    mission_date = _today()

    response = (
        supabase.table(TABLE)
        .select("*")
        .eq("username", username)
        .eq("mission_date", mission_date)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if rows:
        return rows[0]

    supabase.table(TABLE).upsert(
        _mission_defaults(username, mission_date),
        on_conflict="username,mission_date",
    ).execute()

    response = (
        supabase.table(TABLE)
        .select("*")
        .eq("username", username)
        .eq("mission_date", mission_date)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if rows:
        return rows[0]

    return _mission_defaults(username, mission_date)


def update_daily_test(username):
    """Mark today's daily test mission as complete."""
    mission = get_today_mission(username)

    supabase.table(TABLE).update({"daily_test_completed": True}).eq(
        "id", mission["id"]
    ).execute()


def _increment_today_field(username, field_name):
    mission = get_today_mission(username)
    current_value = int(mission.get(field_name) or 0)

    supabase.table(TABLE).update({field_name: current_value + 1}).eq(
        "id", mission["id"]
    ).execute()


def update_revision(username):
    """Increment today's completed revision count."""
    _increment_today_field(username, "revision_count")


def update_question_count(username):
    """Increment today's answered question count."""
    _increment_today_field(username, "questions_answered")


def get_mission_progress(username):
    """Return today's daily mission progress."""
    mission = get_today_mission(username)

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


def mission_completed(username):
    """Return True only when all three daily missions are complete."""
    progress = get_mission_progress(username)
    return progress["completed_count"] == 3


def claim_reward(username):
    """Claim the daily mission reward once all missions are complete."""
    mission = get_today_mission(username)

    if bool(mission.get("reward_claimed")):
        return False

    if not mission_completed(username):
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

    add_xp(username, DAILY_MISSION_REWARD_XP, reward_type="daily_mission_completion")

    return True
