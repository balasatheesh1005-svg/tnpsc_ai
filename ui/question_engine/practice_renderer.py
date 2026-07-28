import html
import time
import streamlit as st

from core.question_engine.practice_session import (
    clear_practice_session,
    complete_practice_session,
    get_next_repository_type,
    get_practice_state,
    get_practice_summary,
    next_practice_question,
    record_practice_answer,
    set_practice_question_index,
    start_practice_session,
)
from core.navigation_v2.navigation_state import (
    check_repository_availability,
    get_selected_display_title,
    get_selected_repository_id,
    get_selected_subject,
    get_selected_topic_id,
)
from ui.components.cards import (
    achievement_card,
    achievement_grid,
    analytics_grid,
    glass_card_html,
    html_fragment,
    learning_journey_roadmap,
    micro_motivation_banner,
    repository_progress_card,
)
from ui.question_engine.body_component import render_question_body
from ui.question_engine.explanation_component import render_explanation_card
from ui.question_engine.header_component import render_question_header
from ui.question_engine.option_component import render_option_cards
from ui.question_engine.palette_component import render_question_palette
from ui.question_engine.parser import NormalizedQuestion, UniversalQuestionAdapter


def _format_time(seconds: int) -> str:
    minutes = max(0, seconds) // 60
    secs = max(0, seconds) % 60
    return f"{minutes:02d}:{secs:02d}"


def render_practice_workspace(user: str):
    """
    Master UI Controller for the independent Practice Engine.
    Routes seamlessly between Question Renderer, Result Screen, and Review Mode.
    """
    state = get_practice_state()
    if not state["active"]:
        st.info("No practice session active.")
        return

    if state["review_mode"]:
        render_practice_review(user)
    elif state["completed"]:
        render_practice_result_screen(user)
    else:
        render_practice_question(user)


def render_practice_question(user: str):
    """Renders the current question card using Universal Renderer components."""
    state = get_practice_state()
    questions = state["questions"]
    curr_i = state["current_index"]
    total_q = len(questions)

    if not questions or curr_i >= total_q:
        st.warning("No questions available in practice stack.")
        return

    q_raw = questions[curr_i]
    q: NormalizedQuestion = UniversalQuestionAdapter.normalize(q_raw)
    prefix = "practice"

    # Top Control Bar (Exit Practice Button)
    col_nav_top, col_title_top = st.columns([1, 4], gap="small")
    with col_nav_top:
        if st.button("Continue Learning →", key="practice_exit_top_btn", use_container_width=True):
            clear_practice_session()
            st.rerun()
    with col_title_top:
        st.html(
            f"""
            <div style="padding: 4px 8px;">
                <span class="progress-pill" style="background:#EFF6FF; color:#2563EB; font-weight:800;">
                    🏛️ {html.escape(state['subject'].title())} &nbsp;|&nbsp; 📖 {html.escape(state['display_title'])}
                </span>
                <span class="progress-pill" style="background:#FEF3C7; color:#D97706; font-weight:800;">
                    📝 {html.escape(state['repository_type'].replace('_', ' ').title())} Repository
                </span>
            </div>
            """
        )

    st.markdown("---")

    # 1. Question Header (Progress, Timer, Badges, Language Mode, Bookmark)
    elapsed_time = int(time.time() - state["start_time"])
    render_question_header(
        q=q,
        current_index=curr_i,
        total_questions=total_q,
        prefix=prefix,
        timer_seconds=None,
    )

    # 2. Question Palette Expander
    if total_q > 1:
        with st.expander("🗂️ Question Palette & Jump Navigation", expanded=False):
            render_question_palette(
                prefix=prefix,
                total_questions=total_q,
                current_index=curr_i,
                bookmarked_set=st.session_state.get(f"{prefix}_bookmarks", set()),
            )

    # 3. Question Body
    lang_mode = st.session_state.get(f"{prefix}_lang_mode", "BOTH")
    render_question_body(q=q, lang_mode=lang_mode)

    # 4. Option Cards
    answers = state["answers"]
    is_answered = curr_i in answers
    selected_option = answers[curr_i]["selected_option"] if is_answered else ""

    chosen_key, _ = render_option_cards(
        q=q,
        prefix=prefix,
        disabled=is_answered,
        selected_option_key=selected_option,
    )

    # 5. Footer / Answer Submit / Navigation Controls
    st.markdown("<br>", unsafe_allow_html=True)
    c_prev, c_submit, c_next = st.columns([1, 2, 1], gap="small")

    with c_prev:
        if st.button("⬅️ Previous", key="practice_prev_q_btn", disabled=(curr_i == 0), use_container_width=True):
            set_practice_question_index(curr_i - 1)
            st.rerun()

    with c_submit:
        if not is_answered:
            if st.button("✅ Submit Answer", key="practice_submit_q_btn", type="primary", use_container_width=True):
                if not chosen_key:
                    st.warning("Please select an option before submitting.")
                else:
                    is_correct = (chosen_key == q.correct_answer)
                    record_practice_answer(curr_i, chosen_key, is_correct, q.id)
                    st.rerun()
        else:
            st.info(f"Answer Submitted: **{selected_option}**")

    with c_next:
        btn_label = "Finish Practice 🏁" if (curr_i + 1 == total_q) else "Next ➡️"
        if st.button(btn_label, key="practice_next_q_btn", type="primary" if is_answered else "secondary", use_container_width=True):
            next_practice_question()
            st.rerun()

    # 6. Explanation Component (Visible after submitting)
    if is_answered:
        st.markdown("---")
        render_explanation_card(
            q=q,
            prefix=prefix,
            user_choice=selected_option,
        )


def render_practice_result_screen(user: str):
    """Renders the Premium Intelligent Study Summary Screen with prioritized notifications, roadmap progress, and single primary CTA focus."""
    summary = complete_practice_session(user)

    subject = summary["subject"]
    topic_id = summary["topic_id"]
    repository_id = summary["repository_id"]
    repo_type = summary["repository_type"]
    display_title = summary["display_title"]
    total_q = summary["total_questions"]
    correct = summary["correct"]
    wrong = summary["wrong"]
    accuracy = summary["accuracy"]
    time_taken = summary["time_taken"]
    xp_earned = summary["xp_earned"]

    xp_already_awarded = summary.get("xp_already_awarded", False)
    xp_display = "0 XP" if xp_already_awarded else f"+{xp_earned} XP"
    streak = summary.get("streak", 0)

    PRACTICE_REPO_ORDER = [
        "easy",
        "medium",
        "hard",
        "statement_based",
        "assertion_reason",
        "match_the_following",
        "chronology",
        "pyq",
        "grand_test",
    ]
    curr_idx = PRACTICE_REPO_ORDER.index(repo_type) if repo_type in PRACTICE_REPO_ORDER else 0
    completed_count = curr_idx + 1
    total_repos = 9
    is_grand_test = (repo_type == "grand_test")
    is_mastered = is_grand_test  # Strict Topic Mastery Policy: ONLY after Grand Test

    avail = check_repository_availability(subject, topic_id or repository_id)
    next_repo_type = get_next_repository_type(repo_type, avail)

    # =========================================================================
    # FEATURE 2 & 4: PRIORITY NOTIFICATION QUEUE
    # Priority: 1. Topic Mastered -> 2. Primary Achievement -> 3. XP -> 4. Streak
    # =========================================================================

    # Priority 1: Topic Mastered Celebration (Shown ONLY after Grand Test)
    if is_mastered:
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%); padding: 20px 24px; border-radius: 16px; border: 2px solid #F59E0B; margin-bottom: 20px; color: #78350F; box-shadow: 0 10px 25px rgba(245, 158, 11, 0.25);">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                    <div>
                        <span style="background:#F59E0B; color:white; font-weight:800; font-size:0.8rem; padding:4px 12px; border-radius:12px;">
                            👑 MASTER MILESTONE
                        </span>
                        <h2 style="margin: 8px 0 4px 0; color: #92400E; font-size: 1.6rem;">🏆 Topic Mastered!</h2>
                        <p style="margin: 0; font-size: 0.9rem; color: #B45309;">
                            Congratulations! You have completed all 9 learning & practice stages for <b>{html.escape(display_title)}</b>.
                        </p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Priority 2: Primary Unlocked Achievement Notification (Highest Priority Card)
    unlocked_achievements = summary.get("unlocked_achievements", [])
    if unlocked_achievements:
        ach_tuples = [
            (
                ach["title"],
                ach["description"],
                ach["unlocked"],
                ach.get("level", "bronze"),
            )
            for ach in unlocked_achievements
        ]
        st.markdown("### 🥇 Priority Achievement Unlocked")
        st.html(achievement_grid(ach_tuples[:1]).markup)
        st.markdown("<br>", unsafe_allow_html=True)

    # Priority 3 & 4: XP & Streak Highlights
    if streak > 0:
        st.success(f"🔥 Daily Streak Active: {streak} Day(s)! Continuous effort builds mastery.")
    if xp_already_awarded:
        st.info("ℹ️ Practice session record updated. XP already awarded for this mode.")

    # =========================================================================
    # FEATURE 3: REPOSITORY COMPLETION CELEBRATION
    # =========================================================================
    repo_name_formatted = repo_type.replace('_', ' ').title()
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 22px; border-radius: 16px; color: white; margin-bottom: 20px; border: 1px solid #334155;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <div>
                    <span class="progress-pill" style="background:#DCFCE7; color:#15803D; font-weight:800; font-size:0.85rem;">
                        🎉 {html.escape(repo_name_formatted)} Repository Completed
                    </span>
                    <h2 style="margin: 8px 0 4px 0; color: #F8FAFC; font-size: 1.5rem;">📖 {html.escape(display_title)}</h2>
                    <p style="color: #94A3B8; font-size: 0.88rem; margin: 0;">
                        Status: <span style="color:#86EFAC; font-weight:700;">Repository Completed Successfully</span> &nbsp;|&nbsp; Reward: <b>{xp_display}</b>
                    </p>
                </div>
                <div>
                    <span class="progress-pill" style="background:#2563EB; color:white; font-weight:800; font-size:1.1rem; padding: 8px 16px;">
                        Accuracy: {accuracy}%
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================================
    # FEATURE 1: REPOSITORY PROGRESS PERCENTAGE
    # =========================================================================
    st.html(repository_progress_card(repo_type, completed_count, total_repos).markup)

    # =========================================================================
    # FEATURE 7: MICRO MOTIVATION BANNER
    # =========================================================================
    st.html(micro_motivation_banner(accuracy, streak, curr_idx).markup)

    # Secondary Unlocked Achievements (If more than 1 unlocked)
    if len(unlocked_achievements) > 1:
        with st.expander(f"🏅 Additional Achievements ({len(unlocked_achievements) - 1})", expanded=False):
            ach_tuples_rem = [
                (
                    ach["title"],
                    ach["description"],
                    ach["unlocked"],
                    ach.get("level", "bronze"),
                )
                for ach in unlocked_achievements[1:]
            ]
            st.html(achievement_grid(ach_tuples_rem).markup)

    # Performance Summary Glass Card (All 6 Existing Stats Preserved)
    analytics_items = [
        ("📦 Attempted", f"{total_q} Qs"),
        ("✅ Correct", f"{correct}"),
        ("❌ Wrong", f"{wrong}"),
        ("⏱ Time Taken", _format_time(time_taken)),
        ("⚡ XP Earned", xp_display),
        ("🎯 Accuracy Rate", f"{accuracy}%"),
    ]

    card_html = glass_card_html(
        f"🏆 Study Summary — {display_title}",
        value=f"{accuracy}% Accuracy",
        body=f"Subject: {subject.title()} | Mode: {repo_name_formatted}",
        extra_html=html_fragment(analytics_grid(analytics_items).markup),
    )
    st.html(card_html)

    # Performance Insight
    if accuracy >= 95:
        st.success("🏆 Outstanding Performance! You have demonstrated exceptional accuracy and topic recall.")
    elif accuracy >= 80:
        st.success("🌟 Excellent Work! You have a solid grasp of key concepts for this topic.")
    elif accuracy >= 60:
        st.info("👍 Good Progress! Review your wrong answers to strengthen weaker areas before continuing.")
    elif accuracy >= 40:
        st.warning("💡 Needs More Practice. We recommend retrying this mode or reviewing the 2-Minute Revision card.")
    else:
        st.warning("📖 Revise Before Continuing. Low accuracy detected. Please read topic notes before retrying.")

    st.markdown("---")

    # =========================================================================
    # FEATURE 5: LEARNING JOURNEY ROADMAP INDICATOR
    # =========================================================================
    st.html(learning_journey_roadmap(repo_type, avail).markup)

    st.markdown("---")

    # =========================================================================
    # FEATURE 4: PRIMARY ACTION FOCUS (EXACTLY ONE PRIMARY CTA BUTTON)
    # =========================================================================
    st.markdown("### 🚀 Next Step")

    if is_grand_test:
        next_btn_label = "Continue to Next Topic 📖"
    elif next_repo_type:
        formatted_name = next_repo_type.replace('_', ' ').title()
        next_btn_label = f"Continue → {formatted_name}"
    elif avail.get("grand_test"):
        next_btn_label = "Attempt Grand Test 🏆"
    else:
        next_btn_label = "Continue to Next Topic 📖"

    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4, gap="small")

    # SECONDARY ACTION 1: Review Answers
    with btn_col1:
        if st.button("📖 Review Answers", key="practice_res_btn_review", use_container_width=True):
            st.session_state["practice_review_mode"] = True
            st.rerun()

    # SECONDARY ACTION 2: Practice Again
    with btn_col2:
        if st.button("🔄 Practice Again", key="practice_res_btn_again", use_container_width=True):
            start_practice_session(subject, topic_id, repository_id, display_title, repo_type)
            st.rerun()

    # PRIMARY CTA ACTION (EXACTLY ONE PRIMARY BUTTON)
    with btn_col3:
        if is_mastered:
            if st.button("Continue to Next Topic 📖", key="practice_res_btn_next_topic", type="primary", use_container_width=True):
                from core.navigation_v2.navigation_state import get_available_topics, set_global_topic
                topics = get_available_topics(subject)
                curr_t_idx = -1
                for i, t in enumerate(topics):
                    if t.get("topic_id") == topic_id:
                        curr_t_idx = i
                        break
                if curr_t_idx != -1 and curr_t_idx + 1 < len(topics):
                    next_t = topics[curr_t_idx + 1]
                    set_global_topic(subject, next_t["topic_id"])
                else:
                    st.session_state["nav_view"] = "topic_select"
                clear_practice_session()
                st.session_state["study_stage"] = "completed"
                st.rerun()
        elif next_repo_type:
            if st.button(next_btn_label, key="practice_res_btn_next_repo", type="primary", use_container_width=True):
                start_practice_session(subject, topic_id, repository_id, display_title, next_repo_type)
                st.rerun()
        elif avail.get("grand_test"):
            if st.button("Attempt Grand Test 🏆", key="practice_res_btn_gt", type="primary", use_container_width=True):
                with st.spinner("⏳ Loading Grand Test Repository..."):
                    questions = load_questions(repository_id, "grand_test")
                    if questions:
                        clear_practice_session()
                        st.session_state.update({
                            "test_subject": subject,
                            "test_topic_id": topic_id,
                            "test_repository_id": repository_id,
                            "test_topic": repository_id,
                            "test_qs": questions,
                            "q_index": 0,
                            "score": 0,
                            "answered": False,
                            "test_active": True,
                            "test_mode": "grand_test",
                            "start_time": time.time(),
                            "test_start_xp": st.session_state.get("xp", 0),
                        })
                        st.session_state["main_menu"] = "📘 Daily Test"
                        st.rerun()
                    else:
                        st.error("Grand Test repository could not be loaded.")
        else:
            if st.button("Continue to Next Topic 📖", key="practice_res_btn_next_topic_fallback", type="primary", use_container_width=True):
                from core.navigation_v2.navigation_state import get_available_topics, set_global_topic
                topics = get_available_topics(subject)
                curr_t_idx = -1
                for i, t in enumerate(topics):
                    if t.get("topic_id") == topic_id:
                        curr_t_idx = i
                        break
                if curr_t_idx != -1 and curr_t_idx + 1 < len(topics):
                    next_t = topics[curr_t_idx + 1]
                    set_global_topic(subject, next_t["topic_id"])
                else:
                    st.session_state["nav_view"] = "topic_select"
                clear_practice_session()
                st.session_state["study_stage"] = "completed"
                st.rerun()

    # SECONDARY ACTION 3: Return to Hub
    with btn_col4:
        if st.button("Continue Learning →", key="practice_res_btn_return_hub", use_container_width=True):
            clear_practice_session()
            st.session_state["study_stage"] = "completed"
            st.rerun()


def render_practice_review(user: str):
    """Renders interactive review mode allowing student to review all questions & explanations."""
    state = get_practice_state()
    questions = state["questions"]
    answers = state["answers"]

    st.markdown(
        f"""
        <div style="background:#1E293B; padding:16px; border-radius:12px; color:white; margin-bottom:15px; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <h3 style="margin:0; color:#F8FAFC;">📖 Practice Review — {html.escape(state['display_title'])}</h3>
                <p style="margin:0; color:#94A3B8; font-size:0.85rem;">Review your choices, correct answers, and detailed explanations.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Back to Performance Summary", key="practice_review_back_btn"):
        st.session_state["practice_review_mode"] = False
        st.rerun()

    st.markdown("---")

    for idx, q_raw in enumerate(questions):
        q: NormalizedQuestion = UniversalQuestionAdapter.normalize(q_raw)
        ans_info = answers.get(idx, {})
        user_choice = ans_info.get("selected_option", "Not Answered")
        is_correct = ans_info.get("is_correct", False)

        status_badge = "🟢 Correct" if is_correct else "🔴 Incorrect / Skipped"
        st.markdown(
            f"""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; padding:14px; border-radius:10px; margin-bottom:12px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <b>Question {idx + 1} of {len(questions)}</b>
                    <span class="progress-pill">{status_badge}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_question_body(q=q, lang_mode="BOTH")
        render_explanation_card(q=q, prefix=f"review_{idx}", user_choice=user_choice)
        st.markdown("---")

    if st.button("⬅️ Back to Performance Summary", key="practice_review_back_bottom_btn", type="primary"):
        st.session_state["practice_review_mode"] = False
        st.rerun()
