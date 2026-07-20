import streamlit as st
from ui.notes.layout import section_anchor


def render_trap_points(trap_data):
    """
    Renders Component 12: TNPSC Trap Points High Visibility Warning Card
    Theme Accent: Red (#DC2626)
    """
    if not trap_data:
        return

    section_anchor("sec_trap_points")
    st.markdown('<div class="nova-card nova-trap-card animate-fade-in">', unsafe_allow_html=True)
    st.markdown("### ⚠️ **TNPSC Trap Points — Common Student Mistakes**")

    if isinstance(trap_data, list):
        for item in trap_data:
            if isinstance(item, dict):
                title = item.get("title", "Caution Area")
                st.subheader(f"🛑 {title}")
                points = item.get("points", {})
                if isinstance(points, dict):
                    tab1, tab2 = st.tabs(["🇬🇧 English Warning", "🇮🇳 தமிழ் எச்சரிக்கை"])
                    with tab1:
                        for p in points.get("en", []):
                            st.markdown(f"⚠️ {p}")
                    with tab2:
                        for p in points.get("ta", []):
                            st.markdown(f"⚠️ {p}")
            elif isinstance(item, str):
                st.markdown(f"⚠️ **{item}**")
    elif isinstance(trap_data, dict):
        en = trap_data.get("en", [])
        ta = trap_data.get("ta", [])
        tab1, tab2 = st.tabs(["🇬🇧 English Warning", "🇮🇳 தமிழ் எச்சரிக்கை"])
        with tab1:
            for p in en if isinstance(en, list) else [en]:
                st.markdown(f"⚠️ {p}")
        with tab2:
            for p in ta if isinstance(ta, list) else [ta]:
                st.markdown(f"⚠️ {p}")

    st.markdown("</div>", unsafe_allow_html=True)
