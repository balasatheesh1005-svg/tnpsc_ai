import pandas as pd
import streamlit as st

from core.progress_ai import get_progress


def render_progress_page(section, user):
    section("📊 Progress Dashboard")

    progress = get_progress(user)

    if not progress:

        st.info("📭 No progress data yet")

        st.stop()

    # ---------------- DATAFRAME ----------------

    df = pd.DataFrame(progress)

    if df.empty:

        st.warning("No progress found")

        st.stop()

    # ---------------- CLEAN ----------------

    df["topic"] = df["topic"].str.replace("_", " ").str.title()

    # ---------------- STATS ----------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric("📚 Topics", len(df))

    with col2:

        st.metric("📝 Tests", len(df))

    with col3:

        st.metric("🎯 Avg Accuracy", f"{round(df['accuracy'].mean(),1)}%")

    # ---------------- SUBJECT PERFORMANCE ----------------

    st.markdown("## 📊 Subject Performance")

    subject_avg = df.groupby("subject")["accuracy"].mean().sort_values(ascending=False)

    st.bar_chart(subject_avg)

    # ---------------- TABLE ----------------

    st.markdown("## 📘 Topic Wise Progress")

    st.dataframe(
        df[["subject", "topic", "accuracy", "created_at"]], use_container_width=True
    )

    # ---------------- ANALYSIS ----------------

    weak = df[df["accuracy"] < 50]

    strong = df[df["accuracy"] >= 75]

    c1, c2 = st.columns(2)

    with c1:

        st.error("🔻 Weak Areas")

        if weak.empty:

            st.success("None")

        else:

            for _, row in weak.iterrows():

                st.write(f"• {row['topic']} " f"({row['accuracy']}%)")

    with c2:

        st.success("💪 Strong Areas")

        if strong.empty:

            st.info("None")

        else:

            for _, row in strong.iterrows():

                st.write(
                    f"• {row['topic']} " f"({row['accuracy']}%)"
                )
