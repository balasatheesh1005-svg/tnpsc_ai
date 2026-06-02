import streamlit as st
import random, time

from ui.components.header import render_sidebar_branding
from ui.theme import render_theme_css


# ---------------- UI HELPERS ----------------
def section(title):
    st.markdown(
        f"""
    <div style="
    background:#ffffff;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
    margin-bottom:15px;">
    <h3>{title}</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="TNPSC Nova AI", page_icon="assets/app_icon.png", layout="wide"
)
# ---------------- STYLE ----------------
render_theme_css()

# ---------------- IMPORTS ----------------
from core.question_loader import load_questions
from core.test_completion import complete_test
from core.test_evaluator import evaluate_answer
from core.test_revision import handle_correct_revision, handle_wrong_revision
from core.test_topic_selector import get_test_config
from core.test_weakness import handle_correct_answer, handle_wrong_answer
from ui.dashboard import render_dashboard
from streamlit_option_menu import option_menu
from core.dashboard_stats_ai import get_dashboard_stats
from ui.pages.daily_test_renderer import render_explanation_next, render_question
from ui.pages.leaderboard import render_leaderboard
from ui.pages.mentor import render_mentor
from ui.pages.notes import render_notes_page
from ui.pages.progress import render_progress_page
from ui.pages.teacher import render_teacher
from ui.pages.weakness import render_weakness_page

st.write("✅ Supabase Connected")
# ---------------- USER ----------------
username = st.text_input("👤 Enter your name", placeholder="Type your name...")
if not username:
    st.stop()

user = username
if username:
    st.session_state["username"] = username
    dashboard_stats = get_dashboard_stats(username)

    st.session_state["tests_attempted"] = dashboard_stats["tests_attempted"]

    st.session_state["accuracy"] = dashboard_stats["accuracy"]

    st.session_state["streak"] = dashboard_stats["streak"]

    st.session_state["rank"] = dashboard_stats["rank"]

    st.session_state["weak_subject"] = dashboard_stats["weak_subject"]
# ---------------- SESSION INIT ----------------

if "correct_streak" not in st.session_state:
    st.session_state.correct_streak = 0

if "wrong_count" not in st.session_state:
    st.session_state.wrong_count = 0

if "level" not in st.session_state:
    st.session_state.level = "easy"

if "exam" not in st.session_state:
    st.session_state["exam"] = "group1"

if "user" not in st.session_state:
    st.session_state["user"] = "satheeshkumar"

if "start_time" not in st.session_state:
    st.session_state.start_time = 0

if "test_active" not in st.session_state:
    st.session_state.test_active = False

if "start_test" not in st.session_state:
    st.session_state.start_test = False

if "test_qs" not in st.session_state:
    st.session_state.test_qs = []

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "mentor_notification" not in st.session_state:
    st.session_state["mentor_notification"] = False

if "mentor_chat" not in st.session_state:
    st.session_state["mentor_chat"] = []

# ---------------- MENU ----------------
with st.sidebar:
    render_sidebar_branding(
        username,
        st.session_state.get("rank", 0),
        st.session_state.get("accuracy", 0),
        st.session_state.get("streak", 0),
    )

    selected = option_menu(
        menu_title="📂 Menu",
        options=[
            "🏠 Home",
            "📘 Daily Test",
            "📚 Notes",
            "🧠 Weakness",
            "📊 Progress",
            "🏆 Leaderboard",
            "🤖 AI Teacher",
            "👨‍🏫 Personal Mentor",
        ],
        icons=[
            "house",
            "clipboard-check",
            "book",
            "brain",
            "bar-chart",
            "trophy",
            "robot",
            "person",
        ],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "0",
                "background-color": "transparent",
            },
            "icon": {
                "color": "inherit",
                "font-size": "17px",
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "4px 0",
                "--hover-color": "#EFF6FF",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #0F172A, #2563EB)",
                "color": "#FFFFFF",
            },
            "menu-title": {
                "font-size": "16px",
                "font-weight": "800",
                "color": "#0F172A",
                "padding": "0.4rem 0.2rem 0.75rem",
            },
        },
    )


def init_test():
    st.session_state.start_time = time.time()
    st.session_state.test_active = True
    st.session_state.score = 0
    st.session_state.q_index = 0


def get_color(score):
    if score < 50:
        return "red"
    elif score < 75:
        return "orange"
    else:
        return "green"


import time


def typing_effect(text):
    placeholder = st.empty()
    output = ""

    for char in text:
        output += char
        placeholder.markdown(output)
        time.sleep(0.01)


# ---------------- SESSION INIT ----------------
if "test_qs" not in st.session_state:
    st.session_state.test_qs = []
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "test_active" not in st.session_state:
    st.session_state.test_active = False
if "test_subject" not in st.session_state:
    st.session_state.test_subject = None

if "test_topic" not in st.session_state:
    st.session_state.test_topic = None

# ================= MENU ROUTING =================

# ---------------- HOME ----------------
if selected == "🏠 Home":
    render_dashboard()


# ---------------- DAILY TEST ----------------
elif selected == "📘 Daily Test":
    section("📘 Daily Test")

    col1, col2, col3 = st.columns(3)
    if st.session_state.get("start_test"):

        subject = st.session_state.get("test_subject")
        topic = st.session_state.get("test_topic")
        questions = load_questions(subject, topic, "easy")

        if not questions:
            st.error("No questions found")
            st.stop()

        st.session_state.test_qs = random.sample(questions, min(5, len(questions)))
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.test_active = True

        st.session_state.start_test = False

        st.rerun()  # 🔥 MUST

    # 🚀 START TEST
    with col1:
        if st.button("🚀 Start Daily Test"):
            with st.spinner("Loading questions..."):

                st.success("Questions Loaded!")

                st.session_state.q_index = 0

                st.session_state.score = 0

                st.session_state.answered = False

                st.session_state.correct_streak = 0

                st.session_state.wrong_count = 0

                st.session_state.progress_saved = False

                st.session_state.test_active = True
                st.session_state.start_time = time.time()
                st.session_state.level = "easy"

            test_config = get_test_config(user)
            subject = test_config["subject"]
            topic = test_config["topic"]

            st.session_state.test_subject = subject
            st.session_state.test_topic = topic

            level = test_config["level"]
            questions = load_questions(subject, topic, level)

            if not questions:
                st.error("No questions found")
                st.stop()

            st.session_state.test_qs = random.sample(questions, min(5, len(questions)))
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.answered = False

            st.rerun()
    # 🔥 WEAK TEST
    with col2:
        if st.button("🔥 Practice Weak Topics"):
            test_config = get_test_config(user, mode="weak")
            subject = test_config["subject"]
            topic = test_config["topic"]
            st.session_state.test_subject = subject
            st.session_state.test_topic = topic

            level = test_config["level"]

            st.session_state.subject = subject
            st.session_state.topic = topic
            questions = load_questions(subject, topic, level)

            if not questions:
                st.error("No questions found")
                st.stop()

            st.session_state.test_qs = random.sample(questions, min(5, len(questions)))
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.test_active = True
            st.session_state.start_time = time.time()

            st.rerun()
    with col3:

        if st.button("📚 Revision Test"):

            test_config = get_test_config(user, mode="revision")
            subject = test_config["subject"]
            topic = test_config["topic"]

            # =========================
            # STORE SESSION
            # =========================

            st.session_state.test_subject = subject

            st.session_state.test_topic = topic

            # =========================
            # LEVEL
            # =========================

            level = test_config["level"]

            # =========================
            # LOAD QUESTIONS
            # =========================

            questions = load_questions(subject, topic, level)

            if not questions:

                st.error("❌ No revision questions found")

                st.stop()

            # =========================
            # START TEST
            # =========================

            st.session_state.test_qs = random.sample(questions, min(5, len(questions)))

            st.session_state.q_index = 0

            st.session_state.test_active = True

            st.rerun()

    # ---------------- SAFETY ----------------
    if not st.session_state.test_active:
        st.info("👉 Click Start Test")
        st.stop()

    # ---------------- TIMER ----------------
    elapsed = int(time.time() - st.session_state.start_time)
    st.warning(f"⏱ Time: {elapsed}s")

    if not st.session_state.test_qs:
        st.warning("No questions loaded")
        st.stop()

    # ---------------- QUESTIONS ----------------
    if st.session_state.q_index < len(st.session_state.test_qs):

        q = st.session_state.test_qs[st.session_state.q_index]

        # 🎯 Difficulty UI
        color = {"easy": "#2ecc71", "medium": "#f39c12", "hard": "#e74c3c"}

        st.markdown(
            f"""
        <div style="
        background:{color[st.session_state.level]};
        padding:10px;
        border-radius:10px;
        color:white;
        text-align:center;
        ">
        🎯 Difficulty: {st.session_state.level.upper()}
        </div>
        """,
            unsafe_allow_html=True,
        )

        selected, options = render_question(q)

        # ---------------- SUBMIT ----------------
        if st.button("Submit"):

            result = evaluate_answer(
                selected,
                options,
                q,
                user,
                st.session_state.test_subject,
                st.session_state.test_topic,
            )

            if result["processed"]:
                if result["is_correct"]:

                    subject = st.session_state.test_subject
                    topic = st.session_state.test_topic
                    topic = handle_correct_answer(user, subject, topic)
                    handle_correct_revision(user, subject, topic)

                else:

                    subject = st.session_state.test_subject
                    topic = st.session_state.test_topic
                    topic = handle_wrong_answer(user, subject, topic)
                    handle_wrong_revision(user, subject, topic)

        # ---------------- NEXT ----------------
        if st.session_state.answered:

            render_explanation_next(q)
    # ✅ ALWAYS DEFINE FIRST
    total = st.session_state.get("score", 0)
    total_q = len(st.session_state.get("test_qs", []))
    # ---------------- RESULT ----------------
    if st.session_state.q_index >= total_q:

        if total_q == 0:
            percent = 0
        else:
            percent = int((total / total_q) * 100)
        # ==========================================
        # TEST COMPLETED
        # ==========================================

        st.success("🎉 Test Completed!")

        st.markdown(f"### ✅ Score: {total} / {total_q}")

        percent = int((total / total_q) * 100)

        st.progress(percent / 100)

        # ==========================================
        # 🏆 RANK PREDICTION
        # ==========================================

        def predict_rank(percent):

            if percent >= 90:
                return "Top 1-100 Rank"

            elif percent >= 75:
                return "Top 500 Rank"

            elif percent >= 60:
                return "Top 2000 Rank"

            else:
                return "Needs Improvement"

        rank = predict_rank(percent)

        st.markdown("## 🏆 Rank Prediction")

        st.success(f"🎯 Expected Rank: {rank}")

        complete_test(
            user,
            st.session_state.get("test_subject", "polity"),
            st.session_state.get("test_topic", "general"),
            percent,
        )

        # ==========================================
        # 🔥 REFRESH DASHBOARD STATS
        # ==========================================

        dashboard_stats = get_dashboard_stats(username)

        st.session_state["tests_attempted"] = dashboard_stats["tests_attempted"]

        st.session_state["accuracy"] = dashboard_stats["accuracy"]

        st.session_state["streak"] = dashboard_stats["streak"]

        st.session_state["rank"] = dashboard_stats["rank"]

        st.session_state["weak_subject"] = dashboard_stats["weak_subject"]

        # ==========================================
        # 🔚 RESET TEST
        # ==========================================

        st.session_state.test_active = False

        st.session_state.test_qs = []

# =====================================================
# 📘 NOTES
# =====================================================

elif selected == "📚 Notes":

    render_notes_page(section)


# =====================================================
# 🧠 WEAKNESS
# =====================================================

elif selected == "🧠 Weakness":

    render_weakness_page(section, user)


# =====================================================
# 📊 PROGRESS
# =====================================================

elif selected == "📊 Progress":

    render_progress_page(section, user)

# ---------------- LEADERBOARD ----------------
elif selected == "🏆 Leaderboard":

    render_leaderboard(section)

# ---------------- AI TEACHER ----------------
elif selected == "🤖 AI Teacher":

    render_teacher(section, user)

elif selected == "👨‍🏫 Personal Mentor":

    render_mentor(section, typing_effect, user)

st.markdown("---")

st.caption("🚀 TNPSC AI • India's AI Powered TNPSC Preparation Platform")
