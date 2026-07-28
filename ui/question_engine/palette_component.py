import streamlit as st
from core.question_engine.session import set_session_value, reset_answer


def render_question_palette(
    prefix: str,
    total_questions: int,
    current_index: int,
    answered_map: dict = None,
    bookmarked_set: set = None,
):
    st.markdown("### 🗂️ Question Palette")
    
    answered_map = answered_map or {}
    bookmarked_set = bookmarked_set or set()

    cols_per_row = 10
    total_rows = (total_questions + cols_per_row - 1) // cols_per_row

    for r in range(total_rows):
        cols = st.columns(cols_per_row, gap="small")
        for c in range(cols_per_row):
            q_idx = r * cols_per_row + c
            if q_idx >= total_questions:
                break

            q_num = q_idx + 1
            is_curr = (q_idx == current_index)
            is_ans = q_idx in answered_map
            is_correct = answered_map.get(q_idx)

            # Button styling label
            label = f"{q_num}"
            if is_curr:
                label = f"[{q_num}]"
            
            btn_type = "secondary"
            if is_curr:
                btn_type = "primary"

            with cols[c]:
                if st.button(label, key=f"{prefix}_pal_{q_idx}", type=btn_type, use_container_width=True):
                    set_session_value(st.session_state, prefix, "index", q_idx)
                    reset_answer(st.session_state, prefix)
                    st.rerun()
