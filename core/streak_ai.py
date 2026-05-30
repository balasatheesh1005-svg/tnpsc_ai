from datetime import date, timedelta

from core.supabase_client import supabase

TABLE = "user_streaks"


def _parse_date(value):
    if not value:
        return None
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value))


def update_streak(user):
    today = date.today()

    response = supabase.table(TABLE).select("*").eq("username", user).execute()
    rows = response.data or []

    if not rows:
        streak = 1
        supabase.table(TABLE).insert(
            {
                "username": user,
                "last_date": today.isoformat(),
                "streak": streak,
            }
        ).execute()
        return streak

    row = rows[0]
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
    ).eq("username", user).execute()

    return streak


def get_streak(user):
    response = (
        supabase.table(TABLE).select("streak").eq("username", user).limit(1).execute()
    )
    rows = response.data or []

    if not rows:
        return 0

    return int(rows[0].get("streak") or 0)
