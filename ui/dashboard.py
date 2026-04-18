import streamlit as st
from core.streak_ai import get_streak
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.revision_ai import get_revision_topics
from core.leaderboard_ai import get_top_users
import pandas as pd


def show_dashboard(user):

    # ---------------- HEADER ----------------
    st.markdown(
        f"""
    <div style="
    background: linear-gradient(90deg, #667eea, #764ba2);
    padding:20px;
    border-radius:15px;
    color:white;
    ">
    <h2>👋 Welcome, {user}</h2>
    <p>Your AI-powered TNPSC preparation dashboard</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("## 📊 Overview")

    col1, col2, col3 = st.columns(3)

    # ---------------- STREAK ----------------
    with col1:
        streak = get_streak(user)

        st.markdown(
            f"""
        <div style="
        background:#ff5e62;
        padding:15px;
        border-radius:12px;
        color:white;
        text-align:center;
        ">
        🔥 <h3>{streak}</h3>
        <p>Day Streak</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # ---------------- PROGRESS ----------------
    with col2:
        progress = get_progress(user)

        total_scores = []
        for scores in progress.values():
            total_scores.extend(scores)

        avg = int(sum(total_scores) / len(total_scores)) if total_scores else 0

        st.markdown(
            f"""
        <div style="
        background:#43cea2;
        padding:15px;
        border-radius:12px;
        color:white;
        text-align:center;
        ">
        📊 <h3>{avg}%</h3>
        <p>Avg Score</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # ---------------- WEAKNESS COUNT ----------------
    with col3:
        weak = get_weakness(user)
        total_weak = sum(weak.values()) if weak else 0

        st.markdown(
            f"""
        <div style="
        background:#ff4d4d;
        padding:15px;
        border-radius:12px;
        color:white;
        text-align:center;
        ">
        🧠 <h3>{total_weak}</h3>
        <p>Weak Areas</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ---------------- CHART + WEAKNESS ----------------
    col1, col2 = st.columns(2)

    # 📊 Progress Chart
    with col1:
        st.subheader("📊 Subject Performance")

        progress = get_progress(user)

        if progress:
            df_data = []
            for subject, scores in progress.items():
                avg = sum(scores) / len(scores)
                df_data.append({"Subject": subject, "Score": avg})

            df = pd.DataFrame(df_data)
            st.bar_chart(df.set_index("Subject"))
        else:
            st.info("No progress data")


# 🧠 Weakness Heatmap
def color_map(val):
    if val >= 5:
        return "background-color: #ff4d4d; color:white"
    elif val >= 3:
        return "background-color: #ffa64d"
    elif val >= 1:
        return "background-color: #ffff99"
    return ""


with col2:
    st.markdown("## 🧠 Weakness Heatmap")

weak_data = get_weakness(user)

if not weak_data:
    st.success("🔥 No Weakness!")
else:

    for topic, count in weak_data.items():

        if count >= 10:
            color = "#ff0000"  # 🔴 high danger
        elif count >= 5:
            color = "#ff6b6b"  # 🟥
        elif count >= 2:
            color = "#ffc107"  # 🟨
        else:
            color = "#28a745"  # 🟩

        st.markdown(
            f"""
        <div style="
        background:{color};
        padding:12px;
        border-radius:10px;
        margin-bottom:10px;
        color:white;
        font-weight:bold;
        ">
        📘 {topic} → {count}
        </div>
        """,
            unsafe_allow_html=True,
        )
        import pandas as pd

    df = pd.DataFrame(list(weak_data.items()), columns=["Topic", "Weakness"])
    st.dataframe(df.style.background_gradient(cmap="Reds"))
    # ---------------- REVISION + LEADERBOARD ----------------
    col1, col2 = st.columns(2)

    # 🔁 Revision
    with col1:
        st.subheader("🔁 Smart Revision")

        rev = get_revision_topics(user)

        if not rev:
            st.success("All clear 🔥")
        else:
            for t in rev[:5]:
                st.write(f"🔁 {t}")

    # 🏆 Leaderboard
    with col2:
        st.subheader("🏆 Top Performers")

        leaders = get_top_users()

        for i, (u, s) in enumerate(leaders[:5], 1):

            if u == user:
                st.success(f"⭐ {i}. {u} → {int(s)}%")
            else:
                st.write(f"{i}. {u} → {int(s)}%")
