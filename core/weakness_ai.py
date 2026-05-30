from core.supabase_client import supabase

# ==========================================
# ADD WEAKNESS
# ==========================================


def add_weakness(username, subject, topic):

    existing = (
        supabase.table("users_weakness")
        .select("*")
        .eq("username", username)
        .eq("subject", subject)
        .eq("topic", topic)
        .execute()
    )

    data = existing.data

    # ✅ already exists
    if data:

        weakness = data[0]["weakness"] + 1

        supabase.table("users_weakness").update({"weakness": weakness}).eq(
            "id", data[0]["id"]
        ).execute()

    # ✅ new row
    else:

        supabase.table("users_weakness").insert(
            {"username": username, "subject": subject, "topic": topic, "weakness": 1}
        ).execute()


# ==========================================
# REDUCE WEAKNESS
# ==========================================


def reduce_weakness(username, subject, topic):

    existing = (
        supabase.table("users_weakness")
        .select("*")
        .eq("username", username)
        .eq("subject", subject)
        .eq("topic", topic)
        .execute()
    )

    data = existing.data

    if not data:
        return

    current = data[0]["weakness"]

    new_value = max(current - 1, 0)

    supabase.table("users_weakness").update({"weakness": new_value}).eq(
        "id", data[0]["id"]
    ).execute()


# ==========================================
# GET WEAKNESS
# ==========================================


def get_weakness(username):

    response = (
        supabase.table("users_weakness").select("*").eq("username", username).execute()
    )

    rows = response.data

    result = {}

    for row in rows:

        key = f"{row['subject']}" f"-" f"{row['topic']}"

        result[key] = row["weakness"]

    return result


# ==========================================
# MOST WEAK TOPIC
# ==========================================


def get_most_weak_topic(username):

    weak_data = get_weakness(username)

    if not weak_data:

        return ("polity-historical_background", 0)

    weak_topic = max(weak_data, key=weak_data.get)

    count = weak_data[weak_topic]

    return weak_topic, count
