import html
import streamlit as st
from core.navigation_v2.navigation_state import (
    check_repository_availability,
    get_available_topics,
    get_selected_subject,
    set_global_topic,
)


def render_topic_selector():
    subject = get_selected_subject()
    subj_title = subject.title()

    c_hdr, c_btn = st.columns([3, 1], gap="small")
    with c_hdr:
        st.markdown(
            f"""
            <div>
                <span style="font-size: 0.8rem; font-weight: 800; color: #2563EB; text-transform: uppercase;">Subject: {html.escape(subj_title)}</span>
                <h2 style="margin: 2px 0 10px 0; color: #0F172A;">📖 Select Topic</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c_btn:
        if st.button("⬅️ Change Subject", key="btn_change_subject_from_topic"):
            st.session_state["selected_subject"] = None
            st.session_state["nav_view"] = "subject_select"
            st.rerun()

    topics_meta = get_available_topics(subject)
    
    search_q = st.text_input("🔍 Search Topic:", placeholder="Type to filter topics...", key="topic_search_filter")
    if search_q.strip():
        q_lower = search_q.strip().lower()
        topics_meta = [
            t for t in topics_meta 
            if q_lower in t["display_title"].lower() or q_lower in t["topic_id"].lower()
        ]

    if not topics_meta:
        st.warning(f"No topics found for subject '{subj_title}'.")
        return

    cols = st.columns(2, gap="medium")
    for idx, meta in enumerate(topics_meta):
        col = cols[idx % 2]
        topic_id = meta["topic_id"]
        display_title = meta["display_title"]
        avail = check_repository_availability(subject, topic_id)
        
        has_notes = avail.get("notes", False)
        has_gt = avail.get("grand_test", False)
        qs_count = sum(1 for k in ["easy", "medium", "hard", "statement_based", "assertion_reason", "match_the_following", "chronology"] if avail.get(k))

        part_badge = f'<span class="progress-pill" style="background:#F1F5F9; color:#475569;">Part {meta.get("part", 1)} of {meta.get("total_parts", 1)}</span>' if meta.get("total_parts", 1) > 1 else ""

        with col:
            card_html = f"""
            <div class="sidebar-welcome" style="margin-bottom: 12px; border-top: 4px solid #2563EB;">
                <h3 style="margin: 0 0 6px 0; color: #0F172A; font-size: 1.05rem;">{html.escape(display_title)}</h3>
                <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px;">
                    {part_badge}
                    {'<span class="progress-pill" style="background:#EFF6FF; color:#2563EB;">📖 Notes Ready</span>' if has_notes else '<span class="progress-pill">📖 Notes Pending</span>'}
                    {'<span class="progress-pill" style="background:#FEF3C7; color:#D97706;">🏆 Grand Test Ready</span>' if has_gt else ''}
                    <span class="progress-pill">{qs_count} Practice Repos</span>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            if st.button(f"Enter Topic Hub 🚀", key=f"select_top_{idx}_{topic_id[:12]}", type="primary", use_container_width=True):
                set_global_topic(subject, topic_id)
                st.session_state["nav_view"] = "topic_hub"
                st.rerun()
