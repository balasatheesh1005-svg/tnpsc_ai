import streamlit as st
from ui.notes.layout import section_anchor


def render_user_notes(topic_name):
    """
    Renders Component 20b: Personal Notes Editor
    Allows students to write, edit, and locally store custom revision notes per topic.
    """
    section_anchor("sec_user_notes")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #FEFCE8; border-left: 5px solid #CA8A04;">', unsafe_allow_html=True)
    st.markdown("### ✏️ **My Personal Revision Notes**")

    notes_key = f"user_personal_notes_{topic_name}"
    existing_notes = st.session_state.get(notes_key, "")

    user_text = st.text_area("Write your summary notes, formulas, or mnemonic reminders here:", value=existing_notes, height=120, key=f"txt_area_{topic_name}")

    if user_text != existing_notes:
        st.session_state[notes_key] = user_text

    if user_text:
        st.toast("💾 Personal notes saved locally.")

    st.markdown("</div>", unsafe_allow_html=True)
