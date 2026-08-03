import html
import streamlit as st

from core.exam_readiness_ai import get_exam_readiness
from ui.components.cards import (
    readiness_hero_card_html,
    render_card_styles,
    strengths_improvements_card_html,
    subject_readiness_grid_html,
)


def render_exam_readiness_dashboard(user: str = None):
    """
    Exam Readiness Dashboard V2.
    Renders output ONLY from core.exam_readiness_ai.
    Zero readiness calculation logic performed in UI.
    """
    render_card_styles()

    # 1. Page Title Header
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #0284C7, #2563EB); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(2, 132, 199, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">🎯 Exam Readiness Engine V2</h2>
                    <p style="color: #BAE6FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        Central Readiness Assessment Engine • Evaluating Current Preparation Levels
                    </p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 8px 16px; border-radius: 999px; font-weight: 800; font-size: 0.88rem; border: 1px solid rgba(255, 255, 255, 0.2);">
                    ⚡ Deterministic 5-Dimension Evaluation
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Fetch Master Engine Output (STRICTLY FROM ENGINE)
    from core.user_context import UserContext
    ctx = UserContext.get_or_create(user)
    readiness = get_exam_readiness(user=user, context=ctx)


    mentor_insight = readiness.get("mentor_insight", "Focus on balancing your subject readiness.")
    dimensions = readiness.get("readiness_dimensions", {})
    subjects = readiness.get("subjects", [])
    strengths = readiness.get("strengths", [])
    improvements = readiness.get("improvements", [])
    reason = readiness.get("readiness_reason", "Readiness score calculated from learning signals.")

    # 3. Section 1 - 🧠 Mentor Readiness Directives Banner
    st.markdown(
        f"""
        <div class="nova-glass-card" style="padding: 18px 22px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(240, 249, 255, 0.95), rgba(239, 246, 255, 0.95)); border: 1px solid rgba(2, 132, 199, 0.3);">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div style="font-size: 2.2rem; background: #0284C7; color: white; border-radius: 50%; width: 48px; height: 48px; display: grid; place-items: center; flex-shrink: 0; box-shadow: 0 6px 16px rgba(2, 132, 199, 0.3);">
                    🧠
                </div>
                <div>
                    <div style="color: #0369A1; font-size: 0.8rem; font-weight: 900; text-transform: uppercase; letter-spacing: 0.5px;">AI Mentor Readiness Directives</div>
                    <div style="color: #0F172A; font-size: 1.05rem; font-weight: 850; margin-top: 2px;">
                        "{html.escape(mentor_insight)}"
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 4. Section 2 - 🎯 Overall Readiness Hero Card
    st.html(readiness_hero_card_html(readiness).markup)

    # 5. Section 3 - 📊 5-Dimension Readiness Metric Cards Grid
    st.markdown("<h3 style='color: #0F172A; font-weight: 900; margin-bottom: 12px;'>📊 Readiness Dimensions Breakdown</h3>", unsafe_allow_html=True)
    d_cols = st.columns(5)

    dim_items = [
        ("📖 Topic Mastery", dimensions.get("topic_mastery", 70), "30% Weight"),
        ("📦 Repo Completion", dimensions.get("repository_completion", 65), "20% Weight"),
        ("🔄 Revision Health", dimensions.get("revision_health", 75), "20% Weight"),
        ("🔥 Consistency", dimensions.get("consistency", 80), "15% Weight"),
        ("📝 PYQ Practice", dimensions.get("pyq_readiness", 60), "15% Weight"),
    ]

    for col, (label, score_val, w_label) in zip(d_cols, dim_items):
        with col:
            color_hex = "#10B981" if score_val >= 80 else ("#2563EB" if score_val >= 65 else ("#F97316" if score_val >= 50 else "#EF4444"))
            st.markdown(
                f"""
                <div class="nova-glass-card" style="padding: 14px; text-align: center;">
                    <div style="color: #64748B; font-size: 0.75rem; font-weight: 800; text-transform: uppercase;">{label}</div>
                    <div style="color: {color_hex}; font-size: 1.6rem; font-weight: 950; margin-top: 2px;">{score_val}%</div>
                    <div style="color: #64748B; font-size: 0.72rem; font-weight: 800; margin-top: 2px;">{w_label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    # 6. Section 4 - 📚 Subject-wise Readiness & Strengths/Improvements
    left_col, right_col = st.columns([6, 6])

    with left_col:
        st.html(subject_readiness_grid_html(subjects).markup)

    with right_col:
        st.html(strengths_improvements_card_html(strengths, improvements).markup)

    st.write("")

    # 7. Section 5 - 📖 Why This Readiness Score? (Rationale Card)
    st.markdown(
        f"""
        <div class="nova-glass-card" style="padding: 22px;">
            <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                <span>📖 Why Was This Readiness Score Assigned?</span>
            </div>
            <div style="color: #334155; font-size: 0.95rem; font-weight: 750; line-height: 1.5; background: rgba(248, 250, 252, 0.9); padding: 14px 18px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 10px;">
                {html.escape(reason)}
            </div>
            <div style="color: #64748B; font-size: 0.8rem; font-weight: 750;">
                ℹ️ Note: Exam Readiness score represents current preparation level based on learning data. It is not an actual exam result prediction.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
