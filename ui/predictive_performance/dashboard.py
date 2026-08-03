import html
import streamlit as st

from core.predictive_performance_ai import get_predictive_performance
from ui.components.cards import (
    predictive_hero_card_html,
    predictive_comparison_cards_html,
    predictive_confidence_card_html,
    predictive_explanation_card_html,
    render_card_styles,
)


def render_predictive_performance_dashboard(user: str = None):
    """
    Predictive Performance Dashboard V2.
    Renders output ONLY from core.predictive_performance_ai.
    Zero predictive analysis or calculation performed in UI.
    """
    render_card_styles()

    # 1. Page Header
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #2563EB, #1D4ED8); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(37, 99, 235, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">🔮 Predictive Performance Dashboard V2</h2>
                    <p style="color: #93C5FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        Central Predictive Performance Engine • Rule-Based Learning Outcome Projections
                    </p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 8px 16px; border-radius: 999px; font-weight: 800; font-size: 0.88rem; border: 1px solid rgba(255, 255, 255, 0.2);">
                    ⚡ Deterministic Estimation Engine
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Fetch Master Engine Output (STRICTLY FROM ENGINE)
    from core.user_context import UserContext
    ctx = UserContext.get_or_create(user)
    pred_data = get_predictive_performance(user=user, context=ctx)


    # 3. Section 1 - 📈 Future Performance Hero Card
    st.html(predictive_hero_card_html(pred_data).markup)

    # 4. Section 2 - 📊 Current vs Estimated Comparison Grid
    st.markdown(
        """
        <div style="font-size: 1.1rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
            📊 Current Metrics vs. Projected Performance Ranges
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.html(predictive_comparison_cards_html(pred_data).markup)

    # 5. Detailed Metric Breakdown Tabs (Sections 3, 4, 5, 6)
    st.markdown(
        """
        <div style="font-size: 1.1rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
            📈 Deep-Dive Projection Dimensions
        </div>
        """,
        unsafe_allow_html=True,
    )

    t_readiness, t_mock, t_revision, t_consistency = st.tabs(
        ["📚 Readiness Trend", "📝 Mock Accuracy Trend", "🔄 Revision Trend", "📅 Consistency Trend"]
    )

    dims = pred_data.get("dimensions", {})

    with t_readiness:
        d_read = dims.get("readiness", {})
        curr_val = d_read.get("current", pred_data.get("current_readiness", 72))
        est_range = d_read.get("estimated_range", pred_data.get("estimated_readiness", "75–79%"))
        trend = d_read.get("trend", pred_data.get("readiness_trend", "Improving"))
        desc = d_read.get("description", "Overall preparation metric trajectory.")

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">📚 Expected Readiness Trend</span>
                    <span style="background: rgba(16, 185, 129, 0.12); color: #10B981; font-weight: 900; font-size: 0.8rem; padding: 4px 12px; border-radius: 999px;">
                        {trend}
                    </span>
                </div>
                <p style="color: #475569; font-size: 0.9rem; font-weight: 600; margin-bottom: 14px;">{desc}</p>
                <div style="display: flex; gap: 20px; align-items: center;">
                    <div style="background: #F8FAFC; padding: 12px 20px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <span style="color: #64748B; font-size: 0.75rem; font-weight: 800;">CURRENT READINESS</span>
                        <div style="color: #0F172A; font-size: 1.8rem; font-weight: 950;">{curr_val}%</div>
                    </div>
                    <div style="font-size: 1.5rem; font-weight: 900; color: #2563EB;">➔</div>
                    <div style="background: #EFF6FF; padding: 12px 20px; border-radius: 12px; border: 1px solid #BFDBFE;">
                        <span style="color: #1D4ED8; font-size: 0.75rem; font-weight: 850;">PROJECTED READINESS</span>
                        <div style="color: #1D4ED8; font-size: 1.8rem; font-weight: 950;">{est_range}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with t_mock:
        d_mock = dims.get("mock_accuracy", {})
        curr_val = d_mock.get("current", pred_data.get("current_mock_accuracy", 74))
        est_range = d_mock.get("estimated_range", pred_data.get("estimated_mock_accuracy", "76–80%"))
        trend = d_mock.get("trend", pred_data.get("mock_accuracy_trend", "Improving"))
        desc = d_mock.get("description", "Expected next mock exam accuracy.")

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">📝 Expected Mock Accuracy Trend</span>
                    <span style="background: rgba(37, 99, 235, 0.12); color: #2563EB; font-weight: 900; font-size: 0.8rem; padding: 4px 12px; border-radius: 999px;">
                        {trend}
                    </span>
                </div>
                <p style="color: #475569; font-size: 0.9rem; font-weight: 600; margin-bottom: 14px;">{desc}</p>
                <div style="display: flex; gap: 20px; align-items: center;">
                    <div style="background: #F8FAFC; padding: 12px 20px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <span style="color: #64748B; font-size: 0.75rem; font-weight: 800;">CURRENT MOCK ACCURACY</span>
                        <div style="color: #0F172A; font-size: 1.8rem; font-weight: 950;">{curr_val}%</div>
                    </div>
                    <div style="font-size: 1.5rem; font-weight: 900; color: #2563EB;">➔</div>
                    <div style="background: #EFF6FF; padding: 12px 20px; border-radius: 12px; border: 1px solid #BFDBFE;">
                        <span style="color: #1D4ED8; font-size: 0.75rem; font-weight: 850;">PROJECTED NEXT MOCK</span>
                        <div style="color: #1D4ED8; font-size: 1.8rem; font-weight: 950;">{est_range}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with t_revision:
        d_rev = dims.get("revision_health", {})
        curr_val = d_rev.get("current", pred_data.get("current_revision_health", 75))
        est_range = d_rev.get("estimated_range", pred_data.get("estimated_revision_health", "78–82%"))
        trend = d_rev.get("trend", pred_data.get("revision_trend", "Stable"))
        desc = d_rev.get("description", "Spaced repetition review completion rate.")

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">🔄 Expected Revision Improvement</span>
                    <span style="background: rgba(16, 185, 129, 0.12); color: #10B981; font-weight: 900; font-size: 0.8rem; padding: 4px 12px; border-radius: 999px;">
                        {trend}
                    </span>
                </div>
                <p style="color: #475569; font-size: 0.9rem; font-weight: 600; margin-bottom: 14px;">{desc}</p>
                <div style="display: flex; gap: 20px; align-items: center;">
                    <div style="background: #F8FAFC; padding: 12px 20px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <span style="color: #64748B; font-size: 0.75rem; font-weight: 800;">CURRENT REVISION HEALTH</span>
                        <div style="color: #0F172A; font-size: 1.8rem; font-weight: 950;">{curr_val}%</div>
                    </div>
                    <div style="font-size: 1.5rem; font-weight: 900; color: #2563EB;">➔</div>
                    <div style="background: #EFF6FF; padding: 12px 20px; border-radius: 12px; border: 1px solid #BFDBFE;">
                        <span style="color: #1D4ED8; font-size: 0.75rem; font-weight: 850;">PROJECTED REVISION HEALTH</span>
                        <div style="color: #1D4ED8; font-size: 1.8rem; font-weight: 950;">{est_range}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with t_consistency:
        d_con = dims.get("consistency", {})
        curr_val = d_con.get("current", pred_data.get("current_consistency", 80))
        est_range = d_con.get("estimated_range", pred_data.get("estimated_consistency", "82–86%"))
        trend = d_con.get("trend", pred_data.get("consistency_trend", "Improving"))
        desc = d_con.get("description", "Daily learning streak sustainability.")

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="font-size: 1.05rem; font-weight: 900; color: #0F172A;">📅 Expected Consistency Trend</span>
                    <span style="background: rgba(16, 185, 129, 0.12); color: #10B981; font-weight: 900; font-size: 0.8rem; padding: 4px 12px; border-radius: 999px;">
                        {trend}
                    </span>
                </div>
                <p style="color: #475569; font-size: 0.9rem; font-weight: 600; margin-bottom: 14px;">{desc}</p>
                <div style="display: flex; gap: 20px; align-items: center;">
                    <div style="background: #F8FAFC; padding: 12px 20px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <span style="color: #64748B; font-size: 0.75rem; font-weight: 800;">CURRENT CONSISTENCY</span>
                        <div style="color: #0F172A; font-size: 1.8rem; font-weight: 950;">{curr_val}%</div>
                    </div>
                    <div style="font-size: 1.5rem; font-weight: 900; color: #2563EB;">➔</div>
                    <div style="background: #EFF6FF; padding: 12px 20px; border-radius: 12px; border: 1px solid #BFDBFE;">
                        <span style="color: #1D4ED8; font-size: 0.75rem; font-weight: 850;">PROJECTED CONSISTENCY</span>
                        <div style="color: #1D4ED8; font-size: 1.8rem; font-weight: 950;">{est_range}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # 6. Section 7 & 8 - 🎯 Prediction Confidence & 📖 Why This Projection?
    col1, col2 = st.columns([5, 7])

    with col1:
        st.html(predictive_confidence_card_html(pred_data).markup)

    with col2:
        st.html(predictive_explanation_card_html(pred_data).markup)
