import streamlit as st
from core.question_engine.navigator import next_index, previous_index
from core.question_engine.session import get_session_value, reset_answer, set_session_value


def render_question_footer(prefix: str, current_index: int, total_questions: int) -> bool:
    answered = get_session_value(st.session_state, prefix, "answered", False)

    # Confidence Rating (optional prior to submit)
    if not answered:
        conf_key = f"{prefix}_confidence_{current_index}"
        if conf_key not in st.session_state:
            st.session_state[conf_key] = "Medium"
            
        c_col1, c_col2 = st.columns([1, 2], gap="small")
        with c_col1:
            st.markdown("<span style='font-size:0.85rem; font-weight:600; color:#64748b;'>Confidence Level:</span>", unsafe_allow_html=True)
        with c_col2:
            conf_val = st.select_slider(
                "Select confidence",
                options=["Low", "Medium", "High"],
                value=st.session_state[conf_key],
                key=f"slider_{conf_key}",
                label_visibility="collapsed",
            )
            st.session_state[conf_key] = conf_val

    st.markdown("<br>", unsafe_allow_html=True)
    prev_col, submit_col, skip_col, next_col = st.columns(4, gap="small")

    # Previous Button
    with prev_col:
        if st.button("⬅️ Previous", key=f"{prefix}_prev_btn", use_container_width=True, disabled=(current_index == 0)):
            prev_i = previous_index(current_index, total_questions)
            set_session_value(st.session_state, prefix, "index", prev_i)
            reset_answer(st.session_state, prefix)
            st.rerun()

    # Submit Button
    submitted = False
    with submit_col:
        submitted = st.button(
            "✅ Submit",
            key=f"{prefix}_submit_btn",
            use_container_width=True,
            disabled=answered,
            type="primary",
        )

    # Skip Button
    with skip_col:
        if st.button("⏭️ Skip", key=f"{prefix}_skip_btn", use_container_width=True, disabled=answered):
            next_i = next_index(current_index, total_questions)
            set_session_value(st.session_state, prefix, "index", next_i)
            reset_answer(st.session_state, prefix)
            st.rerun()

    # Next Button
    with next_col:
        if st.button("Next ➡️", key=f"{prefix}_next_btn", use_container_width=True):
            next_i = next_index(current_index, total_questions)
            set_session_value(st.session_state, prefix, "index", next_i)
            reset_answer(st.session_state, prefix)
            st.rerun()

    return submitted
