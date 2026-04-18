import streamlit as st
import json, os, random, time


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
st.set_page_config(page_title="TNPSC AI", layout="wide")

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
from core.ai_teacher import ai_teacher
from core.weakness_ai import add_weakness, get_weakness, reduce_weakness
from core.progress_ai import get_progress, save_progress
from core.smart_selector import get_smart_topic
from core.leaderboard_ai import get_top_users
from core.revision_ai import add_revision, get_due_revisions
from core.difficulty_ai import get_user_level, get_next_level

# ---------------- USER ----------------
username = st.text_input("Enter your name")
if not username:
    st.stop()

user = username

# ---------------- SESSION INIT ----------------

if "correct_streak" not in st.session_state:
    st.session_state.correct_streak = 0

if "wrong_count" not in st.session_state:
    st.session_state.wrong_count = 0

if "level" not in st.session_state:
    st.session_state.level = "easy"

# ---------------- MENU ----------------
menu = st.sidebar.radio(
    "📂 Menu",
    [
        "🏠 Home",
        "📘 Daily Test",
        "🧠 Weakness",
        "📊 Progress",
        "🏆 Leaderboard",
        "🤖 AI Teacher",
    ],
)


# ---------------- LOAD QUESTIONS ----------------
def load_questions(subject, topic, level="easy"):
    path = f"data/questions/{subject}/{topic}_{level}.json"
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


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


# ================= MENU ROUTING =================

# ---------------- HOME ----------------
if menu == "🏠 Home":
    section("🏠 Dashboard")
    st.write(f"👋 Welcome {user}")
    st.info("Use sidebar to navigate")


# ---------------- DAILY TEST ----------------
elif menu == "📘 Daily Test":

    section("📘 Daily Test")

    col1, col2, col3 = st.columns(3)

    # 🚀 START TEST
    with col1:
        if st.button("🚀 Start Daily Test"):
            st.session_state.test_active = True
            st.session_state.start_time = time.time()
            st.session_state.level = "easy"
            st.session_state.correct_streak = 0
            st.session_state.wrong_count = 0

            topic_key, _ = get_smart_topic(user)

            if isinstance(topic_key, tuple):
                topic_key = topic_key[0]

            if not topic_key:
                topic_key = "polity-historical_background"

            subject, topic = topic_key.split("-")
            level = get_user_level(user)
            subject, topic = topic_key.split("-")

            st.session_state.subject = subject
            st.session_state.topic = topic

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

            if not topics:
                st.success("🔥 No revisions due!")
                st.stop()

            item = random.choice(topics)
            topic_key = item["topic"]
            next_due = item["next_due"]

            import datetime

            due_date = datetime.date.fromisoformat(next_due)
            today = datetime.date.today()
            days_left = (due_date - today).days

            st.info(f"📅 Next Revision: {next_due}")
            st.warning(f"⏳ Days Left: {days_left}")

            if days_left == 0:
                st.error("🔥 Revision due TODAY!")
            elif days_left <= 2:
                st.warning("⚠️ Upcoming revision soon")

            subject, topic = topic_key.split("-")

            level = st.session_state.level

            questions = load_questions(subject, topic, level)

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

                    subject = q.get("subject", "polity")
                    topic = q.get("topic", "general")

                    reduce_weakness(user, subject, topic)  # ✅ ONLY HERE
                    update_revision(user, f"{subject}-{topic}")

                else:
                    st.error(f"❌ Correct Answer: {correct}")

                    st.session_state.wrong_count += 1
                    st.session_state.correct_streak = 0

                    subject = q.get("subject", "polity")
                    topic = q.get("topic", "general")

                    add_weakness(user, subject, topic)  # ✅ ONLY HERE
                    add_revision(user, f"{subject}-{topic}")

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
    # ---------------- RESULT ----------------
    else:

        total = st.session_state.score
        total_q = len(st.session_state.test_qs)
        if total_q == 0:
            percent = 0
        else:
            percent = int((total / total_q) * 100)

        st.success("🏁 Test Completed")

        # 🏆 Rank Prediction
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

        # 🔥 Streak
        from core.streak_ai import update_streak

        streak = update_streak(user)
        st.success(f"🔥 Streak: {streak} days")

        st.session_state.test_active = False

# ---------------- WEAKNESS ----------------
elif menu == "🧠 Weakness":

    section("🧠 Weakness Analysis")

    weak_data = get_weakness(user)

    if not weak_data:
        st.success("🔥 No Weakness!")
    else:

        for topic, count in weak_data.items():

            if count >= 5:
                color = "#ff4d4d"
            elif count >= 2:
                color = "#ffc107"
            else:
                color = "#28a745"

            st.markdown(
                f"""
            <div style="
            background:white;
            padding:10px;
            border-radius:10px;
            margin-bottom:8px;
            border-left:6px solid {color};
            ">
            📘 {topic} → {count}
            </div>
            """,
                unsafe_allow_html=True,
            )
# ---------------- PROGRESS ----------------
elif menu == "📊 Progress":

    section("📊 Progress")

    progress = get_progress(user)

    if not progress:
        st.info("No data")
    else:
        import pandas as pd

        data = []
        for sub, scores in progress.items():
            data.append({"Subject": sub, "Avg": sum(scores) / len(scores)})
        df = pd.DataFrame(data)
        st.bar_chart(df.set_index("Subject"))


# ---------------- LEADERBOARD ----------------
elif menu == "🏆 Leaderboard":

    section("🏆 Leaderboard")

    leaders = get_top_users()

    for i, (u, s) in enumerate(leaders, 1):
        st.write(f"{i}. {u} → {int(s)}%")


# ---------------- AI TEACHER ----------------
elif menu == "🤖 AI Teacher":

    section("🤖 AI Teacher")

    q = st.text_input("Ask doubt")

    if st.button("Ask"):
        if q:
            with st.spinner("Thinking..."):
                ans = ai_teacher(q, user)
                st.success(ans)
