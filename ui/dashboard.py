import streamlit as st
import streamlit as st
from core.streak_ai import get_streak
from core.progress_ai import get_progress
from core.weakness_ai import get_weakness
from core.revision_ai import get_revision_topics
from core.leaderboard_ai import get_top_users
import pandas as pd


def render_dashboard():

    # ---------- SAMPLE DATA ----------
    user = st.session_state.get("username", "")
    notes_completed = len(st.session_state.get("completed_notes", []))

    tests_attempted = st.session_state.get("tests_attempted", 0)

    accuracy = st.session_state.get("accuracy", 0)

    daily_streak = st.session_state.get("streak", 0)

    rank = st.session_state.get("rank", 0)

    from core.weakness_ai import get_weakness

    weak_data = get_weakness(user)

    if weak_data:

        weak_topic = max(weak_data, key=weak_data.get)

        weak_subject = weak_topic.replace("-", " → ")

    else:

        weak_subject = "No Data"
    # ---------- CUSTOM CSS ----------
    st.markdown(
        """
    <style>
    .card {
    padding: 18px;
    border-radius: 16px;
    background: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    text-align: center;
    margin-bottom: 15px;
    width: 100%;
    }

    .card-title {
        font-size: 18px;
        color: #666;
        margin-bottom: 10px;
    }

    .card-value {
        font-size: 24px;
        font-weight: bold;
        color: #111;
    }
    .card:hover {
    transform: translateY(-5px);
    transition: 0.3s;
    }
    .stButton > button {
    width: 100%;
    border-radius: 10px;
    }
    .main-title {
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #666;
        margin-bottom: 30px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # ---------- HERO SECTION ----------
    st.image("assets/logo.png", width=250)
    st.markdown(
        """
        <div class='main-title'>TNPSC Nova AI</div>
        <div class='sub-title'>
            Learn Smarter • Rank Faster • Powered by AI
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <div style="
    padding:18px;
    border-radius:15px;
    background: linear-gradient(90deg, #1e3c72, #2a5298);
    color:white;
    margin-bottom:25px;
    ">

    <h3 style='font-size:22px;'>
    🚀 India's No.1 AI Powered TNPSC Preparation Platform
    </h3>

    <p style='font-size:14px;'>
    Daily Tests • Smart Notes • Weakness Analysis • AI Mentor
    </p>

    </div>
    """,
        unsafe_allow_html=True,
    )
    # ---------- ROW 1 ----------
    (
        col1,
        col2,
    ) = st.columns(2)

    with col1:
        st.markdown(
            f"""
        <div class="card">
            <div class="card-title">📘 Notes Completed</div>
            <div class="card-value">{notes_completed}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="card">
            <div class="card-title">📝 Tests Attempted</div>
            <div class="card-value">{tests_attempted}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # ---------- ROW 2 ----------
    (
        col3,
        col4,
    ) = st.columns(2)

    with col3:
        st.markdown(
            f"""
        <div class="card">
            <div class="card-title">🎯 Accuracy</div>
            <div class="card-value">{accuracy}%</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
        <div class="card">
            <div class="card-title">🔥 Daily Streak</div>
            <div class="card-value">{daily_streak}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    (
        col5,
        col6,
    ) = st.columns(2)

    with col5:
        st.markdown(
            f"""
        <div class="card">
            <div class="card-title">🏆 Rank</div>
            <div class="card-value">#{rank}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col6:
        st.markdown(
            f"""
        <div class="card">
            <div class="card-title">📈 Weak Subject</div>
            <div class="card-value" style="font-size:22px;">
                {weak_subject}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
