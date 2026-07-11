import streamlit as st

from ui.question_engine.components import render_explanation as render_engine_explanation


def _go_to_related_note(question):
    st.session_state["pyq_related_note"] = question.get("related_note", "")
    st.session_state["navigate_to"] = "📚 Notes"
    st.rerun()


def get_pyq_explanation_actions():
    return [
        {
            "label": "Related Notes",
            "key": "related_note",
            "callback": _go_to_related_note,
        },
        {
            "label": "Practice Similar Questions",
            "key": "practice_similar",
            "disabled": True,
        },
        {
            "label": "AI Teacher",
            "key": "ai_teacher",
            "disabled": True,
        },
    ]


def render_explanation(question):
    render_engine_explanation(
        question,
        "pyq",
        actions=get_pyq_explanation_actions(),
    )
