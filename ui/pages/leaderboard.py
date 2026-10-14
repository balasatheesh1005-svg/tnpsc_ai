import streamlit as st

from core.leaderboard_ai import get_top_users
from core.session import current_user_id, current_username
from core.user_identity import get_safe_public_identity


def render_leaderboard(section, user=None):
    section("🏆 Leaderboard")

    leaders = get_top_users()

    if not leaders:
        st.info("No users on the leaderboard yet. Complete a test to appear here.")
        st.stop()

    curr_user = current_username()
    safe_curr_user = get_safe_public_identity(curr_user, seed=current_user_id()) if curr_user else None

    for i, item in enumerate(leaders, 1):

        try:
            u, s = item
            # Final UI privacy guard ensures zero raw emails or tokens can render
            safe_u = get_safe_public_identity(u)
            score_val = int(s)

            if safe_curr_user and (safe_u == safe_curr_user or u == curr_user):
                st.markdown(f"**{i}. {safe_u} (You) → {score_val}%**")
            else:
                st.write(f"{i}. {safe_u} → {score_val}%")

        except Exception:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                safe_name = get_safe_public_identity(item[0])
                st.write(f"{i}. {safe_name} → {item[1]}")
            else:
                st.write(f"{i}. Learner")
