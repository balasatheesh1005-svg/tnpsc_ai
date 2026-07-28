import html
import random
import time
import streamlit as st

from core.navigation_v2.navigation_state import (
    check_repository_availability,
    clear_selected_subject,
    clear_selected_topic,
    get_selected_display_title,
    get_selected_repository_id,
    get_selected_subject,
    get_selected_topic_id,
    get_selected_topic_metadata,
)
from core.question_loader import load_questions
from core.question_engine.practice_session import start_practice_session
from ui.question_engine.practice_renderer import render_practice_workspace
from ui.components.cards import analytics_grid, glass_card_html, html_fragment


def render_practice_setup(subject: str, topic_id: str, repository_id: str, display_title: str, p_key: str = "easy"):
    if st.button("Continue Learning →", key="btn_back_to_hub_from_setup"):
        st.session_state["active_practice_setup"] = None
        st.rerun()

    questions = load_questions(repository_id, p_key)
    q_count = len(questions) if questions else 0

    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 24px; border-radius: 16px; color: white; margin-bottom: 24px; border: 1px solid #334155;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <div>
                    <span class="progress-pill" style="background:#DCFCE7; color:#15803D; font-weight:800; font-size:0.8rem;">
                        🟢 Easy Repository
                    </span>
                    <h2 style="margin: 8px 0 4px 0; color: #F8FAFC; font-size: 1.6rem;">🎯 Practice Setup</h2>
                    <p style="color: #94A3B8; font-size: 0.9rem; margin: 0;">
                        🏛️ {html.escape(subject.title())} &nbsp;|&nbsp; 📖 {html.escape(display_title)}
                    </p>
                </div>
                <div>
                    <span style="background: #1E293B; border: 1px solid #475569; padding: 8px 14px; border-radius: 20px; font-weight: 700; color: #38BDF8; font-size: 0.9rem;">
                        📦 {q_count} Questions Available
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not questions:
        st.warning("⚠️ Repository Not Available")
        return

    st.markdown("### 📋 Session Configuration")

    col_info, col_actions = st.columns([3, 2], gap="medium")

    with col_info:
        st.markdown(
            f"""
            <div class="sidebar-welcome" style="padding: 16px; border-left: 4px solid #16A34A; margin-bottom: 15px;">
                <h4 style="margin: 0 0 10px 0; color: #0F172A; font-size: 1.05rem;">🎯 Practice Overview</h4>
                <ul style="color: #475569; font-size: 0.88rem; line-height: 1.8; margin: 0; padding-left: 20px;">
                    <li><b>Difficulty Level:</b> 🟢 Easy (Basic memory & direct factual questions)</li>
                    <li><b>Language Mode:</b> Bilingual support (English & Tamil toggle available)</li>
                    <li><b>Question Format:</b> TNPSC Standard MCQs with detailed explanations & exam traps</li>
                    <li><b>Timer & Scoring:</b> Instant feedback with session XP rewards</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_actions:
        st.markdown(
            """
            <div class="sidebar-welcome" style="padding: 16px; text-align: center; border-top: 4px solid #2563EB; margin-bottom: 15px;">
                <h4 style="margin: 0 0 10px 0; color: #0F172A; font-size: 1.05rem;">🚀 Ready to Begin?</h4>
                <p style="color: #64748B; font-size: 0.82rem; margin-bottom: 16px;">
                    Click below to launch your practice session using the Universal Question Renderer.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Start Practice 🚀", key="btn_setup_start_practice", type="primary", use_container_width=True):
            started = start_practice_session(subject, topic_id, repository_id, display_title, p_key)
            if started:
                st.rerun()
            else:
                st.error("Could not load practice repository questions.")


def render_topic_hub(user: str):
    if st.session_state.get("practice_active"):
        render_practice_workspace(user)
        return

    subject = get_selected_subject()
    topic_id = get_selected_topic_id()
    repository_id = get_selected_repository_id()
    display_title = get_selected_display_title()
    meta = get_selected_topic_metadata()

    active_setup = st.session_state.get("active_practice_setup")
    if active_setup:
        render_practice_setup(subject, topic_id, repository_id, display_title, active_setup)
        return

    avail = check_repository_availability(subject, topic_id)

    # 1. TOPIC HUB HEADER & TOP ACTIONS
    col_hdr, col_actions = st.columns([3, 2], gap="small")
    with col_hdr:
        part_info = f" (Part {meta.get('part', 1)} of {meta.get('total_parts', 1)})" if meta.get("total_parts", 1) > 1 else ""
        st.markdown(
            f"""
            <div>
                <span class="progress-pill" style="background:#EFF6FF; color:#2563EB; font-weight:800;">
                    🏛️ {html.escape(subject.title())}
                </span>
                <h1 style="margin: 4px 0 0 0; color: #0F172A; font-size: 1.6rem;">{html.escape(display_title)}</h1>
                <p style="color: #64748B; font-size: 0.88rem; margin-top: 2px;">
                    Your complete learning workspace for this topic.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_actions:
        a_col1, a_col2 = st.columns(2, gap="small")
        with a_col1:
            if st.button("⬅️ Change Subject", key="hub_btn_change_subject", use_container_width=True):
                st.session_state["active_practice_setup"] = None
                clear_selected_subject()
                st.rerun()
        with a_col2:
            if st.button("🔄 Change Topic", key="hub_btn_change_topic", use_container_width=True):
                st.session_state["active_practice_setup"] = None
                clear_selected_topic()
                st.rerun()

    st.markdown("---")

    # 2. PROGRESS & MASTERY SUMMARY CARD
    completed_repos = sum(1 for k, v in avail.items() if v)
    total_repos = len(avail)
    mastery_pct = int((completed_repos / max(1, total_repos)) * 100)

    next_step = "📖 Read Topic Notes"
    if avail.get("notes") and avail.get("easy"):
        next_step = "📝 Practice Medium Questions"
    if avail.get("easy") and avail.get("medium"):
        next_step = "🏆 Attempt Grand Test"

    summary_items = [
        ("📊 Topic Mastery", f"{mastery_pct}%"),
        ("📝 Practice Modes Ready", f"{completed_repos} / {total_repos}"),
        ("🎯 Recommended Next Step", next_step),
        ("🔥 Session XP", f"{st.session_state.get('xp', 0)} XP"),
    ]

    hub_card_html = glass_card_html(
        "✨ Topic Overview",
        value=f"{mastery_pct}% Mastery",
        body=f"Subject: {subject.title()} | Topic: {display_title}",
        extra_html=html_fragment(analytics_grid(summary_items).markup),
    )
    st.html(hub_card_html)

    # 3. LEARNING MODULES GRID
    st.markdown("### 🚀 Learning Modules")

    m_col1, m_col2, m_col3 = st.columns(3, gap="medium")

    # CARD 1: READ NOTES
    with m_col1:
        st.markdown(
            f"""
            <div class="sidebar-welcome" style="border-top: 4px solid #2563EB;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <h3 style="margin:0; color:#0F172A; font-size:1.1rem;">📖 Study Notes</h3>
                    {'<span class="progress-pill" style="background:#DCFCE7; color:#15803D;">Ready</span>' if avail.get('notes') else '<span class="progress-pill">Coming Soon</span>'}
                </div>
                <p style="color:#475569; font-size:0.82rem; line-height:1.4;">Comprehensive bilingual notes, key definitions, articles, timelines & Samacheer Kalvi references.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("📖 Study Notes", key="hub_launch_notes", type="primary" if avail.get('notes') else "secondary", disabled=not avail.get('notes'), use_container_width=True):
            st.session_state["study_stage"] = "notes"
            st.session_state["main_menu"] = "📚 Notes"
            st.rerun()

    # CARD 2: GRAND TEST
    with m_col2:
        st.markdown(
            f"""
            <div class="sidebar-welcome" style="border-top: 4px solid #D97706;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <h3 style="margin:0; color:#0F172A; font-size:1.1rem;">🏆 Grand Test</h3>
                    {'<span class="progress-pill" style="background:#FEF3C7; color:#D97706;">100 Qs Elite</span>' if avail.get('grand_test') else '<span class="progress-pill">Coming Soon</span>'}
                </div>
                <p style="color:#475569; font-size:0.82rem; line-height:1.4;">Full 100-question authentic TNPSC Group I Preliminary simulator with multi-act comparative questions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Start Grand Test 🏆", key="hub_launch_gt", type="primary" if avail.get('grand_test') else "secondary", disabled=not avail.get('grand_test'), use_container_width=True):
            with st.spinner("⏳ Loading Grand Test Repository..."):
                questions = load_questions(repository_id, "grand_test")
                if questions:
                    st.session_state.update({
                        "test_subject": subject,
                        "test_topic_id": topic_id,
                        "test_repository_id": repository_id,
                        "test_topic": repository_id,
                        "test_qs": questions,
                        "q_index": 0,
                        "score": 0,
                        "answered": False,
                        "test_active": True,
                        "test_mode": "grand_test",
                        "start_time": time.time(),
                        "test_start_xp": st.session_state.get("xp", 0),
                    })
                    st.session_state["main_menu"] = "📘 Daily Test"
                    st.rerun()
                else:
                    st.error("Grand Test repository could not be loaded.")

    # CARD 3: AI TEACHER
    with m_col3:
        st.markdown(
            """
            <div class="sidebar-welcome" style="border-top: 4px solid #9333EA;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <h3 style="margin:0; color:#0F172A; font-size:1.1rem;">🤖 AI Teacher</h3>
                    <span class="progress-pill" style="background:#F3E8FF; color:#7E22CE;">Active</span>
                </div>
                <p style="color:#475569; font-size:0.82rem; line-height:1.4;">Ask any doubt, request memory tricks, or get detailed constitutional analysis for this topic.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Ask AI Teacher 🤖", key="hub_launch_ai", use_container_width=True):
            st.session_state["teacher_prompt"] = f"Explain the key concepts, landmark features, and exam tricks for '{display_title}' in {subject.title()}."
            st.session_state["main_menu"] = "🤖 AI Teacher"
            st.rerun()

    # 4. PRACTICE REPOSITORIES SELECTOR CARD
    st.markdown("### 📝 Practice Questions")
    st.markdown("<p style='color: #64748B; font-size: 0.85rem; margin-top: -8px; margin-bottom: 14px;'>Choose a practice mode for this topic.</p>", unsafe_allow_html=True)
    
    p_cols = st.columns(4, gap="small")
    
    practice_types = [
        ("Easy", "easy", "🟢", "Basic memory & direct factual questions"),
        ("Medium", "medium", "🟡", "Conceptual understanding & application"),
        ("Hard", "hard", "🔴", "Analytical & elimination logic questions"),
        ("Statement Based", "statement_based", "📋", "Multi-statement accuracy checks"),
        ("Assertion & Reason", "assertion_reason", "⚖️", "Analytical cause and effect evaluation"),
        ("Match the Following", "match_the_following", "📊", "Cross-matching tables & pairs"),
        ("Chronology", "chronology", "⏱️", "Sequential timeline order checks"),
        ("PYQ Practice", "pyq", "🏛️", "Previous Year Question repository"),
    ]

    for idx, (p_title, p_key, p_icon, p_desc) in enumerate(practice_types):
        p_col = p_cols[idx % 4]
        is_avail = avail.get(p_key, False)
        
        if p_key == "easy":
            status_html = '<span style="font-size:0.7rem; color:#15803D; font-weight:700;">● Ready</span>' if is_avail else '<span style="font-size:0.7rem; color:#DC2626; font-weight:700;">Mode Not Available</span>'
            btn_label = "📝 Start Practice"
            btn_disabled = False
        else:
            status_html = '<span style="font-size:0.7rem; color:#15803D; font-weight:700;">● Ready</span>' if is_avail else '<span style="font-size:0.7rem; color:#94A3B8;">Coming Soon</span>'
            btn_label = f"Continue → {p_title}"
            btn_disabled = not is_avail

        with p_col:
            st.markdown(
                f"""
                <div class="sidebar-welcome" style="padding: 10px; margin-bottom: 8px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:800; color:#0F172A; font-size:0.9rem;">{p_icon} {p_title}</span>
                        {status_html}
                    </div>
                    <p style="font-size:0.75rem; color:#64748B; margin: 4px 0 8px 0; min-height: 28px; line-height:1.2;">{p_desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(btn_label, key=f"hub_start_prac_{p_key}", disabled=btn_disabled, use_container_width=True):
                if p_key == "easy":
                    if is_avail:
                        st.session_state["active_practice_setup"] = "easy"
                        st.rerun()
                    else:
                        st.warning("Repository Not Available")
                else:
                    started = start_practice_session(subject, topic_id, repository_id, display_title, p_key)
                    if started:
                        st.rerun()
                    else:
                        st.warning(f"No questions loaded for {p_title}.")

    # 5. ADDITIONAL HUB TOOLKIT & FUTURE PLACEHOLDERS
    st.markdown("### 🛠️ Topic Toolkit & Future Upgrades")

    t_col1, t_col2, t_col3, t_col4 = st.columns(4, gap="small")
    
    with t_col1:
        if st.button("🧠 Smart Revision", key="hub_tool_rev", use_container_width=True):
            st.session_state["main_menu"] = "🧠 Weakness"
            st.rerun()

    with t_col2:
        if st.button("📊 Topic Analytics", key="hub_tool_analytics", use_container_width=True):
            st.session_state["main_menu"] = "📊 Progress"
            st.rerun()

    with t_col3:
        if st.button("🔍 Open PYQ Explorer", key="hub_tool_pyq", use_container_width=True):
            st.session_state["main_menu"] = "PYQ"
            st.rerun()

    with t_col4:
        if st.button("🗺️ Mind Map (Soon)", key="hub_tool_mindmap", disabled=True, use_container_width=True):
            pass

    st.markdown(
        """
        <div style="background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 14px; padding: 12px 18px; margin-top: 15px; text-align: center;">
            <span style="font-size: 0.85rem; color: #64748B; font-weight: 700;">
                🚧 Future Modules Roadmap: 🗺️ Mind Maps • 🎥 Video Lessons • 📄 One Page Notes • 🎯 Weak Area Booster
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
