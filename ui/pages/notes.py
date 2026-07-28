import json
import os
import re
from pathlib import Path
import streamlit as st

from core.navigation_v2.navigation_state import (
    get_selected_display_title,
    get_selected_repository_id,
    get_selected_subject,
    get_selected_topic_id,
)
from core.streamlit_ui_engine import render_notes


@st.cache_data
def load_note(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return None


def render_2_minute_revision_card(data: dict, display_title: str, subject: str):
    """Renders the 2-Minute Quick Revision Card at the bottom of Notes."""
    st.markdown("---")
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 18px 22px; border-radius: 14px; color: white; margin-bottom: 20px; border: 1px solid #334155;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <div>
                    <span class="progress-pill" style="background:#DCFCE7; color:#15803D; font-weight:800; font-size:0.8rem;">
                        ✅ Notes Completed
                    </span>
                    <h3 style="margin: 8px 0 2px 0; color: #F8FAFC; font-size: 1.35rem;">⚡ 2-Minute Quick Revision</h3>
                    <p style="color: #94A3B8; font-size: 0.85rem; margin: 0;">
                        Rapid key points summary for <b>{display_title}</b> before starting practice.
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="medium")

    # 1. Key Points
    with col1:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #2563EB; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• Key Points</h4>
            """,
            unsafe_allow_html=True,
        )
        key_pts = []
        if isinstance(data, dict):
            outcomes = data.get("learning_outcomes", {}).get("Understand", {}).get("en", [])
            if outcomes:
                key_pts.extend(outcomes[:3])
            keywords = data.get("keywords", [])
            if keywords and len(key_pts) < 3:
                key_pts.append(f"Core Focus: {', '.join(keywords[:4])}")

        if not key_pts:
            key_pts = [
                f"Master foundational concepts and constitutional framework of {display_title}.",
                "Focus on landmark timeline events, acts, and statutory definitions.",
                "Review bilingual terminology for high-frequency preliminary questions."
            ]

        for pt in key_pts[:3]:
            st.markdown(f"- {pt}")
        st.markdown("</div>", unsafe_allow_html=True)

    # 2. Important Facts
    with col2:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #16A34A; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• Important Facts</h4>
            """,
            unsafe_allow_html=True,
        )
        facts = []
        if isinstance(data, dict):
            imp_facts = data.get("important_facts", {}).get("en", [])
            if isinstance(imp_facts, list):
                facts.extend(imp_facts[:3])

        if not facts:
            facts = [
                "Direct factual questions account for ~40% of preliminary examination items.",
                "Ensure exact memory of dates, committee recommendations, and numerical limits.",
                "Cross-check Samacheer Kalvi school textbook reference statements."
            ]

        for f in facts[:3]:
            st.markdown(f"- {f}")
        st.markdown("</div>", unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="medium")

    # 3. Important Articles
    with col3:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #D97706; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• Important Articles & Provisions</h4>
            """,
            unsafe_allow_html=True,
        )
        articles = []
        if isinstance(data, dict):
            arts = data.get("important_articles", [])
            if isinstance(arts, list):
                for a in arts[:3]:
                    if isinstance(a, dict):
                        articles.append(f"Article {a.get('article', '')}: {a.get('title', {}).get('en', '')}")
                    elif isinstance(a, str):
                        articles.append(a)

        if not articles:
            articles = [
                "Verify constitutional article numbers, schedules, and parts associated with this topic.",
                "Pay attention to amendment numbers and enforcement years.",
                "Note exceptions and special provisions under specific articles."
            ]

        for art in articles[:3]:
            st.markdown(f"- {art}")
        st.markdown("</div>", unsafe_allow_html=True)

    # 4. TNPSC Traps
    with col4:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #DC2626; padding: 14px; border-radius: 10px; margin-bottom: 12px;">
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 0.98rem;">• TNPSC Traps & Common Pitfalls</h4>
            """,
            unsafe_allow_html=True,
        )
        traps = []
        if isinstance(data, dict):
            t_list = data.get("tnpsc_traps", [])
            if isinstance(t_list, list):
                traps.extend(t_list[:3])

        if not traps:
            traps = [
                "⚠️ Watch for 'NOT correct' or 'Incorrect' wording in question stems.",
                "⚠️ Beware of absolute statements containing words like 'Only', 'All', or 'Never'.",
                "⚠️ Don't confuse Governor/President appointment powers vs. removal procedures."
            ]

        for t in traps[:3]:
            st.markdown(f"- {t}")
        st.markdown("</div>", unsafe_allow_html=True)


def render_notes_page(section):
    section("📘 Topic Notes")

    subject = get_selected_subject().lower()
    topic_id = get_selected_topic_id()
    repository_id = get_selected_repository_id()
    display_title = get_selected_display_title()

    hdr_col, btn_col = st.columns([3, 1], gap="small")
    with hdr_col:
        st.markdown(
            f"""
            <div style="margin-bottom: 12px;">
                <span class="progress-pill" style="background:#EFF6FF; color:#2563EB; font-weight:800;">
                    🏛️ Subject: {subject.title()}
                </span>
                <span class="progress-pill" style="background:#F8FAFC; color:#0F172A; font-weight:800;">
                    📖 Topic: {display_title}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with btn_col:
        if st.button("Continue Learning →", key="notes_switch_topic_btn", use_container_width=True):
            st.session_state["main_menu"] = "🏠 Home"
            st.session_state["nav_view"] = "topic_hub"
            st.rerun()

    note_basename = topic_id
    if note_basename.startswith(f"{subject}_"):
        note_basename = note_basename[len(subject) + 1:]

    candidate_files = [
        f"data/notes/{subject}/{note_basename}.json",
        f"data/notes/{subject}/{note_basename.replace('part', 'part_')}.json" if "part" in note_basename and "part_" not in note_basename else f"data/notes/{subject}/{note_basename}.json",
    ]

    data = None
    loaded_path = None
    for candidate in candidate_files:
        if os.path.exists(candidate):
            data = load_note(candidate)
            if data is not None:
                loaded_path = candidate
                break

    try:
        if data is None:
            st.warning(f"📭 Notes for '{display_title}' are coming soon in the next content update.")
            st.info("💡 You can attempt practice questions or grand tests for this topic in the Study Hub.")
            return

        render_notes(data)
        st.caption(f"UI Type: {data.get('ui_type', 'unknown')}")

        # Render 2-Minute Revision Card
        render_2_minute_revision_card(data, display_title, subject)

    except Exception as e:
        st.error("❌ Error loading notes payload.")
        st.exception(e)

    st.markdown("---")
    if st.button("📝 Start Practice", type="primary", use_container_width=True, key="btn_notes_start_practice"):
        from core.question_engine.practice_session import start_practice_session
        started = start_practice_session(subject, topic_id, repository_id, display_title, "easy")
        if started:
            st.session_state["study_stage"] = "practice_easy"
            st.session_state["main_menu"] = "🏠 Home"
            st.rerun()
        else:
            st.error("No practice questions found for this topic.")

