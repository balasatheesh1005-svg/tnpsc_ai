import streamlit as st
from ui.notes.layout import bilingual_panels, localized_section_title, section_anchor


def render_revision(revision_data):
    """
    Renders Component 11: Quick Revision Summary Card
    Theme Accent: Green (#16A34A)
    """
    if not revision_data:
        return

    section_anchor("sec_revision")
    st.markdown('<div class="nova-card nova-revision-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown(f"### ⚡ **{localized_section_title('Quick Revision Bullet Summary')}**")

    if isinstance(revision_data, dict):
        en = revision_data.get("en", [])
        ta = revision_data.get("ta", [])
        en_values = en if isinstance(en, list) else [en]
        ta_values = ta if isinstance(ta, list) else [ta]
        for language, panel in bilingual_panels(
            en_values,
            ta_values,
            "🇬🇧 English Summary",
            "🇮🇳 தமிழ் சுருக்கம்",
        ):
            with panel:
                for point in en_values if language == "en" else ta_values:
                    st.markdown(f"✅ **{point}**")
    elif isinstance(revision_data, list):
        for pt in revision_data:
            st.markdown(f"✅ **{pt}**")

    st.markdown("</div>", unsafe_allow_html=True)
