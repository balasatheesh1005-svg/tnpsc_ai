import html
import streamlit as st

from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
    get_revision_mentor_message,
)
from ui.components.cards import (
    glass_card,
    glass_card_html,
    html_fragment,
    mentor_personality_banner,
    render_card_styles,
    revision_5level_target_card,
    revision_progress_card,
    section_title,
)
from ui.theme import render_theme_css


def render_revision_dashboard(user: str = None):
    """
    Renders Smart Revision Dashboard V2 featuring 5-Level Intelligent Revision.
    Answers: "What exactly should I revise today?"
    """
    if user is None:
        user = st.session_state.get("username", "")

    render_theme_css()
    render_card_styles()

    # Get Engine V2 Data
    plan = get_intelligent_revision_plan(user)
    analytics = get_revision_analytics_v2(user)
    mentor_msg = get_revision_mentor_message(user)

    # ---------------- MENTOR PERSONALITY BANNER ----------------
    st.html(mentor_personality_banner(mentor_msg).markup)

    # ---------------- HEADER TITLE ----------------
    section_title("Smart Revision Engine V2", "5-Level Intelligent Revision Intelligence")

    # ---------------- 1. TODAY'S REVISION PLAN ----------------
    st.markdown("### 🎯 Today's Revision Plan")
    st.html(revision_5level_target_card(plan).markup)

    # Primary CTA Button to Start Revision
    col_cta1, col_cta2 = st.columns([2, 1])
    with col_cta1:
        if st.button("🚀 Start Revision →", type="primary", use_container_width=True):
            st.session_state.update(
                {
                    "q_index": 0,
                    "score": 0,
                    "answered": False,
                    "test_active": True,
                    "test_mode": "revision",
                    "test_results_processed": False,
                    "test_subject": plan.get("raw_subject", "polity"),
                    "test_topic": plan.get("raw_topic", "general"),
                    "test_level": plan.get("raw_qtype", "easy"),
                }
            )
            st.rerun()

    st.write("")

    # ---------------- 4. REVISION PROGRESS ----------------
    prog = analytics.get("progress", {"completed": 0, "remaining": 0, "percentage": 100})
    st.html(revision_progress_card(prog["completed"], prog["remaining"], prog["percentage"]).markup)

    st.write("")

    # ---------------- 2. OVERDUE REVISION ----------------
    overdue_items = analytics.get("overdue", [])
    if overdue_items:
        section_title("⚠️ Overdue Revisions", f"{len(overdue_items)} topics require immediate review")
        for item in overdue_items:
            s = item['level1_subject']
            t = item['level2_topic']
            r = item['level3_repository']
            q = item['level4_question_type']
            acc = item['accuracy']
            due_str = item['next_due'].strftime("%b %d") if hasattr(item['next_due'], 'strftime') else str(item['next_due'])
            st.html(f"""
            <div class="nova-glass-card" style="border-left: 4px solid #EF4444; padding: 14px 18px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 850; color: #B91C1C; font-size: 0.85rem;">⏳ Overdue ({due_str})</span>
                    <span style="font-size: 0.8rem; color: #64748B;">Level {item.get('level', 1)}</span>
                </div>
                <div style="font-weight: 900; color: #0F172A; margin: 4px 0;">
                    {s} ↓ {t} ↓ {r} ↓ <span style="color: #2563EB;">{q}</span>
                </div>
                <div style="font-size: 0.82rem; color: #64748B;">Accuracy: {acc}%</div>
            </div>
            """)
    else:
        glass_card("🎉 Overdue Revision", value="Zero Overdue Items", body="All past revisions are up to date!")

    st.write("")

    # ---------------- 3. UPCOMING REVISION ----------------
    section_title("🔮 Upcoming Revision Timeline", "Scheduled spaced repetition queue")
    tab_tom, tab_3d, tab_fut = st.tabs(["🗓 Tomorrow", "📅 Next 3 Days", "🔮 Future"])

    with tab_tom:
        tom_items = analytics.get("upcoming", {}).get("tomorrow", [])
        if tom_items:
            for item in tom_items:
                st.info(f"**{item['level1_subject']} ↓ {item['level2_topic']}** ({item['level4_question_type']}) - Scheduled Tomorrow")
        else:
            st.caption("No revisions scheduled for tomorrow.")

    with tab_3d:
        d3_items = analytics.get("upcoming", {}).get("next_3_days", [])
        if d3_items:
            for item in d3_items:
                due_s = item['next_due'].strftime("%b %d") if hasattr(item['next_due'], 'strftime') else str(item['next_due'])
                st.warning(f"**{item['level1_subject']} ↓ {item['level2_topic']}** ({item['level4_question_type']}) - Due {due_s}")
        else:
            st.caption("No revisions scheduled for the next 3 days.")

    with tab_fut:
        fut_items = analytics.get("upcoming", {}).get("future", [])
        if fut_items:
            for item in fut_items[:5]:
                due_s = item['next_due'].strftime("%b %d") if hasattr(item['next_due'], 'strftime') else str(item['next_due'])
                st.write(f"🔹 **{item['level1_subject']} ↓ {item['level2_topic']}** ({item['level4_question_type']}) - Due {due_s}")
        else:
            st.caption("No long-term future revisions pending.")

    st.write("")

    # ---------------- 5. WEAKEST REVISION AREAS ----------------
    section_title("⚠️ Weakest Revision Areas", "Hierarchical sub-repository analysis")
    weak_areas = analytics.get("weakest_areas", [])
    if weak_areas:
        for area in weak_areas:
            s = area['level1_subject']
            t = area['level2_topic']
            r = area['level3_repository']
            q = area['level4_question_type']
            acc = area['accuracy']
            st.html(f"""
            <div class="nova-glass-card" style="padding: 14px 18px; margin-bottom: 10px; border-left: 4px solid #F59E0B;">
                <div style="font-weight: 900; color: #0F172A; font-size: 0.95rem;">
                    {s} ↓ {t} ↓ {r} ↓ <span style="color: #D97706;">{q}</span>
                </div>
                <div style="color: #64748B; font-size: 0.85rem; font-weight: 750; margin-top: 4px;">
                    🎯 Accuracy: <strong style="color: #DC2626;">{acc}%</strong>
                </div>
            </div>
            """)
    else:
        st.info("No major weakness area detected yet. Complete practice tests to populate analytics.")

    st.write("")

    # ---------------- 6. RECENTLY REVISED ----------------
    section_title("🕒 Recently Revised", "Last 5 completed revision sessions")
    recent = analytics.get("recently_revised", [])
    if recent:
        for item in recent:
            st.caption(f"✅ **{item['subject']} - {item['topic']}** | Score: {item['accuracy']} ({item['date']})")
    else:
        st.caption("No revision history recorded yet.")
