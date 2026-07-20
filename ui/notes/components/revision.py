import streamlit as st
from ui.notes.layout import section_anchor


def render_revision(revision_data):
    """
    Renders Component 11: Quick Revision Summary Card
    Theme Accent: Green (#16A34A)
    """
    if not revision_data:
        return

    section_anchor("sec_revision")
    st.markdown('<div class="nova-card nova-revision-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown("### ⚡ **Quick Revision Bullet Summary**")

    if isinstance(revision_data, dict):
        en = revision_data.get("en", [])
        ta = revision_data.get("ta", [])
        if en or ta:
            tab1, tab2 = st.tabs(["🇬🇧 English Summary", "🇮🇳 தமிழ் சுருக்கம்"])
            with tab1:
                for pt in en if isinstance(en, list) else [en]:
                    st.markdown(f"✅ **{pt}**")
            with tab2:
                for pt in ta if isinstance(ta, list) else [ta]:
                    st.markdown(f"✅ **{pt}**")
    elif isinstance(revision_data, list):
        for pt in revision_data:
            st.markdown(f"✅ **{pt}**")

    st.markdown("</div>", unsafe_allow_html=True)
