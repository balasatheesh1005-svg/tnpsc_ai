import streamlit as st

from core.difficulty_ai import get_next_level


def evaluate_answer(selected, options, q, user, subject, topic):
    correct = q["answer"]
    selected_letter = ["a", "b", "c", "d"][options.index(selected)]

    processed = not st.session_state.answered
    is_correct = selected_letter == correct

    if processed:

        if is_correct:

            st.success("✅ Correct")
            st.session_state.score += 1

            st.session_state.correct_streak += 1
            st.session_state.wrong_count = 0

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

        st.info(f"🎯 Next Difficulty: {st.session_state.level.upper()}")

    st.session_state.answered = True

    return {
        "processed": processed,
        "is_correct": is_correct,
        "selected_letter": selected_letter,
        "correct": correct,
    }
