from core.supabase_client import supabase

TABLE = "users_progress"


# =========================
# GET TOP USERS
# =========================


def get_top_users():
    import streamlit as st
    cache_key = "leaderboard_top_users_cache"
    if hasattr(st, "session_state") and cache_key in st.session_state:
        return st.session_state[cache_key]

    try:
        response = supabase.rpc("get_global_leaderboard").execute()
        rows = getattr(response, "data", None) or []
    except Exception as e:
        import logging
        logging.getLogger(__name__).warning(f"Leaderboard RPC get_global_leaderboard failed: {e}")
        rows = []

    leaderboard = []

    for row in rows or []:
        if not isinstance(row, dict):
            continue

        username = row.get("username")

        if not username:
            continue

        try:
            accuracy = float(row.get("accuracy", 0))
        except (TypeError, ValueError):
            continue

        leaderboard.append((username, round(accuracy, 2)))

    leaderboard.sort(key=lambda x: x[1], reverse=True)
    top_10 = leaderboard[:10]
    if hasattr(st, "session_state"):
        st.session_state[cache_key] = top_10

    return top_10

