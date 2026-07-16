import streamlit as st

from ui.question_engine.components import render_explanation as render_engine_explanation


def get_related_note_value(question):
    if question is None:
        return ""
    
    # Try dictionary-like get or attribute lookup
    val = None
    if hasattr(question, "get"):
        val = question.get("related_note") or question.get("related_notes")
    else:
        val = getattr(question, "related_note", None) or getattr(question, "related_notes", None)
        
    if not val:
        return ""
        
    if isinstance(val, list):
        valid_items = [item for item in val if isinstance(item, str) and item.strip()]
        return valid_items[0] if valid_items else ""
        
    if isinstance(val, str):
        return val.strip()
        
    return ""


def _go_to_related_note(question):
    # Clear any previous notes error
    st.session_state.pop("pyq_notes_error", None)

    note = get_related_note_value(question)
    if note:
        st.session_state["pyq_related_note"] = note
        st.session_state["navigate_to"] = "📚 Notes"
    else:
        st.session_state["pyq_notes_error"] = "No related notes available for this question."
    
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
