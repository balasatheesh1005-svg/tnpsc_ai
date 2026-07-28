import html
import streamlit as st
from ui.components.cards import glass_card_html, html_fragment, analytics_grid


def render_universal_result_screen(
    score: int,
    total_questions: int,
    prefix: str,
    subject: str = "General",
    topic: str = "General",
    weak_topic: str = "No Data",
    strong_topic: str = "No Data",
    xp_earned: int = 0,
    streak_days: int = 0,
    on_retry_wrong=None,
    on_start_new=None,
):
    percent = int((score / max(1, total_questions)) * 100)

    # 1. Glass Card Header
    st.html(
        f"""
        <div class="progress-header">
            <div class="progress-details">
                <span class="progress-pill">🎉 Test Completed</span>
                <span class="progress-pill">Score: {score} / {total_questions}</span>
            </div>
            <span class="progress-pill">Accuracy: {percent}%</span>
        </div>
        """
    )

    # 2. Analytics Items
    analytics_items = [
        ("🔥 Streak", f"{streak_days} days"),
        ("⚡ XP Earned", f"+{xp_earned} XP"),
        ("💪 Strong Topic", strong_topic),
        ("📚 Weak Topic", weak_topic),
    ]

    card_html = glass_card_html(
        f"🏆 Test Performance Summary ({subject})",
        value=f"{percent}% Accuracy",
        body=f"Topic: {topic.title()}",
        extra_html=html_fragment(
            analytics_grid(analytics_items).markup
        ),
    )
    st.html(card_html)

    # 3. Recommendations Card
    if percent >= 80:
        st.success("🎉 Excellent Performance! You demonstrated high mastery in this session.")
    elif percent >= 50:
        st.info("👍 Good effort! Focus on revising your weak topics before attempting Grand Tests.")
    else:
        st.warning("⚠️ Practice needed. We recommend reviewing the core notes and retrying wrong questions.")

    # 4. Action Buttons Grid
    st.markdown("### Next Steps")
    btn1, btn2, btn3 = st.columns(3, gap="small")

    with btn1:
        if st.button("🔄 Retry Wrong Questions", key=f"{prefix}_retry_wrong", type="primary", use_container_width=True):
            if on_retry_wrong:
                on_retry_wrong()
            else:
                st.toast("Retrying incorrectly answered questions...", icon="🔄")

    with btn2:
        if st.button("📚 Revise Weak Topics", key=f"{prefix}_revise_weak", use_container_width=True):
            st.session_state["navigate_to"] = "🧠 Weakness"
            st.rerun()

    with btn3:
        if st.button("🚀 Start New Test", key=f"{prefix}_new_test", use_container_width=True):
            if on_start_new:
                on_start_new()
            else:
                st.session_state["test_active"] = False
                st.rerun()
