from datetime import date, timedelta
import logging

from core.session import current_user_id, current_username
from core.supabase_client import supabase
from core.user_identity import resolve_user_id

logger = logging.getLogger(__name__)

TABLE = "user_streaks"


def _parse_date(value):
    if not value:
        return None
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def update_streak(user=None):
    """Updates user daily streak tracking using user_id UUID."""
    user_id = resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] update_streak failed: user_id IS NULL for user={user}")
        return 0

    display_username = current_username() or (str(user) if user and not (len(str(user)) == 36 and str(user).count("-") == 4) else "unknown")
    today = date.today()

    response = supabase.table(TABLE).select("*").eq("user_id", user_id).execute()
    rows = response.data or []

    if not rows:
        streak = 1
        supabase.table(TABLE).insert(
            {
                "user_id": user_id,
                "username": display_username,
                "last_date": today.isoformat(),
                "streak": streak,
            }
        ).execute()
        return streak

    row = rows[0]
    if row.get("user_id") is None:
        logger.warning(f"[DATA INTEGRITY ALERT] Streak record id={row.get('id')} has user_id IS NULL!")

    last_date = _parse_date(row.get("last_date"))
    streak = int(row.get("streak") or 0)

    if last_date == today:
        return streak

    if last_date == today - timedelta(days=1):
        streak += 1
    else:
        streak = 1

    supabase.table(TABLE).update(
        {
            "last_date": today.isoformat(),
            "streak": streak,
        }
    ).eq("id", row["id"]).execute()

    return streak


def get_streak(user=None):
    """Retrieves user current streak count using user_id UUID."""
    user_id = resolve_user_id(user)
    if not user_id:
        logger.error(f"[DATA INTEGRITY ALERT] get_streak failed: user_id IS NULL for user={user}")
        return 0

    response = (
        supabase.table(TABLE).select("streak,user_id,id").eq("user_id", user_id).limit(1).execute()
    )
    rows = response.data or []

    if not rows:
        return 0

    if rows[0].get("user_id") is None:
        logger.warning(f"[DATA INTEGRITY ALERT] Streak record id={rows[0].get('id')} has user_id IS NULL!")

    return int(rows[0].get("streak") or 0)
