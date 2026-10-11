import streamlit as st
from ui.notes.layout import bilingual_panels, section_anchor


def render_introduction(intro_data):
    """
    Renders Component 4: Introduction & Overview
    """
    if not intro_data:
        return

    section_anchor("sec_introduction")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #F8FAFC; border-left: 5px solid #64748B;">', unsafe_allow_html=True)
    st.markdown("### 📖 **Introduction & Historical Background**")

    if isinstance(intro_data, dict):
        en = intro_data.get("en")
        ta = intro_data.get("ta")
        for language, panel in bilingual_panels(en, ta):
            with panel:
                st.write(en if language == "en" else ta)
    elif isinstance(intro_data, list):
        for item in intro_data:
            if isinstance(item, dict):
                title = item.get("title", "Overview")
                st.subheader(f"📌 {title}")
                points = item.get("points", {})
                if isinstance(points, dict):
                    en_points = points.get("en", [])
                    ta_points = points.get("ta", [])
                    for language, panel in bilingual_panels(en_points, ta_points, "EN", "TA"):
                        with panel:
                            for point in en_points if language == "en" else ta_points:
                                st.write(f"• {point}")
            elif isinstance(item, str):
                st.write(f"• {item}")
    elif isinstance(intro_data, str):
        st.write(intro_data)

    st.markdown("</div>", unsafe_allow_html=True)
