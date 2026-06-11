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
    # ---------- EXISTING DASHBOARD DATA ----------
    user = st.session_state.get("username", "")
    notes_completed = len(st.session_state.get("completed_notes", []))
    tests_attempted = st.session_state.get("tests_attempted", 0)
    accuracy = st.session_state.get("accuracy", 0)
    daily_streak = st.session_state.get("streak", 0)
    rank = st.session_state.get("rank", 0)
    tests_attempted_value = int(_to_float(tests_attempted))
    daily_streak_value = int(_to_float(daily_streak))
    rank_value = int(_to_float(rank))

    # ---------- XP & LEVEL DATA ----------
    xp_data = get_user_xp(user)
    level_progress = get_level_progress(user)
    current_level = xp_data["level"]
    current_xp = xp_data["xp"]
    xp_for_next = level_progress["xp_for_next"]
    progress_percent = level_progress["progress_percent"]
    mission_progress = get_mission_progress(user)

    weak_data = get_weakness(user)
    progress_rows = get_progress(user)
    progress_df = _build_progress_df(progress_rows)

    if weak_data:
        weak_topic = max(weak_data, key=weak_data.get)
        if "-" in weak_topic:
            raw_subject, raw_topic = weak_topic.split("-", 1)
            weak_subject = (
                f"{format_subject_name(raw_subject)} → {format_topic_name(raw_topic)}"
            )
        else:
            weak_subject = format_topic_name(weak_topic)
    else:
        weak_subject = "No Data"

    accuracy_value = max(0, min(100, _to_float(accuracy)))
    strongest_subject, weakest_progress_subject = _get_subject_summary(progress_df)
    tests_this_week = _get_weekly_tests(progress_df)
    average_score = (
        round(progress_df["accuracy"].mean(), 1) if not progress_df.empty else 0
    )
    recommendation = _build_recommendation(
        accuracy_value, weak_subject, daily_streak_value
    )

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

    achievements = [
        (
            "7 Day Streak",
            "Maintain a 7 day study streak.",
            daily_streak_value >= 7,
            "gold",
        ),
        (
            "Accuracy Above 80%",
            "Reach 80% average accuracy.",
            accuracy_value >= 80,
            "silver",
        ),
        (
            "10 Tests Completed",
            "Complete 10 practice tests.",
            tests_attempted_value >= 10,
            "bronze",
        ),
        (
            "50 Tests Completed",
            "Complete 50 practice tests.",
            tests_attempted_value >= 50,
            "gold",
        ),
        ("Top 10 Rank", "Enter the leaderboard top 10.", 0 < rank_value <= 10, "gold"),
        (
            "🌟 Level 2",
            "Reach Level 2 mastery.",
            is_achievement_unlocked(user, "level_2"),
            "silver",
        ),
        (
            "⭐ Level 5",
            "Reach Level 5 mastery.",
            is_achievement_unlocked(user, "level_5"),
            "gold",
        ),
        (
            "🌠 Level 10",
            "Reach Level 10 mastery.",
            is_achievement_unlocked(user, "level_10"),
            "gold",
        ),
    ]
    unlocked_count = sum(
        1 for _title, _description, unlocked, _level in achievements if unlocked
    )

    render_theme_css()
    render_header_styles()
    render_card_styles()

    with st.spinner("⏳ Loading Mentor Insights..."):
        render_dashboard_hero(user, rank_value, accuracy_value, daily_streak_value)

    if not progress_rows and not weak_data:
        glass_card(
            "ðŸŒ± No Data Yet",
            value="Start your first test",
            body="Your dashboard insights will appear here after you complete practice.",
        )

    section_title("Your Performance", "Live stats")
    metric_rows = [
        [
            ("streak", "🔥 Streak", f"{daily_streak_value} days", "Daily consistency"),
            ("accuracy", "🎯 Accuracy", f"{accuracy_value:g}%", "Practice quality"),
        ],
        [
            (
                "rank",
                "🏆 Rank",
                f"#{rank_value}" if rank_value else "Not ranked",
                "Leaderboard",
            ),
            ("tests", "📚 Tests Attempted", tests_attempted_value, "Mock practice"),
        ],
    ]

    for row in metric_rows:
        col1, col2 = st.columns(2, gap="small")
        for col, (theme, label, value, delta) in zip((col1, col2), row):
            with col:
                metric_card(theme, label, value, delta)

    col_focus, col_gauge = st.columns([1, 1], gap="small")
    with col_focus:
        glass_card(
            "🎯 Today's Focus",
            value=weak_subject,
            body="Highest weakness topic from your current dashboard data.",
        )

    with col_gauge:
        glass_card(
            "🧭 Accuracy Gauge",
            extra_html=accuracy_gauge(
                accuracy_value,
                "Current average accuracy from your dashboard performance.",
            ),
        )

    col_next, col_xp, col_mission = st.columns(3, gap="small")
    with col_next:
        _render_next_topic_card(user)

    with col_xp:
        xp_card_html = (
            '<div style="'
            "background: linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(245, 158, 11, 0.1) 100%);"
            "border: 1.5px solid rgba(245, 158, 11, 0.3);"
            "border-radius: 18px;"
            "padding: 24px;"
            "backdrop-filter: blur(14px);"
            "position: relative;"
            'overflow: hidden;">'
            '<div style="position: absolute; top: -40px; right: -40px; width: 120px; height: 120px; '
            "background: radial-gradient(circle, rgba(251, 191, 36, 0.15) 0%, transparent 70%);"
            'border-radius: 50%; pointer-events: none;"></div>'
            '<div style="position: relative; z-index: 2;">'
            '<p style="color: rgba(79, 70, 229, 0.7); font-size: 0.9rem; font-weight: 600; margin: 0 0 8px 0;">⭐ XP & LEVEL</p>'
            f'<p style="color: #1f2937; font-size: 2rem; font-weight: 900; margin: 0 0 4px 0;">Level {current_level}</p>'
            f'<p style="color: rgba(79, 70, 229, 0.8); font-size: 0.95rem; margin: 12px 0 16px 0;">📊 {current_xp} / {level_progress["next_level_target"]} XP</p>'
            '<div style="background: rgba(255, 255, 255, 0.4); border-radius: 999px; height: 8px; margin: 12px 0; overflow: hidden;">'
            f'<div style="background: linear-gradient(90deg, #fbbf24 0%, #f59e0b 100%); width: {progress_percent}%; height: 100%; border-radius: 999px;"></div>'
            "</div>"
            f'<p style="color: rgba(79, 70, 229, 0.7); font-size: 0.85rem; margin: 8px 0 0 0;">➜ {xp_for_next} XP to Level {level_progress["next_level"]}</p>'
            "</div>"
            "</div>"
        )
        st.html(xp_card_html)

    with col_mission:
        _render_daily_mission_card(user, mission_progress)

    due_revisions = get_queue_revisions(user)
    revision_data = get_revision_overview(user)
    due_count = get_revision_count(user)
    overdue_count = len(revision_data["overdue"])
    due_today_count = len(revision_data["due_today"])
    upcoming_count = len(revision_data["upcoming"])
    total_queue = revision_data["total"]

    next_item = revision_data["queue"][0] if revision_data["queue"] else None
    next_due_text = (
        _date_label(next_item["next_due"]) if next_item else "No upcoming revisions"
    )
    next_topic_text = (
        _format_revision_label(next_item) if next_item else "All caught up"
    )

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
            value=upcoming_count,
            body="What is next in your spaced repetition queue.",
            extra_html=html_fragment(
                _render_revision_list_items(revision_data["upcoming"])
            ),
        )
        + "</div>"
    )
    st.html(scheduler_html)

    queue_html = glass_card_html(
        "📚 Revision Queue",
        value=total_queue,
        body="Pending Revisions",
        extra_html=html_fragment(
            '<p class="nova-card-copy">🔥 Keep your weak topics fresh</p>'
            + _render_revision_list_items(revision_data["queue"], max_items=6)
        ),
    )
    st.html(queue_html)

    dashboard_revision_html = glass_card_html(
        "📅 Next Revision",
        value=html.escape(next_topic_text),
        body=(
            f"🗓 Due: {html.escape(_date_display(next_item['next_due']))}"
            if next_item
            else "🎉 No revisions pending"
        ),
        extra_html=html_fragment(
            (
                f'<p class="nova-card-copy">⭐ Level {html.escape(str(next_item["level"]))}</p>'
                '<a class="revision-start-button">🚀 Start Revision</a>'
                if next_item
                else ""
            )
        ),
    )
    st.html(dashboard_revision_html)

    section_title("Progress Overview", "Accuracy trend")
    with st.container(border=True):
        st.markdown("#### 📈 Accuracy Trend")
        if latest_chart_df.empty:
            st.info(
                "No users_progress records yet. Complete a test to unlock your trend chart."
            )
        else:
            st.markdown("#### 📊 Trend Summary")
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
                .mark_line(
                    interpolate="monotone",
                    color="#2563EB",
                    strokeWidth=3,
                )
                .encode(
                    x=alt.X("test_no:Q", title="Test #", axis=alt.Axis(tickMinStep=1)),
                    y=alt.Y(
                        "accuracy:Q",
                        title="Accuracy",
                        scale=alt.Scale(domain=[0, 100]),
                    ),
                    tooltip=[
                        alt.Tooltip("test_no:Q", title="Test Number"),
                        alt.Tooltip("accuracy:Q", title="Accuracy", format=".1f"),
                    ],
                )
            )

            area = (
                alt.Chart(latest_chart_df)
                .mark_area(
                    interpolate="monotone",
                    opacity=0.16,
                    color="#3B82F6",
                )
                .encode(
                    x="test_no:Q",
                    y="accuracy:Q",
                )
            )

            target_line = (
                alt.Chart(pd.DataFrame({"target": [75]}))
                .mark_rule(
                    color="#2563EB",
                    strokeDash=[4, 4],
                    size=2,
                )
                .encode(y="target:Q")
            )

            chart = (
                alt.layer(area, line, target_line)
                .properties(
                    height=300,
                    width="container",
                )
                .configure_view(strokeOpacity=0)
            )

            st.altair_chart(chart, use_container_width=True)

    analytics_html = glass_card_html(
        "📊 Weekly Analytics",
        extra_html=analytics_grid(
            [
                ("Tests This Week", tests_this_week),
                ("Average Score", f"{average_score:g}%"),
                ("Best Subject", strongest_subject),
                ("Weakest Subject", weakest_progress_subject),
            ]
        ),
    )
    st.html(analytics_html)

    col_subject, col_consistency = st.columns([1, 1], gap="small")
    with col_subject:
        glass_card(
            "💪 Strongest Subject",
            value=strongest_subject,
            body="Based on highest average accuracy in users_progress.",
        )

    with col_consistency:
        consistency_note = (
            "Excellent consistency. Keep protecting this streak."
            if daily_streak_value >= 7
            else "Build toward a 7 day streak with one focused session daily."
        )
        glass_card(
            "🔥 Study Consistency",
            value=f"{daily_streak_value} days",
            body=consistency_note,
            extra_html=html_fragment(
                '<div class="mini-stat">'
                f'<p class="nova-card-copy">Tests completed: {tests_attempted_value}</p>'
                f'<p class="nova-card-copy">Notes completed: {notes_completed}</p>'
                "</div>"
            ),
        )

    mentor_data = mentor_insights(
        accuracy_value,
        daily_streak_value,
        weak_subject,
        strongest_subject,
        tests_attempted_value,
        due_revisions=len(due_revisions),
    )

    mentor_html = study_plan_card_html(
        "🧠 Personal Mentor",
        revision=mentor_data["revision"],
        practice=mentor_data["practice"],
        goal=mentor_data["goal"],
        estimated_time=mentor_data["time"],
        message=mentor_data["message"],
    )
    st.html(mentor_html)

    achievement_html = glass_card_html(
        "🏅 Achievements",
        body=f"{unlocked_count} of {len(achievements)} unlocked",
        extra_html=achievement_grid(achievements),
    )
    st.html(achievement_html)

    revision_text = (
        f"Review {weak_subject} and complete high-priority revisions."
        if weak_subject != "No Data"
        else "Complete a diagnostic test and prioritize your revision plan."
    )
    recommendation_html = study_plan_card_html(
        "🧠 AI Study Plan",
        revision=revision_text,
        practice="Take a Short Daily Test",
        goal="Reach 75%+ Accuracy",
        estimated_time="15 Minutes",
        raw_recommendation=recommendation,
    )
    st.html(recommendation_html)
