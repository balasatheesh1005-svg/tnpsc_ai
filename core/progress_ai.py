from core.supabase_client import supabase
from core.session import current_user_id

# ====================================
# SAVE PROGRESS
# ====================================


def save_progress(user, subject, topic, accuracy):

    data = {"username": user, "subject": subject, "topic": topic, "accuracy": accuracy}
    user_id = current_user_id()
    if user_id:
        data["user_id"] = user_id

    response = supabase.table("users_progress").insert(data).execute()
    if getattr(response, "error", None) and "user_id" in data:
        data.pop("user_id", None)
        response = supabase.table("users_progress").insert(data).execute()
    return response.data or []


# ====================================
# GET USER PROGRESS
# ====================================


def get_progress(user):

    response = (
        supabase.table("users_progress").select("*").eq("username", user).execute()
    )

    return response.data
