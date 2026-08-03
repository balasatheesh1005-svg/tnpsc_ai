import html

import pandas as pd
import streamlit as st
import altair as alt

from core.leaderboard_ai import get_top_users
from core.daily_mission_ai import claim_reward, get_mission_progress
from core.progress_ai import get_progress
from core.revision_scheduler import (
    get_due_revisions as get_queue_revisions,
    get_revision_count,
    get_revision_overview,
    get_top_due_revisions,
)
from core.test_topic_selector import get_test_config
from core.topics_loader import get_topics
from core.streak_ai import get_streak
from core.weakness_ai import get_weakness
from core.xp_ai import get_user_xp, get_level_progress, is_achievement_unlocked
from ui.components.cards import (
    accuracy_gauge,
    achievement_grid,
    analytics_grid,
    glass_card,
    glass_card_html,
    html_fragment,
    latest_achievement_single_card,
    mentor_personality_banner,
    metric_card,
    render_card_styles,
    section_title,
    study_plan_card_html,
)
from ui.components.header import render_dashboard_hero, render_header_styles
from core.mentor_ai import mentor_insights
from ui.theme import render_theme_css


def _to_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _clean_label(value, fallback="No Data"):
    if value is None or value == "":
        return fallback
    return str(value).replace("-", " -> ").title()


def _title_case_label(text: str) -> str:
    if not text:
        return "No Data"

    small_words = {
        "and",
        "or",
        "the",
        "a",
        "an",
        "in",
        "on",
        "at",
        "to",
        "for",
        "from",
        "by",
        "of",
        "with",
        "into",
        "over",
        "between",
    }

    words = str(text).replace("_", " ").replace("-", " ").split()
    formatted_words = []
    for index, word in enumerate(words):
        normalized = word.lower()
        if index != 0 and normalized in small_words:
            formatted_words.append(normalized)
        else:
            formatted_words.append(normalized.capitalize())

    return " ".join(formatted_words)


def format_topic_name(topic: str) -> str:
    return _title_case_label(topic)


def format_subject_name(subject: str) -> str:
    return _title_case_label(subject)


def _format_revision_label(row):
    subject = format_subject_name(row.get("subject"))
    topic = format_topic_name(row.get("topic"))
    return f"{subject} → {topic}"


def _date_label(due_date):
    today = pd.Timestamp.now(tz="UTC").date()
    if due_date == today:
        return "Today"
    if due_date < today:
        return "Overdue"
    return due_date.strftime("%b %d")


def _date_display(due_date):
    if due_date is None:
        return "No date"
    return due_date.strftime("%b %d")


def _render_revision_list_items(items, max_items=5):
    if not items:
        return (
            '<div class="revision-empty-state">'
            '<p class="nova-card-title">🎉 Great Job!</p>'
            '<p class="nova-card-copy">No revisions pending.</p>'
            "</div>"
        )

    list_html = '<div class="revision-list">'
    for row in items[:max_items]:
        due_date = row.get("next_due")
        due_label = _date_label(due_date)
        badge_type = (
            "today"
            if due_date == pd.Timestamp.now(tz="UTC").date()
            else (
                "overdue"
                if due_date < pd.Timestamp.now(tz="UTC").date()
                else "upcoming"
            )
        )
        list_html += (
            '<div class="revision-item">'
            f'<div class="revision-item-title">{html.escape(_format_revision_label(row))}</div>'
            '<div class="revision-item-meta">'
            f'<span class="revision-badge {badge_type}">{html.escape(due_label)}</span>'
            f'<span class="revision-badge">Level {html.escape(str(row.get("level", 1)))}</span>'
            "</div>"
            "</div>"
        )
    if len(items) > max_items:
        list_html += (
            '<div class="revision-item">'
            f'<p class="nova-card-copy">And {len(items) - max_items} more items in this queue.</p>'
            "</div>"
        )
    list_html += "</div>"
    return list_html


def _daily_mission_item(done, label, count=None, target=None):
    status = "✅" if done else "⬜"
    progress = ""
    if count is not None and target is not None:
        progress = f" ({min(count, target)}/{target})"

    return (
        '<div class="daily-mission-item">'
        f'<span class="daily-mission-status">{status}</span>'
        "<div>"
        f'<div class="daily-mission-label">{html.escape(label)}{html.escape(progress)}</div>'
        "</div>"
        "</div>"
    )


def _daily_mission_body_html(progress):
    revision_count = int(progress.get("revision_count") or 0)
    questions_answered = int(progress.get("questions_answered") or 0)
    completed_count = int(progress.get("completed_count") or 0)

    daily_done = bool(progress.get("daily_test_completed"))
    revision_done = revision_count >= 2
    questions_done = questions_answered >= 20

    mission_html = (
        '<div class="daily-mission-list">'
        + _daily_mission_item(daily_done, "Complete 1 Daily Test")
        + _daily_mission_item(revision_done, "Revise 2 Topics", revision_count, 2)
        + _daily_mission_item(
            questions_done, "Answer 20 Questions", questions_answered, 20
        )
        + "</div>"
        '<div class="daily-mission-footer">'
        f"<span>{completed_count} / 3 Completed</span>"
        "<span>🎁 +100 XP</span>"
        "</div>"
    )

    return mission_html


def _daily_mission_card_html(progress):
    mission_html = _daily_mission_body_html(progress)

    return glass_card_html(
        "🎯 Daily Mission",
        extra_html=html_fragment(mission_html),
    )


def _render_daily_mission_card(user, progress):
    completed_count = int(progress.get("completed_count") or 0)
    reward_claimed = bool(progress.get("reward_claimed"))
    can_claim = completed_count == 3 and not reward_claimed

    with st.container(border=True):
        st.markdown(
            (
                '<div class="nova-card-title">ðŸŽ¯ Daily Mission</div>'
                + _daily_mission_body_html(progress)
            ),
            unsafe_allow_html=True,
        )

        if st.session_state.pop("daily_mission_claim_success", False):
            st.success("🎉 Mission Completed\n\n+100 XP Earned\n\nAmazing consistency!")

        if reward_claimed:
            st.markdown(
                '<div class="daily-mission-claimed">✅ Reward Claimed</div>',
                unsafe_allow_html=True,
            )
        elif can_claim:
            if st.button("🏆 Claim Reward", key="daily_mission_claim_reward"):
                if claim_reward(user):
                    st.session_state["daily_mission_claim_success"] = True
                    st.rerun()
                else:
                    st.info("Reward already claimed or missions are not complete yet.")


def _render_next_topic_card(user):
    try:
        config = get_test_config(user, mode="smart")
        subject = config.get("subject", "polity")
        current_topic_key = config.get("topic", "")

        topics = get_topics(subject)
        normalized = [t.lower().replace(" ", "_") for t in topics]

        if current_topic_key in normalized:
            idx = normalized.index(current_topic_key)
            if idx + 1 < len(topics):
                next_topic_name = topics[idx + 1]
                glass_card(
                    "🎯 Recommended Next Topic",
                    value=next_topic_name,
                    body="Next topic in your learning path.",
                )
            else:
                glass_card(
                    "🏆 Subject Journey Completed",
                    value=subject.title(),
                    body="You have reached the final topic in this subject.",
                )
    except Exception:
        pass


def _build_progress_df(progress_rows):
    if not progress_rows:
        return pd.DataFrame(
            columns=["subject", "topic", "accuracy", "created_at", "test_no"]
        )

    df = pd.DataFrame(progress_rows).copy()

    if "subject" not in df.columns:
        df["subject"] = "Unknown"
    if "topic" not in df.columns:
        df["topic"] = "Unknown"
    if "accuracy" not in df.columns:
        df["accuracy"] = 0
    if "created_at" not in df.columns:
        df["created_at"] = pd.NaT

    df["accuracy"] = pd.to_numeric(df["accuracy"], errors="coerce").fillna(0)
    df["subject"] = df["subject"].fillna("Unknown").astype(str)
    df["topic"] = df["topic"].fillna("Unknown").astype(str)
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce", utc=True)
    df["test_no"] = range(1, len(df) + 1)

    if df["created_at"].notna().any():
        df = df.sort_values(["created_at", "test_no"], na_position="first")
        df["test_no"] = range(1, len(df) + 1)

    return df


def _get_subject_summary(df):
    if df.empty or "accuracy" not in df.columns:
        return "No Data", "No Data"

    subject_avg = df.groupby("subject")["accuracy"].mean().sort_values(ascending=False)
    if subject_avg.empty:
        return "No Data", "No Data"

    strongest = format_subject_name(subject_avg.index[0])
    weakest = format_subject_name(subject_avg.index[-1])
    return strongest, weakest


def _get_weekly_tests(df):
    if df.empty:
        return 0

    dated_df = df[df["created_at"].notna()]
    if dated_df.empty:
        return len(df)

    week_start = pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=7)
    return int((dated_df["created_at"] >= week_start).sum())


def _build_recommendation(accuracy, weak_subject, daily_streak):
    if weak_subject == "No Data":
        return "Complete a diagnostic test today so Nova AI can identify your highest priority topic."

    if accuracy < 50:
        return f"Focus on {weak_subject} basics today and complete due revisions before attempting a timed test."

    if accuracy < 75:
        return f"Revise {weak_subject}, then take a short practice set to push your accuracy above 75%."

    if daily_streak < 3:
        return f"Keep your streak alive with one focused {weak_subject} revision session today."

    return f"Great momentum. Strengthen {weak_subject} with mixed practice and review every missed question."


def render_dashboard():
    # ---------- DATA EXTRACTION FROM REUSED ENGINES ----------
    user = st.session_state.get("username", "")
    notes_completed = len(st.session_state.get("completed_notes", []))
    tests_attempted = st.session_state.get("tests_attempted", 0)
    accuracy = st.session_state.get("accuracy", 0)
    daily_streak = st.session_state.get("streak", 0)
    rank = st.session_state.get("rank", 0)
    tests_attempted_value = int(_to_float(tests_attempted))
    daily_streak_value = int(_to_float(daily_streak))
    rank_value = int(_to_float(rank))

    # Reused XP & Level Engine
    xp_data = get_user_xp(user)
    level_progress = get_level_progress(user)
    current_level = xp_data["level"]
    current_xp = xp_data["xp"]

    # Reused Mission Engine
    mission_progress = get_mission_progress(user)

    # Reused Weakness Engine
    weak_data = get_weakness(user)
    if weak_data:
        weak_topic = max(weak_data, key=weak_data.get)
        if "-" in weak_topic:
            raw_subject, raw_topic = weak_topic.split("-", 1)
            weak_subject = f"{format_subject_name(raw_subject)} → {format_topic_name(raw_topic)}"
        else:
            weak_subject = format_topic_name(weak_topic)
    else:
        weak_subject = "No Data"

    # Reused Progress Engine
    progress_rows = get_progress(user)
    progress_df = _build_progress_df(progress_rows)
    accuracy_value = max(0.0, min(100.0, _to_float(accuracy)))
    strongest_subject, weakest_progress_subject = _get_subject_summary(progress_df)
    tests_this_week = _get_weekly_tests(progress_df)
    average_score = round(progress_df["accuracy"].mean(), 1) if not progress_df.empty else 0

    chart_df = progress_df[["test_no", "accuracy"]].copy()
    latest_chart_df = chart_df.tail(10).reset_index(drop=True)
    if not latest_chart_df.empty:
        latest_chart_df = latest_chart_df.sort_values("test_no")
        current_accuracy = latest_chart_df["accuracy"].iloc[-1]
        best_accuracy = latest_chart_df["accuracy"].max()
        average_accuracy = latest_chart_df["accuracy"].mean()
    else:
        current_accuracy = 0
        best_accuracy = 0
        average_accuracy = 0

    # Reused Revision Engine
    revision_data = get_revision_overview(user)
    due_today_count = len(revision_data.get("due_today", []))
    overdue_count = len(revision_data.get("overdue", []))
    total_due_count = due_today_count + overdue_count

    # Reused Achievements Engine
    achievements = [
        ("7 Day Streak", "Maintain a 7 day study streak.", daily_streak_value >= 7, "gold"),
        ("Accuracy Above 80%", "Reach 80% average accuracy.", accuracy_value >= 80, "silver"),
        ("10 Tests Completed", "Complete 10 practice tests.", tests_attempted_value >= 10, "bronze"),
        ("50 Tests Completed", "Complete 50 practice tests.", tests_attempted_value >= 50, "gold"),
        ("Top 10 Rank", "Enter the leaderboard top 10.", 0 < rank_value <= 10, "gold"),
        ("🌟 Level 2", "Reach Level 2 mastery.", is_achievement_unlocked(user, "level_2"), "silver"),
        ("⭐ Level 5", "Reach Level 5 mastery.", is_achievement_unlocked(user, "level_5"), "gold"),
        ("🌠 Level 10", "Reach Level 10 mastery.", is_achievement_unlocked(user, "level_10"), "gold"),
    ]
    unlocked_achievements = [a for a in achievements if a[2]]
    latest_achievement = unlocked_achievements[-1] if unlocked_achievements else None

    from core.performance import start_timer, end_timer, record_render

    # ---------- RENDER THEMES & STYLES ----------
    start_timer("Header")
    render_theme_css()
    render_header_styles()
    render_card_styles()

    # ---------- PERSONALITY: ONE MENTOR MESSAGE ----------
    if daily_streak_value >= 7:
        mentor_msg = "Excellent consistency."
    elif tests_attempted_value >= 20:
        mentor_msg = "Only two repositories remain."
    elif accuracy_value >= 80:
        mentor_msg = "Today is perfect for Grand Test."
    elif daily_streak_value >= 1:
        mentor_msg = "Keep your streak alive."
    else:
        mentor_msg = "Focus on your weakest subject today to boost overall accuracy."

    st.html(mentor_personality_banner(mentor_msg).markup)

    # ---------- HERO TITLE & SUMMARY ----------
    render_dashboard_hero(user, rank_value, accuracy_value, daily_streak_value)
    record_render("Header", end_timer("Header"))

    # ---------- 8 MANDATORY DASHBOARD CARDS ----------
    start_timer("Hero Cards")
    section_title("Personalized Learning Intelligence", "What should I study today?")


    # 1. Today's Recommendation
    if total_due_count > 0:
        top_due = revision_data["due_today"][0] if revision_data["due_today"] else revision_data["overdue"][0]
        rec_title = f"📖 Revise {format_topic_name(top_due.get('topic', 'Topic'))}"
        rec_body = f"Scheduled for today in Spaced Repetition queue ({total_due_count} topics pending)."
    elif weak_subject != "No Data":
        rec_title = f"📝 Continue {weak_subject}"
        rec_body = "Target your highest weakness topic to boost overall accuracy."
    else:
        rec_title = "🏆 Attempt Grand Test"
        rec_body = "Outstanding consistency! Take a full Grand Test to challenge mastery."

    # 2. Today's Goal
    try:
        smart_cfg = get_test_config(user, mode="smart")
        goal_title_text = f"Complete {format_subject_name(smart_cfg.get('subject', 'Polity'))}"
    except Exception:
        goal_title_text = "Complete Hard Repository"
    goal_time_text = "Estimated 20 Minutes"

    # Row 1: Recommendation & Goal
    col_rec, col_goal = st.columns([1, 1], gap="small")
    with col_rec:
        glass_card(
            "📖 Today's Recommendation",
            value=rec_title,
            body=rec_body,
        )
    with col_goal:
        glass_card(
            "🎯 Today's Goal",
            value=goal_title_text,
            body=f"⏱️ {goal_time_text} • Based on repository progress",
        )

    # Row 2: Weakest, Strongest, Revision Due
    col_weak, col_strong, col_rev = st.columns([1, 1, 1], gap="small")
    with col_weak:
        glass_card(
            "⚠️ Weakest Subject",
            value=weak_subject if weak_subject != "No Data" else "No Major Weakness",
            body=f"Accuracy: {average_score:g}% (Reuse Weakness Engine)" if weak_subject != "No Data" else "Complete diagnostic test",
        )
    with col_strong:
        glass_card(
            "💪 Strongest Subject",
            value=strongest_subject if strongest_subject != "No Data" else "Building Strength",
            body=f"Accuracy: {best_accuracy:g}% (Reuse Progress data)" if strongest_subject != "No Data" else "Keep practicing tests",
        )
    with col_rev:
        glass_card(
            "📅 Revision Due",
            value=f"{total_due_count} Topics",
            body="Scheduled Today (Reuse Revision Engine)",
        )

    # Row 3: Daily Mission, Current Streak, Latest Achievement
    col_mission, col_streak, col_achieve = st.columns([1, 1, 1], gap="small")
    with col_mission:
        _render_daily_mission_card(user, mission_progress)
    with col_streak:
        glass_card(
            "🔥 Current Streak",
            value=f"{daily_streak_value} Days",
            body="Reuse Streak Engine • Daily momentum",
        )
    with col_achieve:
        if latest_achievement:
            st.html(latest_achievement_single_card(latest_achievement[0], latest_achievement[1], latest_achievement[3]).markup)
        else:
            glass_card(
                "🏆 Latest Achievement",
                value="First Step",
                body="Complete your first test to unlock achievements!",
            )
    record_render("Hero Cards", end_timer("Hero Cards"))

    # ---------- DEFERRED / LAZY LOADED ANALYTICS & STRATEGY ----------
    start_timer("Revision Panel")
    with st.expander("📊 Detailed Revision Queue, Charts & Mentor Strategy", expanded=False):
        section_title("Smart Revision Scheduler", "Due Today · Overdue · Upcoming")

        scheduler_html = (
            '<div class="revision-grid">'
            + glass_card_html(
                "📅 Due Today",
                value=due_today_count,
                body="High-priority revisions scheduled for today.",
                extra_html=html_fragment(
                    _render_revision_list_items(revision_data["due_today"])
                ),
            )
            + glass_card_html(
                "⏳ Overdue",
                value=overdue_count,
                body="Topics that need immediate review.",
                extra_html=html_fragment(
                    _render_revision_list_items(revision_data["overdue"])
                ),
            )
            + glass_card_html(
                "🔮 Upcoming",
                value=len(revision_data["upcoming"]),
                body="What is next in your spaced repetition queue.",
                extra_html=html_fragment(
                    _render_revision_list_items(revision_data["upcoming"])
                ),
            )
            + "</div>"
        )
        st.html(scheduler_html)

        section_title("Progress Analytics", "Accuracy trend & history")
        with st.container(border=True):
            st.markdown("#### 📈 Accuracy Trend")
            if latest_chart_df.empty:
                st.info("No users_progress records yet. Complete a test to unlock your trend chart.")
            else:
                st.html(
                    analytics_grid(
                        [
                            ("Current Accuracy", f"{current_accuracy:g}%"),
                            ("Best Accuracy", f"{best_accuracy:g}%"),
                            ("Average Accuracy", f"{average_accuracy:g}%"),
                        ]
                    ).markup
                )
                line = (
                    alt.Chart(latest_chart_df)
                    .mark_line(interpolate="monotone", color="#2563EB", strokeWidth=3)
                    .encode(
                        x=alt.X("test_no:Q", title="Test #", axis=alt.Axis(tickMinStep=1)),
                        y=alt.Y("accuracy:Q", title="Accuracy", scale=alt.Scale(domain=[0, 100])),
                        tooltip=[
                            alt.Tooltip("test_no:Q", title="Test Number"),
                            alt.Tooltip("accuracy:Q", title="Accuracy", format=".1f"),
                        ],
                    )
                )
                area = (
                    alt.Chart(latest_chart_df)
                    .mark_area(interpolate="monotone", opacity=0.16, color="#3B82F6")
                    .encode(x="test_no:Q", y="accuracy:Q")
                )
                target_line = (
                    alt.Chart(pd.DataFrame({"target": [75]}))
                    .mark_rule(color="#2563EB", strokeDash=[4, 4], size=2)
                    .encode(y="target:Q")
                )
                chart = alt.layer(area, line, target_line).properties(height=280, width="container").configure_view(strokeOpacity=0)
                st.altair_chart(chart, use_container_width=True)

        mentor_data = mentor_insights(
            accuracy_value,
            daily_streak_value,
            weak_subject,
            strongest_subject,
            tests_attempted_value,
            due_revisions=len(revision_data.get("due_today", [])),
        )
        mentor_html = study_plan_card_html(
            "🧠 Personal Mentor Strategy",
            revision=mentor_data["revision"],
            practice=mentor_data["practice"],
            goal=mentor_data["goal"],
            estimated_time=mentor_data["time"],
            message=mentor_data["message"],
        )
        st.html(mentor_html)
    record_render("Revision Panel", end_timer("Revision Panel"))

