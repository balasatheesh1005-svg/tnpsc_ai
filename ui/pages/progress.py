import pandas as pd
import streamlit as st

from core.progress_ai import get_progress, aggregate_topic_progress
from core.topics_loader import get_topic_metadata_by_id

__all__ = ["render_progress_page", "aggregate_topic_progress"]


def render_progress_page(section, user):
    section("📊 Progress Dashboard")

    progress = get_progress(user)
    if not progress:
        st.info("📭 No progress data recorded yet. Attempt a practice session or grand test in the Topic Hub to view your progress analytics!")
        return

    df = pd.DataFrame(progress)
    if df.empty or "accuracy" not in df.columns:
        st.warning("No progress records found.")
        return

    df["accuracy"] = pd.to_numeric(df["accuracy"], errors="coerce")
    df = df.dropna(subset=["accuracy"])
    if df.empty:
        st.warning("No valid progress records found.")
        return

    # Normalize metadata for records
    repo_titles = []
    part_titles = []
    subjects = []
    for _, row in df.iterrows():
        raw_subj = row.get("subject")
        subj = str(raw_subj if raw_subj is not None else "polity").lower().strip()
        if not subj:
            subj = "polity"
        subjects.append(subj)

        lookup = str(row.get("topic_id") or row.get("repository_id") or row.get("topic") or "").strip()
        meta = get_topic_metadata_by_id(subj, lookup)

        repo_basename = meta.get("repository_id") or lookup or "Topic"
        if repo_basename.startswith(f"{subj}_"):
            repo_basename = repo_basename[len(subj) + 1:]

        repo_titles.append(repo_basename.replace("_", " ").title())
        part_titles.append(meta.get("display_title") or repo_basename.replace("_", " ").title())

    df["subject"] = subjects
    df["repo_display"] = repo_titles
    df["part_display"] = part_titles

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📚 Active Topics", len(df.groupby(["subject", "repo_display"])))
    with col2:
        st.metric("📝 Total Tests Attempted", len(df))
    with col3:
        st.metric("🎯 Overall Average Accuracy", f"{round(float(df['accuracy'].mean()), 1)}%")

    st.markdown("---")

    # ---------------- 1. REPOSITORY PROGRESS (FULL TOPIC LEVEL) ----------------
    st.markdown("## 🏛️ Repository Level Progress")
    st.caption("Overall aggregated performance for complete practice repositories.")

    repo_avg = df.groupby(["subject", "repo_display"])["accuracy"].agg(["mean", "count"]).reset_index()
    repo_avg.columns = ["Subject", "Practice Repository", "Avg Accuracy (%)", "Tests Count"]
    repo_avg["Avg Accuracy (%)"] = repo_avg["Avg Accuracy (%)"].round(1)

    st.dataframe(repo_avg, use_container_width=True)

    # ---------------- 2. PART PROGRESS (NOTE PART LEVEL) ----------------
    st.markdown("## 📖 Part Level Breakdown")
    st.caption("Specific accuracy and completion state broken down by individual note parts.")

    part_avg = aggregate_topic_progress(df)

    st.dataframe(part_avg, use_container_width=True)

    # ---------------- ANALYSIS ----------------
    weak = part_avg[part_avg["Accuracy (%)"] < 50].sort_values(
        by=["Accuracy (%)", "Note Part"], ascending=[True, True]
    )
    strong = part_avg[part_avg["Accuracy (%)"] >= 75].sort_values(
        by=["Accuracy (%)", "Note Part"], ascending=[False, True]
    )

    c1, c2 = st.columns(2)
    with c1:
        st.error("🔻 Weak Topic Areas")
        if weak.empty:
            st.success("No critical weak areas identified!")
        else:
            for _, row in weak.iterrows():
                st.write(f"• **{row['Note Part']}** ({row['Accuracy (%)']}%)")

    with c2:
        st.success("💪 Strong Topic Areas")
        if strong.empty:
            st.info("Keep practicing to build your strong topic areas!")
        else:
            for _, row in strong.iterrows():
                st.write(f"• **{row['Note Part']}** ({row['Accuracy (%)']}%)")
