import streamlit as st
import random, time


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
st.markdown(
    """
<style>
.stButton>button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------- IMPORTS ----------------
from core.weakness_ai import add_weakness, get_weakness, reduce_weakness
from core.smart_selector import get_smart_topic
from core.revision_ai import add_revision, get_due_revisions
from core.difficulty_ai import get_user_level, get_next_level
from core.question_loader import load_questions
from ui.dashboard import render_dashboard
from streamlit_option_menu import option_menu
from core.storage_ai import save_user_data, load_user_data
from core.supabase_client import supabase
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
    user_data = load_user_data(username)

    st.session_state["tests_attempted"] = user_data.get("tests_attempted", 0)

    st.session_state["accuracy"] = user_data.get("accuracy", 0)

    st.session_state["streak"] = user_data.get("streak", 0)

    st.session_state["rank"] = user_data.get("rank", 0)

    st.session_state["weak_subject"] = user_data.get("weak_subject", "No Data")
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

            topic_data = get_smart_topic(user)

            # 🔥 Flatten tuple completely
            while isinstance(topic_data, tuple):
                topic_data = topic_data[0]

            topic_key = topic_data

            if not topic_key:
                topic_key = "polity-historical_background"

            parts = topic_key.split("-")
            if len(parts) == 2:
                subject, topic = parts
            else:
                subject = "polity"  # default
                topic = parts[0]

            st.session_state.test_subject = subject
            st.session_state.test_topic = topic

            topic = topic.lower().replace(" ", "_")

            level = st.session_state.level
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
            weak = get_weakness(user)
            if not weak:
                st.warning("No weak topics")
                st.stop()

            topic = sorted(weak.items(), key=lambda x: x[1], reverse=True)[0][0]

            if "-" not in topic:
                topic = f"polity-{topic}"

            subject, topic = topic.split("-")
            st.session_state.test_subject = subject
            st.session_state.test_topic = topic

            level = get_user_level(user)

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

            topics = get_due_revisions(user)

            # =========================
            # NO REVISIONS
            # =========================

            if not topics:

                st.success("🔥 No revisions due!")

                st.stop()

            # =========================
            # PICK REVISION
            # =========================

            topic_key, next_due = random.choice(topics)

            import datetime

            due_date = datetime.date.fromisoformat(next_due)

            today = datetime.date.today()

            days_left = (due_date - today).days

            # =========================
            # REVISION STATUS
            # =========================

            st.info(f"📅 Next Revision: {next_due}")

            st.warning(f"⏳ Days Left: {days_left}")

            if days_left == 0:

                st.error("🔥 Revision due TODAY!")

            elif days_left <= 2:

                st.warning("⚠️ Upcoming revision soon")

            # =========================
            # SPLIT SUBJECT/TOPIC
            # =========================

            subject, topic = topic_key.split("-")

            # =========================
            # DISPLAY TOPIC
            # =========================

            display_topic = topic.replace("_", " ").title()

            st.success(f"📚 Revision Topic: " f"{display_topic}")

            st.info(f"📅 Next Revision Date: " f"{next_due}")

            # =========================
            # STORE SESSION
            # =========================

            st.session_state.test_subject = subject

            st.session_state.test_topic = topic

            # =========================
            # LEVEL
            # =========================

            level = st.session_state.level

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

        # Progress
        st.progress((st.session_state.q_index + 1) / len(st.session_state.test_qs))

        st.subheader(f"Q{st.session_state.q_index+1}")

        st.write(q["question_en"])
        st.caption(q["question_ta"])

        options = [
            f"{q['options_en'][i]} / {q['options_ta'][i]}"
            for i in range(len(q["options_en"]))
        ]

        selected = st.radio("Choose answer", options)

        # ---------------- SUBMIT ----------------
        if st.button("Submit"):

            correct = q["answer"]
            selected_letter = ["a", "b", "c", "d"][options.index(selected)]

            if not st.session_state.answered:
                from core.weakness_ai import reduce_weakness
                from core.revision_ai import update_revision

                if selected_letter == correct:

                    st.success("✅ Correct")
                    st.session_state.score += 1

                    st.session_state.correct_streak += 1
                    st.session_state.wrong_count = 0

                    subject = st.session_state.test_subject
                    topic = st.session_state.test_topic
                    if topic:

                        topic = st.session_state.test_topic
                        topic = topic.lower().replace(" ", "_")

                    else:

                        st.error("No weak topic available.")

                        st.stop()

                    reduce_weakness(user, subject, topic)  # ✅ ONLY HERE
                    update_revision(user, f"{subject}-{topic}")
                    st.session_state.answered = True

                else:
                    st.error(f"❌ Correct Answer: {correct}")

                    st.session_state.wrong_count += 1
                    st.session_state.correct_streak = 0

                    subject = st.session_state.test_subject
                    topic = st.session_state.test_topic
                    topic = topic.lower().replace(" ", "_")
                    st.session_state["weak_subject"] = st.session_state.test_topic
                    add_weakness(user, subject, topic)  # ✅ ONLY HERE
                    add_revision(user, f"{subject}-{topic}")
                    st.session_state.answered = True

                # 🔥 adaptive difficulty
                st.session_state.level = get_next_level(
                    st.session_state.level,
                    st.session_state.correct_streak,
                    st.session_state.wrong_count,
                )

                st.info(f"🎯 Next Difficulty: {st.session_state.level.upper()}")

            st.session_state.answered = True

        # ---------------- NEXT ----------------
        if st.session_state.answered:

            st.info(q.get("explanation_en", ""))

            if st.button("Next"):
                st.session_state.q_index += 1
                st.session_state.answered = False
                st.rerun()
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
        # 🔥 UPDATE DASHBOARD STATS
        # ==========================================

        old_attempts = st.session_state.get("tests_attempted", 0)

        old_accuracy = st.session_state.get("accuracy", 0)

        new_accuracy = int(
            ((old_accuracy * old_attempts) + percent) / (old_attempts + 1)
        )

        # ✅ update after calculation
        st.session_state["tests_attempted"] = old_attempts + 1

        st.session_state["accuracy"] = new_accuracy

        st.session_state["streak"] = st.session_state.get("streak", 0) + 1

        st.session_state["rank"] = 120

        st.session_state["weak_subject"] = "Polity"

        # ==========================================
        # 💾 SAVE USER DATA
        # ==========================================

        save_user_data(
            username,
            {
                "tests_attempted": st.session_state["tests_attempted"],
                "accuracy": st.session_state["accuracy"],
                "streak": st.session_state["streak"],
                "rank": st.session_state["rank"],
                "weak_subject": st.session_state["weak_subject"],
            },
        )

        # ==========================================
        # 🤖 AI COACH
        # ==========================================

        from core.ai_coach import ai_coach
        from core.weakness_ai import get_weakness

        weak_data = get_weakness(user)

        coach_msg = ai_coach(user, total, total_q, weak_data)

        # 🔥 store mentor message
        st.session_state.mentor_chat = [{"role": "assistant", "content": coach_msg}]

        # 🔔 notification ON
        st.session_state["mentor_notification"] = True

        # ==========================================
        # 🧠 UPDATE MEMORY
        # ==========================================

        from core.mentor_memory import update_memory

        update_memory(user, total, total_q, weak_data)

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

        # ==========================================
        # 🔥 STREAK
        # ==========================================

        from core.streak_ai import update_streak

        streak = update_streak(user)

        st.success(f"🔥 Streak: {streak} days")

        # ==========================================
        # 📊 SAVE PROGRESS
        # ==========================================

        if not st.session_state.get("progress_saved", False):

            from core.progress_ai import save_progress

            save_progress(
                user,
                st.session_state.get("test_subject", "polity"),
                st.session_state.get("test_topic", "general"),
                percent,
            )

            st.session_state.progress_saved = True

            st.success("✅ Progress Saved!")

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
