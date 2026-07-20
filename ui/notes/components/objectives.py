import streamlit as st
from ui.notes.layout import section_anchor


def render_objectives(objectives_data):
    """
    Renders Component 3: Learning Objectives & Exam Importance
    """
    if not objectives_data:
        return

    section_anchor("sec_objectives")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #F0F9FF; border-left: 5px solid #0284C7;">', unsafe_allow_html=True)
    st.markdown("### 🎯 **Learning Objectives & Exam Importance**")

    if isinstance(objectives_data, dict):
        en = objectives_data.get("en")
        ta = objectives_data.get("ta")
        if en or ta:
            tab1, tab2 = st.tabs(["🇬🇧 English", "🇮🇳 தமிழ்"])
            with tab1:
                if isinstance(en, list):
                    for obj in en:
                        st.markdown(f"• {obj}")
                elif isinstance(en, str):
                    st.markdown(en)
            with tab2:
                if isinstance(ta, list):
                    for obj in ta:
                        st.markdown(f"• {obj}")
                elif isinstance(ta, str):
                    st.markdown(ta)
    elif isinstance(objectives_data, list):
        for obj in objectives_data:
            st.markdown(f"• {obj}")

    st.markdown("</div>", unsafe_allow_html=True)
