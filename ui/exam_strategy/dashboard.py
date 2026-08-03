import html
import streamlit as st

from core.exam_strategy_ai import get_exam_strategy
from ui.components.cards import (
    exam_strategy_hero_card_html,
    exam_strategy_subject_flow_html,
    exam_strategy_time_plan_html,
    exam_strategy_question_rules_html,
    exam_strategy_risk_card_html,
    exam_strategy_mentor_card_html,
    render_card_styles,
)


def render_exam_strategy_dashboard(user: str = None):
    """
    Exam Strategy Dashboard V2.
    Renders output ONLY from core.exam_strategy_ai.
    Dashboard NEVER creates execution strategies — central engine creates.
    """
    render_card_styles()

    # 1. Page Header Banner
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(37, 99, 235, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">🎯 Exam Execution Strategy Dashboard V2</h2>
                    <p style="color: #93C5FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        Single Pre-Exam Strategy Authority • Personalized Attempt Sequence & Time Management
                    </p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 8px 16px; border-radius: 999px; font-weight: 800; font-size: 0.88rem; border: 1px solid rgba(255, 255, 255, 0.2);">
                    ⚡ Execution Strategy Engine
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Fetch Master Engine Output (STRICTLY FROM ENGINE)
    from core.user_context import UserContext
    ctx = UserContext.get_or_create(user)
    strategy_data = get_exam_strategy(user=user, context=ctx)


    # 3. Section 1 - 🎯 Overall Strategy Hero Header
    st.html(exam_strategy_hero_card_html(strategy_data).markup)

    # 4. Section 2 - 📚 Subject Attempt Order Flow
    st.html(exam_strategy_subject_flow_html(strategy_data).markup)

    # 5. Section 3 - ⏱ Section-wise Time Allocation
    st.html(exam_strategy_time_plan_html(strategy_data).markup)

    # 6. Section 4, 5, 6 - 📝 Question Decision Rules, ⏭ Skip Strategy & 🔄 Review Order Grid
    st.html(exam_strategy_question_rules_html(strategy_data).markup)

    # 7. Section 7 & 8 - ⚠ Risk Awareness Callouts & 🧠 Mentor Strategy Advice
    col1, col2 = st.columns([6, 6])

    with col1:
        st.html(exam_strategy_risk_card_html(strategy_data).markup)

    with col2:
        st.html(exam_strategy_mentor_card_html(strategy_data).markup)
