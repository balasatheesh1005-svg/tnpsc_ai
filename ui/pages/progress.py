import pandas as pd
import streamlit as st

from core.progress_ai import get_progress
from core.topics_loader import get_topic_metadata_by_id


def render_progress_page(section, user):
    section("📊 Progress Dashboard")

    progress = get_progress(user)
    if not progress:
        st.info("📭 No progress data recorded yet. Attempt a practice session or grand test in the Topic Hub to view your progress analytics!")
        return

    df = pd.DataFrame(progress)
    if df.empty:
        st.warning("No progress records found.")
        return

    # Normalize metadata for records
    repo_titles = []
    part_titles = []
    for _, row in df.iterrows():
        subj = str(row.get("subject", "polity"))
        lookup = row.get("topic_id") or row.get("repository_id") or row.get("topic", "")
        meta = get_topic_metadata_by_id(subj, lookup)

        repo_basename = meta["repository_id"]
        if repo_basename.startswith(f"{subj}_"):
            repo_basename = repo_basename[len(subj) + 1:]

        repo_titles.append(repo_basename.replace("_", " ").title())
        part_titles.append(meta["display_title"])

    df["repo_display"] = repo_titles
    df["part_display"] = part_titles

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📚 Active Topics", len(df["repo_display"].unique()))
    with col2:
        st.metric("📝 Total Tests Attempted", len(df))
    with col3:
        st.metric("🎯 Overall Average Accuracy", f"{round(df['accuracy'].mean(), 1)}%")

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

    part_avg = df.groupby(["subject", "repo_display", "part_display"])["accuracy"].agg(["mean", "count"]).reset_index()
    part_avg.columns = ["Subject", "Repository", "Note Part", "Accuracy (%)", "Attempts"]
    part_avg["Accuracy (%)"] = part_avg["Accuracy (%)"].round(1)

    st.dataframe(part_avg, use_container_width=True)

    # ---------------- ANALYSIS ----------------
    weak = df[df["accuracy"] < 50]
    strong = df[df["accuracy"] >= 75]

    c1, c2 = st.columns(2)
    with c1:
        st.error("🔻 Weak Topic Areas")
        if weak.empty:
            st.success("No critical weak areas identified!")
        else:
            for _, row in weak.iterrows():
                st.write(f"• **{row['part_display']}** ({row['accuracy']}%)")

    with c2:
        st.success("💪 Strong Topic Areas")
        if strong.empty:
            st.info("Keep practicing to build your strong topic areas!")
        else:
            for _, row in strong.iterrows():
                st.write(f"• **{row['part_display']}** ({row['accuracy']}%)")
