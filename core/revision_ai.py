import datetime

from core.supabase_client import supabase


TABLE = "user_revisions"


def _split_topic_key(topic_key):
    subject, topic = topic_key.split("-", 1)
    return subject, topic


def _join_topic_key(row):
    return f"{row['subject']}-{row['topic']}"


def add_revision(user, topic):
    subject, topic_name = _split_topic_key(topic)
    next_due = datetime.date.today() + datetime.timedelta(days=1)

    supabase.table(TABLE).upsert(
        {
            "username": user,
            "subject": subject,
            "topic": topic_name,
            "level": 1,
            "next_due": next_due.isoformat(),
        },
        on_conflict="username,subject,topic",
    ).execute()


def update_revision(user, topic_key):
    subject, topic = _split_topic_key(topic_key)

    response = (
        supabase.table(TABLE)
        .select("*")
        .eq("username", user)
        .eq("subject", subject)
        .eq("topic", topic)
        .limit(1)
        .execute()
    )
    rows = response.data or []

    if not rows:
        return

    row = rows[0]
    level = min(int(row.get("level") or 1) + 1, 5)

    days_map = {
        1: 1,
        2: 3,
        3: 7,
        4: 15,
        5: 30,
    }

    next_due = datetime.date.today() + datetime.timedelta(days=days_map[level])

    supabase.table(TABLE).update(
        {
            "level": level,
            "next_due": next_due.isoformat(),
        }
    ).eq("id", row["id"]).execute()


def get_due_revisions(user):
    today = datetime.date.today().isoformat()

    response = (
        supabase.table(TABLE)
        .select("subject,topic,next_due")
        .eq("username", user)
        .lte("next_due", today)
        .order("next_due")
        .execute()
    )

    due_topics = []

    for row in response.data or []:
        due_topics.append((_join_topic_key(row), row["next_due"]))

    return due_topics


def get_revision_topics(user):
    today = datetime.date.today().isoformat()

    response = (
        supabase.table(TABLE)
        .select("subject,topic")
        .eq("username", user)
        .lte("next_due", today)
        .order("next_due")
        .execute()
    )

    return [_join_topic_key(row) for row in response.data or []]
