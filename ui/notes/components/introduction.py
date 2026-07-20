import streamlit as st
from ui.notes.layout import section_anchor


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
        if en or ta:
            tab1, tab2 = st.tabs(["🇬🇧 English", "🇮🇳 தமிழ்"])
            with tab1:
                st.write(en if en else "")
            with tab2:
                st.write(ta if ta else "")
    elif isinstance(intro_data, list):
        for item in intro_data:
            if isinstance(item, dict):
                title = item.get("title", "Overview")
                st.subheader(f"📌 {title}")
                points = item.get("points", {})
                if isinstance(points, dict):
                    tab1, tab2 = st.tabs(["EN", "TA"])
                    with tab1:
                        for p in points.get("en", []):
                            st.write(f"• {p}")
                    with tab2:
                        for p in points.get("ta", []):
                            st.write(f"• {p}")
            elif isinstance(item, str):
                st.write(f"• {item}")
    elif isinstance(intro_data, str):
        st.write(intro_data)

    st.markdown("</div>", unsafe_allow_html=True)
