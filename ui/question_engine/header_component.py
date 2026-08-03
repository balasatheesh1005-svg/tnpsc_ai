import html
import time
from typing import Optional
import streamlit as st
from ui.question_engine.parser import NormalizedQuestion


def render_question_header(
    q: NormalizedQuestion,
    current_index: int,
    total_questions: int,
    prefix: str,
    timer_seconds: Optional[int] = None,
):
    # Language mode state init (default: BOTH)
    lang_key = f"{prefix}_lang_mode"
    if lang_key not in st.session_state:
        st.session_state[lang_key] = "BOTH"

    # Bookmark state init
    bm_key = f"{prefix}_bookmarks"
    if bm_key not in st.session_state:
        st.session_state[bm_key] = set()

    is_bookmarked = (q.id in st.session_state[bm_key]) or (current_index in st.session_state[bm_key])

    # Progress calculation
    total = max(1, total_questions)
    curr = max(1, current_index + 1)
    percent = int((curr / total) * 100)

    # Timer calculation
    timer_html = ""
    if timer_seconds:
        start_key = f"{prefix}_started_at"
        if not st.session_state.get(start_key):
            st.session_state[start_key] = time.time()
        elapsed = int(time.time() - st.session_state[start_key])
        remaining = max(0, timer_seconds - elapsed)
        mins = remaining // 60
        secs = remaining % 60
        timer_html = f'<span class="progress-pill timer-pill">⏱ {mins:02d}:{secs:02d}</span>'

    # Badges HTML
    diff_class = q.difficulty.lower().replace(" ", "-")
    badges_html = f"""
    <div class="question-badges">
        <span class="question-badge subject">{html.escape(q.subject)}</span>
        <span class="question-badge topic">{html.escape(q.topic)}</span>
        <span class="question-badge difficulty {diff_class}">{html.escape(q.difficulty)}</span>
        <span class="question-badge type">{html.escape(q.question_type)}</span>
        <span class="question-badge bloom">{html.escape(q.bloom_level)}</span>
    </div>
    """

    st.html(
        f"""
        <div class="progress-header">
            <div class="progress-details">
                {timer_html}
                <span class="progress-pill">Question {curr} / {total}</span>
                <span class="progress-pill">{html.escape(q.exam)}</span>
            </div>
            <div class="progress-pill">{percent}% Complete</div>
        </div>
        """
    )
    st.progress(percent / 100.0)

    # Header controls row (Language Toggle + Bookmark + Report)
    col_badges, col_ctrls = st.columns([3, 2], gap="small")
    with col_badges:
        st.html(badges_html)
    with col_ctrls:
        c1, c2, c3 = st.columns([2, 1, 1], gap="small")
        with c1:
            lang_mode = st.radio(
                "Language Mode",
                options=["EN", "TA", "BOTH"],
                index=["EN", "TA", "BOTH"].index(st.session_state[lang_key]),
                key=f"{prefix}_lang_select_{q.id}",
                horizontal=True,
                label_visibility="collapsed",
            )
            if lang_mode != st.session_state[lang_key]:
                st.session_state[lang_key] = lang_mode
                st.rerun()
        with c2:
            bm_icon = "⭐" if is_bookmarked else "☆"
            if st.button(bm_icon, key=f"{prefix}_bm_btn_{q.id}", help="Bookmark question"):
                if is_bookmarked:
                    st.session_state[bm_key].discard(q.id)
                    st.session_state[bm_key].discard(current_index)
                else:
                    st.session_state[bm_key].add(q.id)
                    st.session_state[bm_key].add(current_index)
                st.rerun()
        with c3:
            if st.button("🚩", key=f"{prefix}_report_btn_{q.id}", help="Report issue"):
                st.toast("Question flagged for review by TNPSC Nova AI Team.", icon="🚩")
