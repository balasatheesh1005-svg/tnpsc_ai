import html
import time

import streamlit as st
from ui.components.cards import glass_card_html


def _format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def render_question(q):
    total = len(st.session_state.test_qs) or 1
    current = st.session_state.q_index + 1
    elapsed = (
        int(time.time() - st.session_state.start_time)
        if st.session_state.get("start_time")
        else 0
    )
    total_time = total * 45
    remaining = max(0, total_time - elapsed)
    subject = st.session_state.get("test_subject", "General").title()
    difficulty = st.session_state.get("level", "easy").upper()
    progress_pct = current / total

    st.markdown(
        f"""
        <div class="progress-header">
            <div class="progress-details">
                <span class="progress-pill">⏱ Remaining Time: {_format_time(remaining)}</span>
                <span class="progress-pill">Question {current} / {total}</span>
            </div>
            <div class="progress-pill">{int(progress_pct * 100)}% Complete</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(progress_pct)

    question_html = f"""
    <section class="nova-glass-card question-card">
        <div class="question-badges">
            <span class="question-badge subject">{html.escape(subject)}</span>
            <span class="question-badge difficulty">{html.escape(difficulty)}</span>
        </div>
        <div class="question-title">{html.escape(q.get('question_en', ''))}</div>
        <p class="nova-card-copy">{html.escape(q.get('question_ta', ''))}</p>
    </section>
    """
    st.markdown(question_html, unsafe_allow_html=True)

    options = [
        f"{q['options_en'][i]} / {q['options_ta'][i]}"
        for i in range(len(q["options_en"]))
    ]

    selected = st.radio("Select the best answer", options)

    return selected, options


def render_explanation_next(q):
    explanation_html = glass_card_html(
        "✅ Correct Answer",
        body=q.get("explanation_en", "No explanation available."),
    )
    st.html(explanation_html)

    if st.button("Next", use_container_width=True):
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.rerun()
