import streamlit as st

from core.daily_mission_ai import update_question_count
from core.difficulty_ai import get_next_level
from core.xp_ai import add_xp


def evaluate_answer(selected, options, q, user, subject, topic):
    correct = q.get("answer")
    if selected not in options or correct is None:
        st.warning("Something went wrong. Please try again.")
        return {
            "processed": False,
            "is_correct": False,
            "selected_letter": None,
            "correct": correct,
        }

    selected_letter = ["a", "b", "c", "d"][options.index(selected)]

    processed = not st.session_state.get("answered", False)
    is_correct = selected_letter == correct

    if processed:
        st.session_state.answered = True
        update_question_count(user)

        if is_correct:

            st.success("✅ Correct")
            st.session_state.score += 1

            st.session_state.correct_streak += 1
            st.session_state.wrong_count = 0

            # 🔥 Award XP for correct answer
            xp_result = add_xp(user, 10, reward_type="correct_answer")
            if xp_result.get("level_up"):
                st.session_state["xp_level_up"] = True
            st.session_state["xp_level"] = xp_result.get("new_level", 1)

        else:
            st.error(f"❌ Correct Answer: {correct}")

            st.session_state.wrong_count += 1
            st.session_state.correct_streak = 0

        # 🔥 adaptive difficulty
        st.session_state.level = get_next_level(
            st.session_state.level,
            st.session_state.correct_streak,
            st.session_state.wrong_count,
        )

    st.session_state.answered = True

    return {
        "processed": processed,
        "is_correct": is_correct,
        "selected_letter": selected_letter,
        "correct": correct,
    }
