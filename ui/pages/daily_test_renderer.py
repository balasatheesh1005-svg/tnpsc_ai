import html
import time
import streamlit as st
from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion
from ui.question_engine.body_component import render_question_body
from ui.question_engine.explanation_component import render_explanation_card


def _format_time(seconds):
    minutes = max(0, seconds) // 60
    secs = max(0, seconds) % 60
    return f"{minutes:02d}:{secs:02d}"


def render_question(q_raw):
    q: NormalizedQuestion = UniversalQuestionAdapter.normalize(q_raw)
    
    total = len(st.session_state.get("test_qs", [])) or 1
    current = st.session_state.get("q_index", 0) + 1
    elapsed = (
        int(time.time() - st.session_state.start_time)
        if st.session_state.get("start_time")
        else 0
    )
    total_time = total * 45
    remaining = max(0, total_time - elapsed)
    progress_pct = current / total

    # Language Toggle State init
    lang_key = "daily_lang_mode"
    if lang_key not in st.session_state:
        st.session_state[lang_key] = "BOTH"

    # Header Row with Language Toggle
    col_hdr, col_lang = st.columns([3, 1], gap="small")
    with col_hdr:
        st.html(
            f"""
            <div class="progress-header">
                <div class="progress-details">
                    <span class="progress-pill">⏱ Time: {_format_time(remaining)}</span>
                    <span class="progress-pill">Question {current} / {total}</span>
                    <span class="progress-pill">{html.escape(q.subject)}</span>
                    <span class="progress-pill difficulty">{html.escape(q.difficulty)}</span>
                </div>
                <div class="progress-pill">{int(progress_pct * 100)}% Complete</div>
            </div>
            """
        )
    with col_lang:
        lang_mode = st.radio(
            "Lang",
            options=["EN", "TA", "BOTH"],
            index=["EN", "TA", "BOTH"].index(st.session_state[lang_key]),
            key="daily_lang_radio",
            horizontal=True,
            label_visibility="collapsed",
        )
        if lang_mode != st.session_state[lang_key]:
            st.session_state[lang_key] = lang_mode
            st.rerun()

    st.progress(progress_pct)

    # Question Body Layout
    render_question_body(q, lang_mode=st.session_state[lang_key])

    # Options Extraction
    options_labels = []
    for opt in q.options:
        text = opt.get_display_text(st.session_state[lang_key])
        options_labels.append(f"{opt.id}. {text}")

    if not options_labels:
        options_labels = ["A. Option A", "B. Option B", "C. Option C", "D. Option D"]

    selected = st.radio(
        "Select the best answer",
        options_labels,
        key=f"daily_radio_{q.id}_{current}",
        disabled=st.session_state.get("answered", False),
    )

    return selected, options_labels


def render_explanation_next(q_raw):
    q: NormalizedQuestion = UniversalQuestionAdapter.normalize(q_raw)
    chosen = st.session_state.get("last_selected_option", "")
    
    render_explanation_card(
        q=q,
        prefix="daily",
        user_choice=chosen,
    )

    if st.button("Next ➡️", key="daily_next_exp_btn", type="primary", use_container_width=True):
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.rerun()

