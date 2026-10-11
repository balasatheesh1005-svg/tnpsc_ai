import streamlit as st
from ui.notes.layout import bilingual_panels, localized_section_title, section_anchor


def render_fact_box(facts_data):
    """
    Renders Component 9: Amber Fact Box Card
    Theme Accent: Amber (#D97706), Rounded, Shadow, Icon
    """
    if not facts_data:
        return

    section_anchor("sec_fact_box")
    st.markdown('<div class="nova-card nova-fact-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown(f"### 💡 **{localized_section_title('Important Fact Box')}**")

    if isinstance(facts_data, dict):
        en = facts_data.get("en", [])
        ta = facts_data.get("ta", [])

        for language, panel in bilingual_panels(
            en,
            ta,
            "🇬🇧 English Facts",
            "🇮🇳 தமிழ் குறிப்புகள்",
        ):
            with panel:
                for fact in en if language == "en" else ta:
                    st.markdown(f"⭐ **{fact}**")
    elif isinstance(facts_data, list):
        for fact in facts_data:
            st.markdown(f"⭐ **{fact}**")

    st.markdown("</div>", unsafe_allow_html=True)
