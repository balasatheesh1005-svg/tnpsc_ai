import streamlit as st
from ui.notes.layout import section_anchor


def render_topic_cards(section_key, section_data):
    """
    Renders Component 7: Expandable Topic Cards with nested subtopics and media support.
    """
    if not section_data:
        return

    sec_title = section_key.replace("_", " ").title()
    section_anchor(f"sec_{section_key}")

    st.markdown(f"### 📌 **{sec_title}**")

    if isinstance(section_data, list):
        for idx, item in enumerate(section_data):
            if isinstance(item, dict):
                title = item.get("title", item.get("title_en", f"Item {idx+1}"))
                title_ta = item.get("title_ta", "")
                header_text = f"{title} ({title_ta})" if title_ta else title
                
                with st.expander(f"🔹 {header_text}", expanded=(idx == 0)):
                    points = item.get("points")
                    if isinstance(points, dict):
                        en_pts = points.get("en", [])
                        ta_pts = points.get("ta", [])
                        if en_pts or ta_pts:
                            tab1, tab2 = st.tabs(["🇬🇧 English", "🇮🇳 தமிழ்"])
                            with tab1:
                                for p in en_pts:
                                    st.markdown(f"• {p}")
                            with tab2:
                                for p in ta_pts:
                                    st.markdown(f"• {p}")
                    elif "content_en" in item or "content_ta" in item:
                        tab1, tab2 = st.tabs(["🇬🇧 English", "🇮🇳 தமிழ்"])
                        with tab1:
                            st.write(item.get("content_en", ""))
                        with tab2:
                            st.write(item.get("content_ta", ""))
                    elif "question" in item: # e.g. Aptitude Solved Example
                        st.markdown(f"**Question:** {item.get('question')}")
                        st.markdown(f"**Solution:** `{item.get('solution')}`")
                        st.success(f"**Answer:** {item.get('answer')}")

            elif isinstance(item, str):
                st.markdown(f"• {item}")
    elif isinstance(section_data, dict):
        with st.expander(f"🔹 {sec_title}", expanded=True):
            en_pts = section_data.get("en", [])
            ta_pts = section_data.get("ta", [])
            if isinstance(en_pts, list) or isinstance(ta_pts, list):
                tab1, tab2 = st.tabs(["🇬🇧 English", "🇮🇳 தமிழ்"])
                with tab1:
                    for p in en_pts if isinstance(en_pts, list) else [en_pts]:
                        st.markdown(f"• {p}")
                with tab2:
                    for p in ta_pts if isinstance(ta_pts, list) else [ta_pts]:
                        st.markdown(f"• {p}")

    st.markdown("---")
