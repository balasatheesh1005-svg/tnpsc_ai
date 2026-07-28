import html
import streamlit as st
from core.navigation_v2.navigation_state import get_available_subjects, get_available_topics, set_global_topic


def render_subject_selector(on_subject_selected=None):
    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 style="margin-bottom: 5px; color: #0F172A;">📚 Select Subject</h2>
            <p style="color: #64748B; font-size: 0.95rem; margin: 0;">Choose a subject to explore topics and access unified learning modules.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    subjects = get_available_subjects()
    cols = st.columns(2, gap="medium")

    for idx, subj in enumerate(subjects):
        col = cols[idx % 2]
        s_id = subj["id"]
        title = subj["title"]
        icon = subj["icon"]
        desc = subj["description"]
        
        topics_count = len(get_available_topics(s_id))

        with col:
            card_html = f"""
            <div class="sidebar-welcome" style="margin-bottom: 15px; border-left: 5px solid #2563EB;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                    <div style="font-size: 2rem;">{icon}</div>
                    <div>
                        <h3 style="margin: 0; color: #0F172A; font-size: 1.15rem;">{html.escape(title)}</h3>
                        <span style="font-size: 0.78rem; font-weight: 700; color: #2563EB; background: #EFF6FF; padding: 2px 8px; border-radius: 99px;">
                            {topics_count} Topics Available
                        </span>
                    </div>
                </div>
                <p style="color: #475569; font-size: 0.85rem; margin-bottom: 12px; line-height: 1.4;">
                    {html.escape(desc)}
                </p>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            if st.button(f"Explore {title} ➡️", key=f"select_subj_{s_id}", type="primary", use_container_width=True):
                st.session_state["selected_subject"] = s_id
                st.session_state["nav_view"] = "topic_select"
                if on_subject_selected:
                    on_subject_selected(s_id)
                st.rerun()
