from core.supabase_client import supabase


TABLE = "mentor_memory"


def update_memory(user, score, total, weak_data):
    percent = int((score / total) * 100) if total else 0
    weak_topics = list(weak_data.keys())[:3] if weak_data else []

    supabase.table(TABLE).upsert(
        {
            "username": user,
            "last_score": percent,
            "weak_topics": weak_topics,
        },
        on_conflict="username",
    ).execute()


def get_memory(user):
    response = (
        supabase.table(TABLE)
        .select("last_score,weak_topics")
        .eq("username", user)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if not rows:
        return {}

    row = rows[0]
    return {
        "last_score": row.get("last_score", 0),
        "weak_topics": row.get("weak_topics") or [],
    }
