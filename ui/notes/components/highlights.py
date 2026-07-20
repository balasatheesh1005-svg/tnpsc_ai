import streamlit as st
from ui.notes.layout import section_anchor


def render_highlights(topic_name):
    """
    Renders Component 20c: Key Text Highlights & Storage Card
    """
    section_anchor("sec_highlights")
    hl_key = f"highlights_{topic_name}"
    highlights_list = st.session_state.get(hl_key, [])

    if highlights_list:
        st.markdown('<div class="nova-card animate-fade-in" style="background-color: #FEF08A; border-left: 5px solid #A16207;">', unsafe_allow_html=True)
        st.markdown("### 🖍️ **Key Highlighted Quotes & Definitions**")
        for hl in highlights_list:
            st.markdown(f'<mark style="background-color:#FDE047; padding:0.2rem 0.5rem; border-radius:4px;">{hl}</mark>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
