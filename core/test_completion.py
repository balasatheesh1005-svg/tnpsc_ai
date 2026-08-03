import streamlit as st

from core.ai_coach import ai_coach
from core.mentor_memory import update_memory
from core.progress_ai import save_progress
from core.streak_ai import update_streak
from core.weakness_ai import get_weakness
from core.xp_ai import add_xp


from core.engine_cache import clear_engine_cache


def complete_test(user, subject, topic, percent):
    clear_engine_cache(user)
    weak_data = get_weakness(user)

    coach_msg = ai_coach(user, percent, 100, weak_data)

    # 🔥 store mentor message
    st.session_state.mentor_chat = [{"role": "assistant", "content": coach_msg}]

    # 🔔 notification ON
    st.session_state["mentor_notification"] = True

    update_memory(user, percent, 100, weak_data)

    streak = update_streak(user)

    st.success(f"🔥 Streak: {streak} days")

    # 🔥 Award XP for daily test completion
    total_xp_earned = 0
    xp_rewards = []

    # +50 XP for test completion
    add_xp(user, 50, reward_type="daily_test_completion")
    total_xp_earned += 50
    xp_rewards.append("+50 XP: Test Completed")

    # +50 XP for 100% accuracy bonus
    if percent == 100:
        add_xp(user, 50, reward_type="accuracy_100_bonus")
        total_xp_earned += 50
        xp_rewards.append("+50 XP: Perfect Score Bonus!")

    # +100 XP for 7-day streak
    if streak == 7:
        add_xp(user, 100, reward_type="streak_7_day")
        total_xp_earned += 100
        xp_rewards.append("+100 XP: 7-Day Streak!")

    # Show XP rewards
    if xp_rewards:
        st.info(f"⭐ XP Rewards: {' | '.join(xp_rewards)}")

    if not st.session_state.get("progress_saved", False):

        save_progress(
            user,
            subject,
            topic,
            percent,
        )

        st.session_state.progress_saved = True

        st.success("✅ Progress Saved!")
