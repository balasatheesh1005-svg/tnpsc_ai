import html
import streamlit as st

from core.coach_maturity_ai import get_coach_maturity
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
from core.test_topic_selector import start_practice_test

from ui.components.cards import (
    coach_hero_card_html,
    coach_next_best_action_card_html,
    coach_mentor_summary_card_html,
    render_card_styles,
)


def navigate_to_practice_questions():
    """
    Canonical navigation helper from AI Coach onboarding to Study Hub Practice Questions.
    Sets destination to Learn & Practice Hub -> Practice Questions area without
    auto-launching tests or mutating widget-bound state.
    """
    st.session_state["navigate_to"] = "📚 Learn & Practice"
    st.session_state["main_menu"] = "📚 Learn & Practice"
    st.session_state["learn_practice_sub_tab"] = "🎯 Practice Questions"
    st.session_state["test_active"] = False
    st.session_state["practice_active"] = False
    st.session_state["active_practice_setup"] = None


def render_coach_dashboard(user: str = None):
    """
    Flagship AI Exam Coach Dashboard V2.
    Unifies outputs from master intelligence engines under a truthful 3-state maturity model:
    1. NO_DATA (0 completed tests)
    2. EARLY_INSIGHTS (1-4 completed tests)
    3. PERSONALIZED_COACH (5+ completed tests)
    
    PURE PRESENTATION LAYER:
    - Zero calculations
    - Zero predictions
    - Zero evaluations
    - Zero strategy creation
    - Zero database mutations
    Renders outputs exclusively received from master core engines and maturity gate.
    """
    render_card_styles()

    # 1. Fetch Maturity Gate Evaluation
    maturity = get_coach_maturity(user)
    coach_state = maturity["state"]

    # 2. Fetch Outputs from All Master Core AI Engines
    readiness = get_exam_readiness(user)
    recommendation = get_ai_recommendation(user)
    study_plan = get_personal_study_plan(user, available_time=45)
    intelligence = get_learning_intelligence(user)
    mock_data = get_mock_intelligence(user)
    predictive = get_predictive_performance(user)
    adaptive_revision = get_adaptive_final_revision(user)
    exam_strategy = get_exam_strategy(user)
    streak = maturity.get("streak", 0)

    # 3. Page Title Header
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(37, 99, 235, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">🤖 AI Exam Coach Dashboard V2</h2>
                    <p style="color: #93C5FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        Flagship Mentor Experience • Unified Exam Intelligence Hub
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

    # =========================================================================
    # STATE 1 — NO_DATA (0 Tests Completed: Pure Onboarding Experience)
    # =========================================================================
    if coach_state == "NO_DATA":
        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 26px; margin-bottom: 22px; background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); border: 1px solid rgba(147, 197, 253, 0.35); color: white; box-shadow: 0 16px 36px rgba(37, 99, 235, 0.25);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 18px;">
                    <div style="flex: 1; min-width: 280px;">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                            <span style="background: rgba(59, 130, 246, 0.3); color: #93C5FD; border: 1px solid rgba(147, 197, 253, 0.4); font-size: 0.8rem; font-weight: 900; padding: 4px 14px; border-radius: 999px; text-transform: uppercase;">
                                🤖 AI Exam Coach
                            </span>
                            <span style="background: rgba(255, 255, 255, 0.18); color: white; font-size: 0.8rem; font-weight: 900; padding: 4px 14px; border-radius: 999px;">
                                🚀 Welcome Aspirant
                            </span>
                        </div>
                        <div style="color: white; font-size: 1.8rem; font-weight: 950; line-height: 1.25; margin-bottom: 8px;">
                            Welcome to AI Exam Coach! 👋
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.12); backdrop-filter: blur(10px); border-left: 4px solid #60A5FA; padding: 12px 16px; border-radius: 10px; color: #E2E8F0; font-size: 0.92rem; font-weight: 700; line-height: 1.45;">
                            "Complete your first practice test to unlock personalized readiness, weakness analysis, revision strategy and recommendations."
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Primary Canonical Call-to-Action
        st.markdown(
            """
            <div class="nova-glass-card" style="padding: 24px; text-align: center; border: 2px dashed #3B82F6; margin-bottom: 20px; background: rgba(239, 246, 255, 0.9);">
                <div style="font-size: 1.3rem; font-weight: 950; color: #1E3A8A; margin-bottom: 8px;">
                    🎯 Explore Practice Questions
                </div>
                <p style="color: #475569; font-size: 0.95rem; max-width: 620px; margin: 0 auto 16px auto;">
                    Choose a subject, topic and practice mode to begin. Your performance will help AI Exam Coach build personalized readiness and weakness insights.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("🚀 Explore Practice Questions", type="primary", use_container_width=True, key="coach_btn_first_test"):
            navigate_to_practice_questions()
            st.rerun()

        st.write("")

        # Quick Actions Bar
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
            if st.button("🚀 Study Plan", use_container_width=True, key="qa_no_data_plan"):
                st.session_state["navigate_to"] = "📅 Study Planner"
                st.rerun()
        with col2:
            if st.button("🔄 Revision", use_container_width=True, key="qa_no_data_rev"):
                st.session_state["navigate_to"] = "⚡ Adaptive Revision Strategy"
                st.rerun()
        with col3:
            if st.button("📝 Attempt Mock", use_container_width=True, key="qa_no_data_mock"):
                st.session_state["navigate_to"] = "📝 Mock Intelligence"
                st.rerun()
        with col4:
            if st.button("🎯 First Practice", use_container_width=True, key="qa_no_data_prac"):
                navigate_to_practice_questions()
                st.rerun()
        with col5:
            if st.button("📜 View PYQs", use_container_width=True, key="qa_no_data_pyq"):
                st.session_state["navigate_to"] = "PYQ"
                st.rerun()
        with col6:
            if st.button("📚 Smart Notes", use_container_width=True, key="qa_no_data_notes"):
                st.session_state["navigate_to"] = "📚 Notes"
                st.rerun()

        st.write("")

        # Section 9 — Starter Recommendation
        st.html(coach_next_best_action_card_html(recommendation).markup)

        # What Unlocks Next Preview Grid
        st.markdown(
            """
            <div class="nova-glass-card" style="padding: 22px; margin-bottom: 22px;">
                <div style="font-size: 1.1rem; font-weight: 950; color: #0F172A; margin-bottom: 14px;">
                    🔓 What Unlocks With Your Practice?
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
                    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 14px; border-radius: 12px;">
                        <div style="font-size: 1.2rem; margin-bottom: 4px;">🎯</div>
                        <div style="font-weight: 900; color: #1E293B; font-size: 0.95rem;">Exam Readiness Index</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 4px;">Weighted multi-dimensional readiness tracking across syllabus subjects.</div>
                    </div>
                    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 14px; border-radius: 12px;">
                        <div style="font-size: 1.2rem; margin-bottom: 4px;">🧠</div>
                        <div style="font-weight: 900; color: #1E293B; font-size: 0.95rem;">Weakness & Mistake Diagnosis</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 4px;">Automatic identification of tricky question types and knowledge gaps.</div>
                    </div>
                    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 14px; border-radius: 12px;">
                        <div style="font-size: 1.2rem; margin-bottom: 4px;">⚡</div>
                        <div style="font-weight: 900; color: #1E293B; font-size: 0.95rem;">Spaced Revision Plan</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 4px;">Intelligent spaced recall scheduling to counteract forgetting.</div>
                    </div>
                    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 14px; border-radius: 12px;">
                        <div style="font-size: 1.2rem; margin-bottom: 4px;">🔮</div>
                        <div style="font-weight: 900; color: #1E293B; font-size: 0.95rem;">Trajectory Forecasting</div>
                        <div style="font-size: 0.8rem; color: #64748B; margin-top: 4px;">Conservative readiness estimation based strictly on verified test data.</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.html(coach_mentor_summary_card_html(readiness, recommendation, adaptive_revision).markup)
        return

    # =========================================================================
    # STATE 2 & 3: EARLY_INSIGHTS and PERSONALIZED_COACH
    # =========================================================================

    # Hero Card
    st.html(coach_hero_card_html(user, readiness, recommendation, streak).markup)

    # State Status Banner for Early Insights
    if coach_state == "EARLY_INSIGHTS":
        st.markdown(
            f"""
            <div style="background: #FEF3C7; border: 1px solid #F59E0B; padding: 12px 18px; border-radius: 12px; margin-bottom: 18px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                <div style="color: #92400E; font-weight: 850; font-size: 0.92rem;">
                    ⚡ <b>Early Insights Stage:</b> {maturity['attempt_count']} test(s) completed. Keep practicing (5+ tests) to unlock full multi-dimensional readiness and prediction trajectory.
                </div>
                <span style="background: #D97706; color: white; padding: 3px 10px; border-radius: 999px; font-weight: 900; font-size: 0.75rem;">
                    {maturity['attempt_count']} / 5 Tests
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # QUICK ACTIONS BAR
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
        if st.button("🚀 Study Plan", use_container_width=True, key="qa_coach_plan"):
            st.session_state["navigate_to"] = "📅 Study Planner"
            st.rerun()

    with col2:
        if st.button("🔄 Revision", use_container_width=True, key="qa_coach_rev"):
            st.session_state["navigate_to"] = "⚡ Adaptive Revision Strategy"
            st.rerun()

    with col3:
        if st.button("📝 Attempt Mock", use_container_width=True, key="qa_coach_mock"):
            st.session_state["navigate_to"] = "📝 Mock Intelligence"
            st.rerun()

    with col4:
        if maturity.get("weakness_eligible") and maturity.get("weak_topic"):
            if st.button("🧠 Weak Topic", use_container_width=True, key="qa_coach_weak"):
                st.session_state["learn_practice_sub_tab"] = "🧠 Weak Areas"
                st.session_state["navigate_to"] = "🧠 Weakness"
                st.rerun()
        else:
            if st.button("🎯 Practice", use_container_width=True, key="qa_coach_prac"):
                success, msg = start_practice_test(
                    subject="polity",
                    topic="historical_background",
                    level="easy",
                    mode="daily",
                    q_count=10,
                    navigate=True,
                )
                if success:
                    st.rerun()
                else:
                    st.error(msg)

    with col5:
        if st.button("📜 View PYQs", use_container_width=True, key="qa_coach_pyq"):
            st.session_state["navigate_to"] = "PYQ"
            st.rerun()

    with col6:
        if st.button("📚 Smart Notes", use_container_width=True, key="qa_coach_notes"):
            st.session_state["navigate_to"] = "📚 Notes"
            st.rerun()

    st.write("")

    # SECTION 9 — NEXT BEST ACTION
    st.html(coach_next_best_action_card_html(recommendation).markup)

    # SECTION 1 — CURRENT STATUS & SECTION 2 — TODAY'S PLAN
    col_status, col_plan = st.columns([6, 6])

    with col_status:
        if coach_state == "EARLY_INSIGHTS":
            attempts_disp = f"{maturity['attempt_count']} Tests"
            acc_disp = f"{maturity['avg_accuracy']}%"
            streak_disp = f"{streak} Days"
            topics_disp = f"{maturity['topics_attempted']} Topics"

            st.markdown(
                f"""
                <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                    <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                        📊 Section 1 — Early Activity Overview
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">TESTS COMPLETED</div>
                            <div style="color: #2563EB; font-size: 1.6rem; font-weight: 950;">{attempts_disp}</div>
                            <div style="color: #475569; font-size: 0.78rem; font-weight: 700;">Baseline Activity</div>
                        </div>
                        <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">AVERAGE ACCURACY</div>
                            <div style="color: #059669; font-size: 1.6rem; font-weight: 950;">{acc_disp}</div>
                            <div style="color: #475569; font-size: 0.78rem; font-weight: 700;">Real Observed</div>
                        </div>
                        <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">STUDY STREAK</div>
                            <div style="color: #10B981; font-size: 1.5rem; font-weight: 950;">{streak_disp}</div>
                        </div>
                        <div style="background: #F8FAFC; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                            <div style="color: #64748B; font-size: 0.75rem; font-weight: 800;">TOPICS PRACTICED</div>
                            <div style="color: #D97706; font-size: 1.5rem; font-weight: 950;">{topics_disp}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            # Mature Personalized Coach
            raw_score = readiness.get("overall_readiness_score")
            score = int(raw_score) if raw_score is not None else 0
            level = html.escape(str(readiness.get("readiness_level", "Developing Readiness")))
            mastered = maturity.get("mastered_count", 0)
            pending = maturity.get("pending_count", 0)

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
        topic_disp = html.escape(str(study_plan.get("topic", "Indian Polity")).replace("_", " ").title())
        rev_target = html.escape(str(adaptive_revision.get("daily_target", "Daily Practice Target")))
        rec_mock = html.escape(str(recommendation.get("recommendation", "Daily Practice Set")))
        time_est = html.escape(str(study_plan.get("estimated_time", "30 minutes")))

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    📅 Section 2 — Today's Plan
                </div>
                <div style="display: grid; gap: 8px;">
                    <div style="background: #EFF6FF; border-left: 4px solid #2563EB; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 0.75rem; color: #1D4ED8; font-weight: 900; text-transform: uppercase;">Study Focus</span>
                        <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">📖 {topic_disp}</div>
                    </div>
                    <div style="background: #ECFDF5; border-left: 4px solid #10B981; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 0.75rem; color: #047857; font-weight: 900; text-transform: uppercase;">Revision Target</span>
                        <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">🔄 {rev_target}</div>
                    </div>
                    <div style="background: #FEF3C7; border-left: 4px solid #F59E0B; padding: 10px 14px; border-radius: 8px;">
                        <span style="font-size: 0.75rem; color: #92400E; font-weight: 900; text-transform: uppercase;">Recommended Activity</span>
                        <div style="font-size: 0.95rem; font-weight: 900; color: #0F172A;">📝 {rec_mock} (Est: {time_est})</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # SECTION 3 — LEARNING INSIGHTS & SECTION 4 — MOCK INSIGHTS
    col_learn, col_mock = st.columns([6, 6])

    with col_learn:
        strong = maturity.get("strong_subject") or ("Collecting data..." if coach_state == "EARLY_INSIGHTS" else "General")
        weak_topic = maturity.get("weak_topic") or ("Not enough data yet" if coach_state == "EARLY_INSIGHTS" else "No critical weakness recorded")
        trend = "Baseline In Progress" if coach_state == "EARLY_INSIGHTS" else html.escape(str(predictive.get("topic_mastery_trend", "Stable")))

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
        if maturity.get("mock_eligible") and maturity.get("latest_mock_accuracy") is not None:
            mock_acc_disp = f"🎯 {maturity['latest_mock_accuracy']}% ({mock_data.get('mock_level', 'Completed')})"
            mistakes_list = mock_data.get("mistakes", [])
            common_mistake = mistakes_list[0]["pattern"] if mistakes_list else "No recurring pattern observed"
        else:
            mock_acc_disp = "No mock attempted yet"
            common_mistake = "Collecting mistake patterns..." if coach_state == "EARLY_INSIGHTS" else "No mock history available"

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; height: 100%;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 12px;">
                    📝 Section 4 — Mock Intelligence Insights
                </div>
                <div style="display: grid; gap: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Latest Mock Accuracy:</span>
                        <span style="font-size: 0.95rem; font-weight: 950; color: #2563EB;">{mock_acc_disp}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Common Mistake Pattern:</span>
                        <span style="font-size: 0.88rem; font-weight: 900; color: #991B1B;">⚠️ {common_mistake}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; background: #F8FAFC; padding: 10px 14px; border-radius: 10px;">
                        <span style="font-size: 0.88rem; font-weight: 800; color: #475569;">Question Pace:</span>
                        <span style="font-size: 0.88rem; font-weight: 900; color: #0F172A;">⏱ Standard: 54s / Question (TNPSC Guideline)</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # SECTION 5 — EXAM READINESS & SECTION 6 — PREDICTION
    col_read, col_pred = st.columns([6, 6])

    with col_read:
        if coach_state == "EARLY_INSIGHTS":
            raw_avg = maturity.get("avg_accuracy")
            read_score = int(raw_avg) if raw_avg is not None else 0
            read_lvl = "Early Assessment"
        else:
            raw_score = readiness.get("overall_readiness_score")
            read_score = int(raw_score) if raw_score is not None else 0
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
                    <div style="background: linear-gradient(90deg, #2563EB, #10B981); width: {max(5, read_score)}%; height: 100%;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_pred:
        if not maturity["prediction_eligible"]:
            est_range = "Unlocks at 5 tests"
            pred_conf_disp = "Unlocks at 5 tests"
            note = "⚠ Conservative estimation requires at least 5 completed test records."
        else:
            est_range = html.escape(str(predictive.get("estimated_readiness", "Unavailable")))
            conf_val = int(predictive.get("prediction_confidence") or 0)
            pred_conf_disp = f"🎯 {conf_val}%"
            note = "⚠ Conservative estimation model. Never guarantees exam pass or rank."

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
                    <span style="background: #10B981; color: white; font-size: 0.78rem; font-weight: 900; padding: 2px 10px; border-radius: 999px;">{pred_conf_disp}</span>
                </div>
                <div style="color: #94A3B8; font-size: 0.74rem; margin-top: 10px; text-align: center;">
                    {note}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # SECTION 7 — REVISION & SECTION 8 — EXAM STRATEGY
    col_rev, col_strat = st.columns([6, 6])

    with col_rev:
        phase = html.escape(str(adaptive_revision.get("revision_phase", "Foundation Phase")))
        target = html.escape(str(adaptive_revision.get("daily_target", "Complete 10 Daily Practice Questions")))
        cycles = adaptive_revision.get("revision_cycles", ["Concept Reinforcement"])
        cycle = html.escape(str(cycles[0] if cycles else "Concept Reinforcement"))

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
        subject_order = exam_strategy.get("subject_order", ["Polity", "History", "Science"])
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

    # SECTION 10 — AI MENTOR EXECUTIVE SUMMARY
    st.html(coach_mentor_summary_card_html(readiness, recommendation, adaptive_revision).markup)
