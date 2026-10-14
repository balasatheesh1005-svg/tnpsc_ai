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

    from core.user_identity import get_safe_public_identity

    for row in rows or []:
        if not isinstance(row, dict):
            continue

        raw_username = row.get("username")
        row_seed = row.get("user_id") or raw_username

        # Sanitize legacy rows from database (in case old rows contain raw email or null)
        safe_username = get_safe_public_identity(raw_username, seed=row_seed)
        if not safe_username:
            continue

        try:
            accuracy = float(row.get("accuracy", 0))
        except (TypeError, ValueError):
            continue

        leaderboard.append((safe_username, round(accuracy, 2)))

    leaderboard.sort(key=lambda x: x[1], reverse=True)
    top_10 = leaderboard[:10]
    if hasattr(st, "session_state"):
        st.session_state[cache_key] = top_10

    return top_10

