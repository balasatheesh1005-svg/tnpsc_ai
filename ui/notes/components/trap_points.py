import streamlit as st
from ui.notes.layout import bilingual_panels, localized_section_title, section_anchor


def render_trap_points(trap_data):
    """
    Renders Component 12: TNPSC Trap Points High Visibility Warning Card
    Theme Accent: Red (#DC2626)
    """
    if not trap_data:
        return

    section_anchor("sec_trap_points")
    st.markdown('<div class="nova-card nova-trap-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown(f"### ⚠️ **{localized_section_title('TNPSC Trap Points — Common Student Mistakes')}**")

    if isinstance(trap_data, list):
        for item in trap_data:
            if isinstance(item, dict):
                title = item.get("title", "Caution Area")
                st.subheader(f"🛑 {title}")
                points = item.get("points", {})
                if isinstance(points, dict):
                    en_points = points.get("en", [])
                    ta_points = points.get("ta", [])
                    for language, panel in bilingual_panels(
                        en_points,
                        ta_points,
                        "🇬🇧 English Warning",
                        "🇮🇳 தமிழ் எச்சரிக்கை",
                    ):
                        with panel:
                            for point in en_points if language == "en" else ta_points:
                                st.markdown(f"⚠️ {point}")
            elif isinstance(item, str):
                st.markdown(f"⚠️ **{item}**")
    elif isinstance(trap_data, dict):
        en = trap_data.get("en", [])
        ta = trap_data.get("ta", [])
        en_values = en if isinstance(en, list) else [en]
        ta_values = ta if isinstance(ta, list) else [ta]
        for language, panel in bilingual_panels(
            en_values,
            ta_values,
            "🇬🇧 English Warning",
            "🇮🇳 தமிழ் எச்சரிக்கை",
        ):
            with panel:
                for point in en_values if language == "en" else ta_values:
                    st.markdown(f"⚠️ {point}")

    st.markdown("</div>", unsafe_allow_html=True)
