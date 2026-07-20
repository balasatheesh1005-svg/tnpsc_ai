import streamlit as st
from ui.notes.layout import section_anchor


def render_related_topics(related_data):
    """
    Renders Component 15: Connected Topics & One-Click Navigation
    """
    if not related_data:
        return

    section_anchor("sec_related_topics")
    st.markdown('<div class="nova-card animate-fade-in" style="background-color: #F5F3FF; border-left: 5px solid #7C3AED;">', unsafe_allow_html=True)
    st.markdown("### 🔗 **Related Topics & Connected Chapters**")

    if isinstance(related_data, list):
        cols = st.columns(min(len(related_data), 4))
        for idx, topic in enumerate(related_data):
            col = cols[idx % len(cols)]
            with col:
                topic_name = topic.get("title", topic) if isinstance(topic, dict) else str(topic)
                if st.button(f"📖 {topic_name}", key=f"btn_rel_{idx}", use_container_width=True):
                    st.session_state["notes_topic"] = topic_name
                    st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
