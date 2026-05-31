import streamlit as st


def render_question(q):
    # Progress
    st.progress((st.session_state.q_index + 1) / len(st.session_state.test_qs))

    st.subheader(f"Q{st.session_state.q_index+1}")

    st.write(q["question_en"])
    st.caption(q["question_ta"])

    options = [
        f"{q['options_en'][i]} / {q['options_ta'][i]}"
        for i in range(len(q["options_en"]))
    ]

    selected = st.radio("Choose answer", options)

    return selected, options


def render_explanation_next(q):
    st.info(q.get("explanation_en", ""))

    if st.button("Next"):
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.rerun()
