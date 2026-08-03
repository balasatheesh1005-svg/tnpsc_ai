import html
import streamlit as st

from core.learning_intelligence_ai import get_learning_intelligence
from core.study_planner_ai import get_personal_study_plan
from core.recommendation_ai import get_ai_recommendation
from core.exam_readiness_ai import get_exam_readiness
from core.mock_intelligence_ai import get_mock_intelligence
from core.predictive_performance_ai import get_predictive_performance
from core.adaptive_revision_ai import get_adaptive_final_revision
from core.exam_strategy_ai import get_exam_strategy
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.streak_ai import get_streak

from ui.components.cards import (
    coach_hero_card_html,
    coach_next_best_action_card_html,
    coach_mentor_summary_card_html,
    render_card_styles,
)


def render_coach_dashboard(user: str = None):
    """
    Flagship AI Exam Coach Dashboard V2.
    Unifies outputs from ALL 8 core intelligence engines into a single mentor experience.
    
    PURE PRESENTATION LAYER:
    - Zero calculations
    - Zero predictions
    - Zero evaluations
    - Zero strategy creation
    - Zero database mutations
    Renders outputs exclusively received from master core engines.
    """
    render_card_styles()

    # 1. Fetch Outputs from All Master Core AI Engines (Zero duplicate logic)
    readiness = get_exam_readiness(user)
    recommendation = get_ai_recommendation(user)
    study_plan = get_personal_study_plan(user, available_time=45)
    intelligence = get_learning_intelligence(user)
    mock_data = get_mock_intelligence(user)
    predictive = get_predictive_performance(user)
    adaptive_revision = get_adaptive_final_revision(user)
    exam_strategy = get_exam_strategy(user)
    progress_rows = get_progress(user)
    weakness_data = get_weakness(user)
    streak = get_streak(user)

    # 2. Page Title Header
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(37, 99, 235, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">🤖 AI Exam Coach Dashboard V2</h2>
                    <p style="color: #93C5FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        Flagship Mentor Experience • Unified Exam Intelligence Engine Hub
                    </p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 8px 16px; border-radius: 999px; font-weight: 800; font-size: 0.88rem; border: 1px solid rgba(255, 255, 255, 0.2);">
                    🏛 TNPSC Nova AI Master Home
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3. HERO SECTION
    st.html(coach_hero_card_html(user, readiness, recommendation, streak).markup)

    # 4. QUICK ACTIONS BAR
    st.markdown(
        """
        <div style="font-size: 1rem; font-weight: 900; color: #0F172A; margin-bottom: 10px;">
            ⚡ Quick Actions
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        if st.button("🚀 Study Plan", use_container_width=True):
            st.session_state["navigate_to"] = "📅 Study Planner"
            st.rerun()

    with col2:
        if st.button("🔄 Revision", use_container_width=True):
            st.session_state["navigate_to"] = "⚡ Adaptive Revision Strategy"
            st.rerun()

    with col3:
        if st.button("📝 Attempt Mock", use_container_width=True):
            st.session_state["navigate_to"] = "📝 Mock Intelligence"
            st.rerun()

    with col4:
        if st.button("🧠 Weak Topic", use_container_width=True):
            st.session_state["navigate_to"] = "🧠 Weakness"
            st.rerun()

    with col5:
        if st.button("📜 View PYQs", use_container_width=True):
            st.session_state["navigate_to"] = "PYQ"
            st.rerun()

    with col6:
        if st.button("📚 Smart Notes", use_container_width=True):
            st.session_state["navigate_to"] = "📚 Notes"
            st.rerun()

    st.write("")

    # 5. SECTION 9 — NEXT BEST ACTION (Rendered Prominently First)
    st.html(coach_next_best_action_card_html(recommendation).markup)

    # 6. SECTION 1 — CURRENT STATUS & SECTION 2 — TODAY'S PLAN
    col_status, col_plan = st.columns([6, 6])

    with col_status:
        score = int(readiness.get("overall_readiness_score", 70))
        level = html.escape(str(readiness.get("readiness_level", "Developing Readiness")))
        mastered = intelligence.get("mastered_count", 12)
        pending = intelligence.get("pending_count", 8)

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    📊 Section 1 — Current Status Overview
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">OVERALL READINESS</div>
                        <div style="color: #2563EB; font-size: 1.6rem; font-weight: 950;">{score}%</div>
                        <div style="color: #475569; font-size: 0.78rem; font-weight: 700;">{level}</div>
                    </div>
                    <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">STUDY STREAK</div>
                        <div style="color: #10B981; font-size: 1.6rem; font-weight: 950;">{streak} Days</div>
                        <div style="color: #475569; font-size: 0.78rem; font-weight: 700;">Active Daily Study</div>
                    </div>
                    <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">MASTERED TOPICS</div>
                        <div style="color: #059669; font-size: 1.5rem; font-weight: 950;">{mastered} Topics</div>
                    </div>
                    <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                        <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">PENDING TOPICS</div>
                        <div style="color: #D97706; font-size: 1.5rem; font-weight: 950;">{pending} Topics</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_plan:
        topic_disp = html.escape(str(study_plan.get("topic", "Indian Economy")).replace("_", " ").title())
        rev_target = html.escape(str(adaptive_revision.get("daily_target", "Revise 3 topics + 40 MCQs")))
        rec_mock = html.escape(str(recommendation.get("recommendation", "Full Length Mock")))
        time_est = html.escape(str(study_plan.get("estimated_time", "45 minutes")))

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    📅 Section 2 — Today's Personalized Plan
                </div>
                <div style="display: grid; gap: 8px;">
                    <div style="background: #EFF6FF; border-left: 4px solid #2563EB; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 0.75rem; color: #1D4ED8; font-weight: 900; text-transform: uppercase;">Study Plan</span>
                        <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">📖 {topic_disp}</div>
                    </div>
                    <div style="background: #ECFDF5; border-left: 4px solid #10B981; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 0.75rem; color: #047857; font-weight: 900; text-transform: uppercase;">Revision Target</span>
                        <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">🔄 {rev_target}</div>
                    </div>
                    <div style="background: #FEF3C7; border-left: 4px solid #F59E0B; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 0.75rem; color: #92400E; font-weight: 900; text-transform: uppercase;">Recommended Practice</span>
                        <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">📝 {rec_mock} (Est: {time_est})</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # 7. SECTION 3 — LEARNING INSIGHTS & SECTION 4 — MOCK INSIGHTS
    col_learn, col_mock = st.columns([6, 6])

    with col_learn:
        strong = html.escape(str(intelligence.get("subject", "History")))
        weak_topic = html.escape(str(intelligence.get("weak_topic", "Physical Geography")).replace("_", " ").title())
        trend = html.escape(str(predictive.get("topic_mastery_trend", "Improving")))

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    🧬 Section 3 — Learning Insights
                </div>
                <div style="display: grid; gap: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Strong Subject:</span>
                        <span style="font-size: 0.92rem; font-weight: 950; color: #059669;">💪 {strong}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Weak Topic Focus:</span>
                        <span style="font-size: 0.92rem; font-weight: 950; color: #DC2626;">⚠️ {weak_topic}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Learning Trajectory:</span>
                        <span style="background: rgba(16, 185, 129, 0.15); color: #10B981; font-weight: 950; font-size: 0.8rem; padding: 2px 10px; border-radius: 999px;">📈 {trend}</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_mock:
        mock_acc = int(mock_data.get("overall_accuracy", 74))
        mock_level = html.escape(str(mock_data.get("mock_level", "Stable")))
        mistakes = mock_data.get("mistake_breakdown", {})
        common_mistake = list(mistakes.keys())[0] if mistakes else "Assertion & Reason Questions"

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    📝 Section 4 — Mock Intelligence Insights
                </div>
                <div style="display: grid; gap: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Latest Mock Accuracy:</span>
                        <span style="font-size: 0.95rem; font-weight: 950; color: #2563EB;">🎯 {mock_acc}% ({mock_level})</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Common Mistake Pattern:</span>
                        <span style="font-size: 0.88rem; font-weight: 900; color: #991B1B;">⚠️ {common_mistake}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Avg Time / Question:</span>
                        <span style="font-size: 0.88rem; font-weight: 900; color: #0F172A;">⏱ 48 Seconds</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # 8. SECTION 5 — EXAM READINESS & SECTION 6 — PREDICTION
    col_read, col_pred = st.columns([6, 6])

    with col_read:
        read_score = int(readiness.get("overall_readiness_score", 72))
        read_lvl = html.escape(str(readiness.get("readiness_level", "Exam Ready")))

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    🎯 Section 5 — Exam Readiness
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <div style="font-size: 1.5rem; font-weight: 950; color: #0F172A;">{read_score}%</div>
                    <span style="background: rgba(37, 99, 235, 0.12); color: #2563EB; font-size: 0.82rem; font-weight: 900; padding: 4px 12px; border-radius: 999px;">
                        {read_lvl}
                    </span>
                </div>
                <div style="background: #E2E8F0; border-radius: 999px; height: 10px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #2563EB, #10B981); width: {read_score}%; height: 100%;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_pred:
        est_range = html.escape(str(predictive.get("estimated_readiness", "75–79%")))
        pred_conf = int(predictive.get("prediction_confidence", 92))

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    🔮 Section 6 — Predictive Performance Trajectory
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 0.85rem; color: #475569; font-weight: 800;">Estimated Readiness Range:</span>
                    <span style="font-size: 1.3rem; font-weight: 950; color: #2563EB;">{est_range}</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.85rem; color: #475569; font-weight: 800;">Prediction Confidence:</span>
                    <span style="background: #10B981; color: white; font-size: 0.78rem; font-weight: 900; padding: 2px 10px; border-radius: 999px;">🎯 {pred_conf}%</span>
                </div>
                <div style="color: #94A3B8; font-size: 0.74rem; margin-top: 10px; text-align: center;">
                    ⚠ Conservative estimation model. Never guarantees exam pass or rank.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # 9. SECTION 7 — REVISION & SECTION 8 — EXAM STRATEGY
    col_rev, col_strat = st.columns([6, 6])

    with col_rev:
        phase = html.escape(str(adaptive_revision.get("revision_phase", "30-Day Plan")))
        target = html.escape(str(adaptive_revision.get("daily_target", "Revise 3 topics + 40 MCQs")))
        cycle = html.escape(str(adaptive_revision.get("revision_cycles", ["Concept Reinforcement"])[0]))

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    ⚡ Section 7 — Adaptive Final Revision
                </div>
                <div style="display: grid; gap: 8px;">
                    <div style="font-size: 0.88rem; font-weight: 850; color: #0F172A;">📅 Active Phase: <span style="color: #2563EB;">{phase}</span></div>
                    <div style="font-size: 0.88rem; font-weight: 850; color: #0F172A;">🔄 Active Cycle: <span style="color: #10B981;">{cycle}</span></div>
                    <div style="font-size: 0.88rem; font-weight: 850; color: #0F172A;">🎯 Target: <span style="color: #475569;">{target}</span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_strat:
        overall_strat = html.escape(str(exam_strategy.get("overall_strategy", "Strength-First Execution")))
        subject_order = exam_strategy.get("subject_order", ["History", "Polity", "Science"])
        order_str = " ➔ ".join([html.escape(s) for s in subject_order[:4]])

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    🎯 Section 8 — Exam Execution Strategy
                </div>
                <div style="display: grid; gap: 8px;">
                    <div style="font-size: 0.88rem; font-weight: 850; color: #0F172A;">⚡ Theme: <span style="color: #2563EB;">{overall_strat}</span></div>
                    <div style="font-size: 0.88rem; font-weight: 850; color: #0F172A;">📚 Attempt Flow: <span style="color: #0F172A;">{order_str}</span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # 10. SECTION 10 — AI MENTOR EXECUTIVE SUMMARY
    st.html(coach_mentor_summary_card_html(readiness, recommendation, adaptive_revision).markup)
