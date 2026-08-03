import html
import streamlit as st

from core.mock_intelligence_ai import get_mock_intelligence
from ui.components.cards import (
    mock_hero_card_html,
    mock_mistakes_strengths_html,
    mock_qtype_performance_html,
    mock_time_analysis_card_html,
    render_card_styles,
)


def render_mock_intelligence_dashboard(user: str = None):
    """
    Mock Intelligence Dashboard V2.
    Renders output ONLY from core.mock_intelligence_ai.
    Zero behavioral analysis or calculations performed in UI.
    """
    render_card_styles()

    # 1. Page Header
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #3B82F6, #1D4ED8); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(37, 99, 235, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">📝 Mock Exam Intelligence Dashboard V2</h2>
                    <p style="color: #93C5FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        Central Mock Exam Behavioral Analysis Engine • Evaluating Observed Test Performance
                    </p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 8px 16px; border-radius: 999px; font-weight: 800; font-size: 0.88rem; border: 1px solid rgba(255, 255, 255, 0.2);">
                    ⚡ Deterministic Behavioral Analytics
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Fetch Master Engine Output (STRICTLY FROM ENGINE)
    from core.user_context import UserContext
    ctx = UserContext.get_or_create(user)
    mock_data = get_mock_intelligence(user=user, context=ctx)


    section_perf = mock_data.get("section_performance", [])
    qtypes = mock_data.get("question_types", [])
    mistakes = mock_data.get("mistakes", [])
    strengths = mock_data.get("strengths", [])
    summary = mock_data.get("summary", "Mock performance analyzed cleanly.")

    # 3. Section 1 - 🎯 Overall Mock Performance Hero Card
    st.html(mock_hero_card_html(mock_data).markup)

    # 4. Section 2 - ⏱️ Time Management Analysis Card
    st.html(mock_time_analysis_card_html(mock_data).markup)
    st.write("")

    # 5. Section 3 - 📚 Section Performance & 📝 Question Type Performance (Side-by-Side)
    left_col, right_col = st.columns([6, 6])

    with left_col:
        # Build Section-wise Cards
        sec_cards = ""
        for s in section_perf:
            s_name = html.escape(str(s.get("subject", "Subject")))
            acc = int(s.get("accuracy", 60))
            t_sec = int(s.get("avg_time_sec", 58))
            b_color = "#10B981" if acc >= 80 else ("#2563EB" if acc >= 65 else ("#F97316" if acc >= 50 else "#EF4444"))

            sec_cards += f"""
            <div style="background: rgba(255, 255, 255, 0.85); border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 14px; margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="color: #0F172A; font-weight: 900; font-size: 0.92rem;">{s_name}</span>
                    <div>
                        <span style="color: {b_color}; font-weight: 950; font-size: 0.95rem; margin-right: 8px;">{acc}%</span>
                        <span style="color: #64748B; font-size: 0.75rem; font-weight: 800; background: #F1F5F9; padding: 2px 8px; border-radius: 999px;">⏱ {t_sec}s/Q</span>
                    </div>
                </div>
                <div style="background: #E2E8F0; border-radius: 999px; height: 6px; overflow: hidden;">
                    <div style="background: {b_color}; width: {acc}%; height: 100%; border-radius: 999px;"></div>
                </div>
            </div>
            """

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px;">
                    📚 Section-wise Mock Accuracy & Pace
                </div>
                <div>
                    {sec_cards}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_col:
        st.html(mock_qtype_performance_html(qtypes).markup)

    st.write("")

    # 6. Section 4 - ⚠ Mistake Patterns & 💪 Observed Strengths
    st.html(mock_mistakes_strengths_html(mistakes, strengths).markup)
    st.write("")

    # 7. Section 5 - 📖 Mock Intelligence Behavioral Summary Card
    st.markdown(
        f"""
        <div class="nova-glass-card" style="padding: 22px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 10px;">
                📖 Mock Intelligence Summary & Strategy Directives
            </div>
            <div style="color: #334155; font-size: 0.95rem; font-weight: 750; line-height: 1.5; background: rgba(248, 250, 252, 0.9); padding: 14px 18px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 10px;">
                {html.escape(summary)}
            </div>
            <div style="color: #64748B; font-size: 0.8rem; font-weight: 750;">
                ℹ️ Note: Mock Exam Intelligence evaluates observed attempt behavior inside completed tests only.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
