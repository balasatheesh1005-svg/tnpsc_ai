import streamlit as st

from core.leaderboard_ai import get_top_users


def render_leaderboard(section):
    section("🏆 Leaderboard")

    leaders = get_top_users()

    if not leaders:
        st.info("No users on the leaderboard yet. Complete a test to appear here.")
        st.stop()

    for i, item in enumerate(leaders, 1):

        try:
            u, s = item
            st.write(f"{i}. {u} → {int(s)}%")

        except:
            st.write(item)
