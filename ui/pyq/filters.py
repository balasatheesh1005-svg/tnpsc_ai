import streamlit as st

from core.question_engine.filters import filter_questions


def apply_pyq_filters(questions, exam=None, year=None, subject=None, keyword=None):
    return filter_questions(
        questions,
        criteria={
            "exam": exam,
            "year": year,
            "subject": subject,
        },
        keyword=keyword,
    )


def render_pyq_filters(facets):
    exams = ["All Exams"] + list(facets.get("exams", []))
    years = ["All Years"] + [str(year) for year in facets.get("years", [])]
    subjects = ["All Subjects"] + list(facets.get("subjects", []))

    col_exam, col_year, col_subject = st.columns(3, gap="small")
    with col_exam:
        exam = st.selectbox("Exam", exams, key="pyq_filter_exam")
    with col_year:
        year = st.selectbox("Year", years, key="pyq_filter_year")
    with col_subject:
        subject = st.selectbox("Subject", subjects, key="pyq_filter_subject")

    keyword = st.text_input(
        "Search PYQ",
        placeholder="Search question, topic, tag, or trick",
        key="pyq_filter_keyword",
    )

    return {
        "exam": exam,
        "year": year,
        "subject": subject,
        "keyword": keyword,
    }
