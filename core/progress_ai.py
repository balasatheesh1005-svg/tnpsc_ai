from core.supabase_client import supabase

# ====================================
# SAVE PROGRESS
# ====================================


def save_progress(user, subject, topic, accuracy):

    data = {"username": user, "subject": subject, "topic": topic, "accuracy": accuracy}

    response = supabase.table("users_progress").insert(data).execute()
    return response.data


# ====================================
# GET USER PROGRESS
# ====================================


def get_progress(user):

    response = (
        supabase.table("users_progress").select("*").eq("username", user).execute()
    )

    return response.data
