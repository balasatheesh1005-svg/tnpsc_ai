import html
import streamlit as st

from core.study_planner_ai import get_personal_study_plan
from ui.components.cards import (
    glass_card_html,
    planner_sequence_timeline_html,
    planner_task_card_html,
    render_card_styles,
)


def render_study_planner_dashboard(user: str = None):
    """
    Personal Study Planner Dashboard V2.
    Renders output ONLY from core.study_planner_ai.
    Zero planning logic or duplicate calculations performed in UI.
    """
    render_card_styles()

    # 1. Page Title Header
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0F172A, #1E3A8A, #2563EB); padding: 24px; border-radius: 20px; color: white; margin-bottom: 20px; box-shadow: 0 10px 28px rgba(37, 99, 235, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                <div>
                    <h2 style="color: white; margin: 0; font-weight: 900; font-size: 1.8rem;">📅 Personal Study Planner Engine V2</h2>
                    <p style="color: #93C5FD; margin: 6px 0 0 0; font-size: 0.95rem; font-weight: 600;">
                        AI-Synthesized Daily Study Plan • Powered by Learning Intelligence Engine V2
                    </p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 8px 16px; border-radius: 999px; font-weight: 800; font-size: 0.88rem; border: 1px solid rgba(255, 255, 255, 0.2);">
                    ⚡ Deterministic Engine
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Interactive Available Study Time Selector
    st.markdown(
        """
        <div style="color: #0F172A; font-weight: 850; font-size: 0.95rem; margin-bottom: 8px;">
            ⏱️ Select Available Study Time Today:
        </div>
        """,
        unsafe_allow_html=True,
    )

    time_cols = st.columns([1, 1, 1, 1, 1])
    preset_times = [20, 45, 90, 120]

    if "study_planner_selected_time" not in st.session_state:
        st.session_state["study_planner_selected_time"] = 45

    current_time = st.session_state["study_planner_selected_time"]

    with time_cols[0]:
        if st.button("⚡ 20 Min", use_container_width=True, type="primary" if current_time == 20 else "secondary"):
            st.session_state["study_planner_selected_time"] = 20
            st.rerun()

    with time_cols[1]:
        if st.button("📘 45 Min", use_container_width=True, type="primary" if current_time == 45 else "secondary"):
            st.session_state["study_planner_selected_time"] = 45
            st.rerun()

    with time_cols[2]:
        if st.button("🚀 90 Min", use_container_width=True, type="primary" if current_time == 90 else "secondary"):
            st.session_state["study_planner_selected_time"] = 90
            st.rerun()

    with time_cols[3]:
        if st.button("🔥 120 Min", use_container_width=True, type="primary" if current_time == 120 else "secondary"):
            st.session_state["study_planner_selected_time"] = 120
            st.rerun()

    with time_cols[4]:
        custom_time = st.number_input(
            "Custom (Mins)",
            min_value=10,
            max_value=240,
            value=current_time if current_time not in preset_times else 60,
            step=5,
            label_visibility="collapsed",
        )
        if custom_time != current_time and current_time not in preset_times:
            st.session_state["study_planner_selected_time"] = custom_time

    selected_time = st.session_state["study_planner_selected_time"]

    # 3. Fetch Master Planner Output (STRICTLY FROM ENGINE)
    from core.user_context import UserContext
    ctx = UserContext.get_or_create(user)
    plan = get_personal_study_plan(user=user, available_time=selected_time, context=ctx)


    today_plan = plan.get("today_plan", [])
    estimated_time = plan.get("estimated_time", 45)
    expected_xp = plan.get("expected_xp", 80)
    mastery_gain = plan.get("expected_mastery_gain", "+12%")
    outcome = plan.get("expected_outcome", {})
    sequence = plan.get("study_sequence", [])
    next_action = plan.get("next_action", "Attempt PYQ")
    mentor_msg = plan.get("mentor_message", "Focus on recovering weak areas.")
    summary = plan.get("daily_summary", {})

    st.write("")

    # 4. Section 1 - 🧠 Mentor Banner
    st.markdown(
        f"""
        <div class="nova-glass-card" style="padding: 18px 22px; margin-bottom: 20px; background: linear-gradient(135deg, rgba(239, 246, 255, 0.95), rgba(243, 232, 255, 0.95)); border: 1px solid rgba(59, 130, 246, 0.3);">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div style="font-size: 2.2rem; background: #2563EB; color: white; border-radius: 50%; width: 48px; height: 48px; display: grid; place-items: center; flex-shrink: 0; box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3);">
                    🧠
                </div>
                <div>
                    <div style="color: #1E40AF; font-size: 0.8rem; font-weight: 900; text-transform: uppercase; letter-spacing: 0.5px;">AI Mentor Daily Focus Directive</div>
                    <div style="color: #0F172A; font-size: 1.05rem; font-weight: 850; margin-top: 2px;">
                        "{html.escape(mentor_msg)}"
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 5. Section 2 - 📊 Daily Summary & Metric Grid
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 16px; text-align: center;">
                <div style="color: #64748B; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">Today's Goal</div>
                <div style="color: #0F172A; font-size: 1.6rem; font-weight: 950; margin-top: 4px;">{summary.get('today_goal', '3 Tasks')}</div>
                <div style="color: #2563EB; font-size: 0.78rem; font-weight: 800; margin-top: 4px;">🎯 Optimized Plan</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 16px; text-align: center;">
                <div style="color: #64748B; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">⏱️ Estimated Time</div>
                <div style="color: #0F172A; font-size: 1.6rem; font-weight: 950; margin-top: 4px;">{estimated_time} Mins</div>
                <div style="color: #64748B; font-size: 0.78rem; font-weight: 800; margin-top: 4px;">Max Limit: {selected_time}m</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 16px; text-align: center;">
                <div style="color: #64748B; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">🏆 Potential XP</div>
                <div style="color: #D97706; font-size: 1.6rem; font-weight: 950; margin-top: 4px;">+{expected_xp} XP</div>
                <div style="color: #D97706; font-size: 0.78rem; font-weight: 800; margin-top: 4px;">Level Boost</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 16px; text-align: center;">
                <div style="color: #64748B; font-size: 0.78rem; font-weight: 800; text-transform: uppercase;">📈 Expected Mastery</div>
                <div style="color: #16A34A; font-size: 1.6rem; font-weight: 950; margin-top: 4px;">{mastery_gain}</div>
                <div style="color: #16A34A; font-size: 0.78rem; font-weight: 800; margin-top: 4px;">Topic Progression</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # 6. Main Grid: Left = Today's Plan & Timeline, Right = Outcome & Next Action
    left_col, right_col = st.columns([7, 5])

    with left_col:
        st.markdown("<h3 style='color: #0F172A; font-weight: 900;'>🎯 Today's Prioritized Study Plan</h3>", unsafe_allow_html=True)
        if not today_plan:
            st.info("No study tasks generated for this time slot.")
        else:
            for task_item in today_plan:
                st.html(planner_task_card_html(task_item).markup)

        st.write("")
        st.html(planner_sequence_timeline_html(sequence).markup)

    with right_col:
        st.markdown("<h3 style='color: #0F172A; font-weight: 900;'>📈 Expected Outcome & Progress</h3>", unsafe_allow_html=True)

        curr_m = outcome.get("current_mastery", "45%")
        exp_m = outcome.get("expected_mastery", "80%")
        curr_c = outcome.get("current_confidence", "Low")
        exp_c = outcome.get("expected_confidence", "Medium")

        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; margin-bottom: 20px;">
                <div style="font-size: 1.05rem; font-weight: 900; color: #0F172A; margin-bottom: 14px;">
                    📊 Expected Learning Outcome
                </div>
                <div style="display: flex; justify-content: space-around; align-items: center; background: rgba(248, 250, 252, 0.9); padding: 16px; border-radius: 14px; border: 1px solid #E2E8F0; margin-bottom: 14px;">
                    <div style="text-align: center;">
                        <span style="color: #64748B; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: block;">Current Mastery</span>
                        <span style="color: #0F172A; font-size: 1.8rem; font-weight: 950;">{curr_m}</span>
                        <span style="background: rgba(239, 68, 68, 0.1); color: #DC2626; font-size: 0.75rem; font-weight: 850; padding: 2px 8px; border-radius: 999px; display: inline-block; margin-top: 4px;">{curr_c} Confidence</span>
                    </div>
                    <div style="font-size: 1.8rem; color: #2563EB; font-weight: 900;">➜</div>
                    <div style="text-align: center;">
                        <span style="color: #166534; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; display: block;">Expected Mastery</span>
                        <span style="color: #16A34A; font-size: 1.8rem; font-weight: 950;">{exp_m}</span>
                        <span style="background: rgba(34, 197, 94, 0.1); color: #16A34A; font-size: 0.75rem; font-weight: 850; padding: 2px 8px; border-radius: 999px; display: inline-block; margin-top: 4px;">{exp_c} Confidence</span>
                    </div>
                </div>
                <div style="color: #475569; font-size: 0.85rem; font-weight: 750; background: rgba(37, 99, 235, 0.06); padding: 10px 14px; border-radius: 10px; border: 1px solid rgba(37, 99, 235, 0.2);">
                    💡 <strong>Learning Progression:</strong> Completing today's plan builds strong conceptual linking and elevates Topic Mastery by <strong>{mastery_gain}</strong>.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Next Recommended Action Box
        st.markdown(
            f"""
            <div class="nova-glass-card" style="padding: 20px; background: linear-gradient(135deg, rgba(254, 243, 199, 0.9), rgba(255, 255, 255, 0.95)); border: 1px solid rgba(245, 158, 11, 0.4);">
                <div style="color: #D97706; font-size: 0.8rem; font-weight: 900; text-transform: uppercase; letter-spacing: 0.5px;">
                    ➡ Next Recommended Action After Today's Plan
                </div>
                <div style="color: #0F172A; font-size: 1.15rem; font-weight: 950; margin: 8px 0;">
                    {html.escape(next_action)}
                </div>
                <div style="color: #64748B; font-size: 0.85rem; font-weight: 750;">
                    Determined automatically based on post-session mastery trajectory.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
