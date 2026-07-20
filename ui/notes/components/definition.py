import streamlit as st
from ui.notes.layout import section_anchor


def render_definition(definition_data):
    """
    Renders Component 2: Bilingual Definition Card
    Theme Accent: Blue (#2563EB)
    """
    if not definition_data:
        return

    section_anchor("sec_definition")
    st.markdown('<div class="nova-card nova-definition-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown("### 📘 **Definition & Core Concept**")

    if isinstance(definition_data, dict):
        en_text = definition_data.get("en", "")
        ta_text = definition_data.get("ta", "")

        if en_text and ta_text:
            tab1, tab2 = st.tabs(["🇬🇧 English", "🇮🇳 தமிழ்"])
            with tab1:
                st.markdown(f'<p style="font-size: 1.05rem; line-height: 1.6; color: #1E293B;">{en_text}</p>', unsafe_allow_html=True)
            with tab2:
                st.markdown(f'<p style="font-size: 1.05rem; line-height: 1.6; color: #1E293B;">{ta_text}</p>', unsafe_allow_html=True)
        elif en_text:
            st.markdown(f'<p style="font-size: 1.05rem; line-height: 1.6;">{en_text}</p>', unsafe_allow_html=True)
        elif ta_text:
            st.markdown(f'<p style="font-size: 1.05rem; line-height: 1.6;">{ta_text}</p>', unsafe_allow_html=True)
    elif isinstance(definition_data, str):
        st.markdown(f'<p style="font-size: 1.05rem; line-height: 1.6;">{definition_data}</p>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
