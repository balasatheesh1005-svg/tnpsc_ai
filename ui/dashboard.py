import html

import pandas as pd
import streamlit as st
import altair as alt

from core.leaderboard_ai import get_top_users
from core.progress_ai import get_progress
from core.revision_ai import get_revision_topics
from core.streak_ai import get_streak
from core.weakness_ai import get_weakness
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
    ]
    unlocked_count = sum(
        1 for _title, _description, unlocked, _level in achievements if unlocked
    )

    render_theme_css()
    render_header_styles()
    render_card_styles()

    render_dashboard_hero(user, rank_value, accuracy_value, daily_streak_value)

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
