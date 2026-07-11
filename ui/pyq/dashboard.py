import streamlit as st

from core.pyq_loader import get_pyq_facets, load_all_pyq
from core.question_engine.session import init_question_session
from core.question_engine.stats import most_repeated_topics
from ui.components.cards import (
    analytics_grid,
    glass_card,
    glass_card_html,
    html_fragment,
    render_card_styles,
    section_title,
)
from ui.pyq.filters import apply_pyq_filters, render_pyq_filters
from ui.pyq.question_card import render_question_card


def _init_pyq_state():
    init_question_session(st.session_state, "pyq")


def _format_count(value, singular, plural=None):
    label = singular if value == 1 else (plural or f"{singular}s")
    return f"{value} {label}"


def _most_repeated_topics(questions, limit=6):
    return most_repeated_topics(questions, limit=limit)


def _render_browse_cards(facets):
    exam_count = len(facets.get("exams", []))
    year_count = len(facets.get("years", []))
    subject_count = len(facets.get("subjects", []))

    col_exam, col_year, col_subject = st.columns(3, gap="small")
    with col_exam:
        glass_card("Browse by Exam", value=exam_count, body=_format_count(exam_count, "exam"))
    with col_year:
        glass_card("Browse by Year", value=year_count, body=_format_count(year_count, "year"))
    with col_subject:
        glass_card(
            "Browse by Subject",
            value=subject_count,
            body=_format_count(subject_count, "subject"),
        )


def _render_repeated_topics(questions):
    rows = _most_repeated_topics(questions)
    if not rows:
        glass_card(
            "Most Repeated Topics",
            body="Repeated-topic insights will appear after PYQ data is added.",
        )
        return

    glass_card(
        "Most Repeated Topics",
        extra_html=analytics_grid(rows),
    )


def _render_placeholders():
    col_bookmarks, col_analytics = st.columns(2, gap="small")
    with col_bookmarks:
        glass_card(
            "Bookmarks",
            value="Coming Soon",
            body="Saved PYQ questions will appear here in a later phase.",
        )
    with col_analytics:
        glass_card(
            "Analytics",
            value="Coming Soon",
            body="PYQ attempt trends will be connected in a later phase.",
        )


def render_pyq_dashboard(section):
    section("PYQ Practice")
    render_card_styles()
    _init_pyq_state()

    questions = load_all_pyq()
    facets = get_pyq_facets(questions)

    total_questions = len(questions)
    current_index = st.session_state.get("pyq_index", 0)
    resume_label = (
        f"Question {min(current_index + 1, total_questions)} of {total_questions}"
        if total_questions
        else "No PYQ data yet"
    )

    glass_card(
        "Continue Practice",
        value=resume_label,
        body="Resume your previous year question practice session.",
    )

    _render_browse_cards(facets)

    section_title("PYQ Filters", "Exam, year, subject, search")
    selected_filters = render_pyq_filters(facets)
    filtered_questions = apply_pyq_filters(questions, **selected_filters)
    filter_signature = tuple(sorted(selected_filters.items()))

    if st.session_state.get("pyq_filter_signature") != filter_signature:
        st.session_state["pyq_index"] = 0
        st.session_state["pyq_answered"] = False
        st.session_state["pyq_filter_signature"] = filter_signature

    st.html(
        glass_card_html(
            "Available Questions",
            value=len(filtered_questions),
            body="Filtered PYQ questions ready for practice.",
            extra_html=html_fragment(""),
        )
    )

    section_title("Most Repeated Topics", "PYQ frequency")
    _render_repeated_topics(questions)
    _render_placeholders()

    section_title("Practice", "Previous year questions")
    if not filtered_questions:
        st.info("No PYQ questions found. Add JSON files under data/pyq to start practice.")
        return

    index = min(st.session_state.get("pyq_index", 0), len(filtered_questions) - 1)
    st.session_state["pyq_index"] = index
    render_question_card(filtered_questions[index], index + 1, len(filtered_questions))
