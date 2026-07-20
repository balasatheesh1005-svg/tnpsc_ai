import streamlit as st


def render_bottom_actions(subject, topic):
    """
    Renders the standardized Bottom Actions Bar for TNPSC Nova AI Notes Engine.
    Actions: Practice MCQ, Revision Cards, Ask AI, Bookmark, Share
    """
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("### 🚀 **Quick Actions**")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🧠 Practice MCQ", key="btn_bottom_practice", use_container_width=True):
            st.session_state.test_subject = subject
            st.session_state.test_topic = topic
            st.session_state.notes_practice_trigger = True
            st.success("🎯 Practice session initialized!")

    with col2:
        if st.button("🎴 Flashcards", key="btn_bottom_flashcards", use_container_width=True):
            st.session_state.show_revision_cards = not st.session_state.get("show_revision_cards", False)

    with col3:
        if st.button("🤖 Ask AI Teacher", key="btn_bottom_ai", use_container_width=True):
            st.session_state.ai_teacher_active = True
            st.info("💡 AI Teacher activated. Ask any question below!")

    with col4:
        is_bookmarked = st.session_state.get(f"bookmark_{topic}", False)
        bookmark_label = "🔖 Bookmarked" if is_bookmarked else "🔖 Bookmark"
        if st.button(bookmark_label, key="btn_bottom_bookmark", use_container_width=True):
            st.session_state[f"bookmark_{topic}"] = not is_bookmarked
            st.rerun()

    with col5:
        if st.button("📤 Share Note", key="btn_bottom_share", use_container_width=True):
            st.toast(f"📋 Link copied for topic: {topic}")


def section_anchor(sec_id):
    """Helper to inject an HTML anchor target for TOC navigation."""
    st.markdown(f'<div id="{sec_id}"></div>', unsafe_allow_html=True)
