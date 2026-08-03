import html
import streamlit as st

from core.adaptive_revision_ai import get_adaptive_final_revision
from ui.components.cards import (
    adaptive_revision_hero_card_html,
    adaptive_revision_priority_cards_html,
    adaptive_revision_order_timeline_html,
    adaptive_revision_cycles_card_html,
    adaptive_revision_risk_card_html,
    adaptive_revision_mentor_card_html,
    render_card_styles,
)


def render_adaptive_revision_dashboard(user: str = None):
    """
    Adaptive Revision Dashboard V2.
    Renders output ONLY from core.adaptive_revision_ai.
    Dashboard NEVER creates revision plans — central engine creates.
    """
    render_card_styles()

    # 1. Page Banner Header
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(37, 99, 235, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">⚡ Adaptive Final Revision Dashboard V2</h2>
                    <p style="color: #93C5FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        Single Personalized Revision Authority • Automated Adaptive Strategy Generation
                    </p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 8px 16px; border-radius: 999px; font-weight: 800; font-size: 0.88rem; border: 1px solid rgba(255, 255, 255, 0.2);">
                    🧠 AI Strategy Engine
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Fetch Master Engine Output (STRICTLY FROM ENGINE)
    from core.user_context import UserContext
    ctx = UserContext.get_or_create(user)
    revision_data = get_adaptive_final_revision(user=user, context=ctx)


    # 3. Section 1 - 📅 Current Revision Phase & Hero Header
    st.html(adaptive_revision_hero_card_html(revision_data).markup)

    # 4. Section 2 & 3 - 🎯 Priority Subjects & 📚 Priority Topics
    st.html(adaptive_revision_priority_cards_html(revision_data).markup)

    # 5. Section 4 - 🔄 Revision Order Timeline
    st.html(adaptive_revision_order_timeline_html(revision_data).markup)

    # 6. Section 5 - 📈 Daily Revision Target Box
    daily_target = html.escape(str(revision_data.get("daily_target", "Revise 3 topics + 40 MCQs + 1 PYQ set")))
    st.markdown(
        f"""
        <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(239, 246, 255, 0.95), rgba(219, 234, 254, 0.95)); border: 1px solid rgba(37, 99, 235, 0.3);">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
                <div>
                    <div style="font-size: 0.8rem; font-weight: 900; color: #1D4ED8; text-transform: uppercase; margin-bottom: 4px;">
                        📈 Daily Revision Target
                    </div>
                    <div style="font-size: 1.25rem; font-weight: 950; color: #0F172A;">
                        {daily_target}
                    </div>
                </div>
                <div style="background: #2563EB; color: white; padding: 8px 18px; border-radius: 999px; font-weight: 900; font-size: 0.88rem;">
                    ⚡ Active Target
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 7. Section 6 - 🔁 Structured Revision Cycles
    st.html(adaptive_revision_cycles_card_html(revision_data).markup)

    # 8. Section 7 & 8 - ⚠ Revision Risk Analysis & 🧠 Mentor Advice
    col1, col2 = st.columns([6, 6])

    with col1:
        st.html(adaptive_revision_risk_card_html(revision_data).markup)

    with col2:
        st.html(adaptive_revision_mentor_card_html(revision_data).markup)

    # 9. Section 9 - ✅ Estimated Revision Completion Meter
    est_comp = html.escape(str(revision_data.get("estimated_completion", "85% estimated revision completion in 24 days")))
    sections = revision_data.get("dashboard_sections", {})
    comp_pct = int(sections.get("completion_percentage", 85))

    st.markdown(
        f"""
        <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">
                    ✅ Estimated Revision Completion
                </div>
                <span style="background: rgba(16, 185, 129, 0.15); color: #10B981; font-weight: 950; font-size: 0.9rem; padding: 4px 14px; border-radius: 999px;">
                    {comp_pct}% Projected
                </span>
            </div>
            <div style="background: #F1F5F9; border-radius: 999px; height: 12px; overflow: hidden; margin-bottom: 10px;">
                <div style="background: linear-gradient(90deg, #2563EB, #10B981); width: {comp_pct}%; height: 100%; border-radius: 999px; transition: width 0.5s ease;"></div>
            </div>
            <div style="color: #475569; font-size: 0.88rem; font-weight: 700; text-align: center;">
                🎯 {est_comp}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
