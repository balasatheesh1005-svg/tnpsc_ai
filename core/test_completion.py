import streamlit as st

from core.ai_coach import ai_coach
from core.mentor_memory import update_memory
from core.progress_ai import save_progress
from core.streak_ai import update_streak
from core.weakness_ai import get_weakness


def complete_test(user, subject, topic, percent):
    weak_data = get_weakness(user)

    coach_msg = ai_coach(user, percent, 100, weak_data)

    # 🔥 store mentor message
    st.session_state.mentor_chat = [{"role": "assistant", "content": coach_msg}]

    # 🔔 notification ON
    st.session_state["mentor_notification"] = True

    update_memory(user, percent, 100, weak_data)

    streak = update_streak(user)

    st.success(f"🔥 Streak: {streak} days")

    if not st.session_state.get("progress_saved", False):

        save_progress(
            user,
            subject,
            topic,
            percent,
        )

        st.session_state.progress_saved = True

        st.success("✅ Progress Saved!")
