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
from core.notes_ai import load_notes
from core.streamlit_ui_engine import render_notes, render polity
from core.topics_loader import get_topics
from core.components.mindmap import render_mindmap
from core.components.revision_cards import generate_cards_from_notes, revision_cards
 
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
menu = st.sidebar.radio(
    "📂 Menu",
    [
        "🏠 Home",
        "📘 Daily Test",
        "📚 Notes",
        "🧠 Weakness",
        "📊 Progress",
        "🏆 Leaderboard",
        "🤖 AI Teacher",
        "🤖 Personal Mentor 🔴" if st.session_state.get("mentor_notification") else "🤖 Personal Mentor",
    ],
)


# ---------------- LOAD QUESTIONS ----------------
def load_questions(subject, topic, level):
    import json, os

    subject = subject.lower()
    topic = topic.lower()

    file_path = f"data/questions/{subject}/{topic}_{level}.json"

    if not os.path.exists(file_path):
        print("❌ Missing:", file_path)
        return []

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def init_test():
    st.session_state.start_time = time.time()
    st.session_state.test_active = True
    st.session_state.score = 0
    st.session_state.q_index = 0


import json


def load_note(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


import re


def format_topic(topic):
    topic = topic.lower()
    topic = re.sub(r"[^a-z0-9 ]", "", topic)
    return topic.replace(" ", "_")


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
if menu == "🏠 Home":
    section("🏠 Dashboard")
    st.write(f"👋 Welcome {user}")
    st.info("Use sidebar to navigate")


# ---------------- DAILY TEST ----------------
elif menu == "📘 Daily Test":

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

            st.session_state.test_active = True
            st.session_state.start_time = time.time()
            st.session_state.level = "easy"
            st.session_state.correct_streak = 0
            st.session_state.wrong_count = 0

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
            topic_key = item

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
                    topic = topic.lower().replace(" ", "_")

                    reduce_weakness(user, subject, topic)  # ✅ ONLY HERE
                    update_revision(user, f"{subject}-{topic}")

                else:
                    st.error(f"❌ Correct Answer: {correct}")

                    st.session_state.wrong_count += 1
                    st.session_state.correct_streak = 0

                    subject = st.session_state.test_subject
                    topic = st.session_state.test_topic
                    topic = topic.lower().replace(" ", "_")

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
    # ✅ ALWAYS DEFINE FIRST
    total = st.session_state.get("score", 0)
    total_q = len(st.session_state.get("test_qs", []))
    # ---------------- RESULT ----------------
    if st.session_state.q_index >= total_q:

        if total_q == 0:
            percent = 0
        else:
            percent = int((total / total_q) * 100)

        st.success("🎉 Test Completed!")

        st.markdown(f"### ✅ Score: {total} / {total_q}")
        st.progress(percent / 100)
        from core.ai_coach import ai_coach
        from core.weakness_ai import get_weakness

        weak_data = get_weakness(user)

        coach_msg = ai_coach(user, total, total_q, weak_data)

        # 🔥 store message
        st.session_state.mentor_chat = [
            {"role": "assistant", "content": coach_msg}
        ]

        # 🔔 notification ON
        st.session_state["mentor_notification"] = True
        from core.mentor_memory import update_memory

        update_memory(user, total, total_q, weak_data)
        
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
        st.session_state.test_qs = []

    from core.progress_ai import save_progress

    percent = int((total / total_q) * 100)

    save_progress(
        user,
        st.session_state.get("test_subject"),
        st.session_state.get("test_topic"),
        percent,
    )
    
elif menu == "📚 Notes":

    st.markdown("## 📘 Notes Section")

    # 🔹 Select Subject
    subject = st.selectbox("Select Subject", ["polity", "economy", "history"])

    # 🔹 Get Topics
    try:
        topics = get_topics(subject)
    except:
        st.error("Topics not found. Check structure JSON.")
        st.stop()

    # 🔹 Select Topic
    topic = st.selectbox("Select Topic", topics)

    # 🔹 Format file path
    file_path = f"data/notes/{subject}/{format_topic(topic)}.json"

    # 🔹 Debug (optional)
    # st.write("Looking for:", file_path)

    # 🔹 Load & Render
    try:
        data = load_note(file_path)

        # 🔥 MAIN ENGINE
        render_notes(data)
        render_polity(content["content"])
            # Mind Map
        if "mind_map" in content["content"]:
            st.markdown("## 🧠 Mind Map")
            render_mindmap(content["content"]["mind_map"])

        # Revision
        st.markdown("## 🔁 Revision")
        cards = generate_cards_from_notes(content["content"])
        if cards:
            revision_cards(cards)

        # Debug UI type
        st.caption(f"UI Type: {data.get('ui_type')}")

    except FileNotFoundError:
        st.warning("Notes not available yet")

    except Exception as e:
        st.error("Error loading notes")
        st.error(e)

    if st.button("🧠 Practice from this Topic"):
        st.session_state.test_subject = subject
        st.session_state.test_topic = format_topic(topic)
        st.session_state.start_test = True
        st.session_state.start_time = time.time()

        st.rerun()

    # -------------- WEAKNESS ----------------
elif menu == "🧠 Weakness":

    import pandas as pd

    weak_data = get_weakness(user)

    if weak_data:

        # ✅ STEP 1: create df FIRST
        df = pd.DataFrame(list(weak_data.items()), columns=["Topic", "Weakness"])

        # split
        df[["Subject", "Subtopic"]] = df["Topic"].str.split("-", expand=True)

        # clean UI
        df["Subtopic"] = df["Subtopic"].str.replace("_", " ").str.title()

        # ✅ STEP 2: functions AFTER df (or before, both ok)
        def color_map(val):
            if val >= 4:
                return "background-color: #ff4d4d; color:white"
            elif val >= 2:
                return "background-color: #ffc107"
            else:
                return "background-color: #28a745"

        def bar(val):
            return "█" * val

        # ✅ STEP 3: apply
        df["Level"] = df["Weakness"].apply(bar)

        # 🎨 Heatmap
        st.markdown("### 🔥 Weakness Heatmap")
        st.dataframe(df.style.applymap(color_map, subset=["Weakness"]))

        # 📊 Visual
        st.markdown("### 📊 Visual Strength")
        st.table(df[["Subject", "Subtopic", "Level"]])

    else:
        st.success("🔥 No Weakness!")

# ---------------- PROGRESS ----------------
elif menu == "📊 Progress":

    section("📊 Progress Dashboard")

    progress = get_progress(user)

    if not progress:
        st.info("No data yet")
        st.stop()

    import pandas as pd

    rows = []

    for subject, topics in progress.items():

        # ✅ if topics is dict (correct case)
        if isinstance(topics, dict):

            for topic, scores in topics.items():
                avg = sum(scores) / len(scores)
                rows.append({"Subject": subject, "Topic": topic, "Average": avg})

        # ⚠️ fallback (old data format)
        elif isinstance(topics, list):

            avg = sum(topics) / len(topics)
            rows.append({"Subject": subject, "Topic": "overall", "Average": avg})

    df = pd.DataFrame(rows)

    st.subheader("📘 Topic-wise Performance")
    st.dataframe(df)

    st.subheader("📊 Subject-wise Performance")
    st.bar_chart(df.groupby("Subject")["Average"].mean())

    st.subheader("🔥 Topic Heatmap")

    for subject, topics in progress.items():

        if not isinstance(topics, dict):
            continue

        st.markdown(f"### 📘 {subject.capitalize()}")

        cols = st.columns(3)

        i = 0
        for topic, scores in topics.items():

            avg = sum(scores) / len(scores)
            color = get_color(avg)

            text = f"**{topic}**\n\n{int(avg)}%"

            with cols[i % 3]:

                with st.container():
                    if color == "red":
                        st.markdown(
                            f"""
                        <div style='background-color:#ffe5e5;
                                    padding:10px;
                                    border-radius:10px'>
                        {text}
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

                    elif color == "orange":
                        st.markdown(
                            f"""
                        <div style='background-color:#fff4e5;
                                    padding:10px;
                                    border-radius:10px'>
                        {text}
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

                    else:
                        st.markdown(
                            f"""
                        <div style='background-color:#e6ffe6;
                                    padding:10px;
                                    border-radius:10px'>
                        {text}
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

            i += 1
    heatmap = {}

    for subject, topics in progress.items():
        if isinstance(topics, dict):
            for topic, scores in topics.items():
                avg = sum(scores) / len(scores)
                heatmap[topic] = avg

    st.subheader("🔥 Strong vs Weak")

    weak = df[df["Average"] < 50]
    strong = df[df["Average"] >= 75]

    st.write("🔻 Weak Topics")
    st.write(weak)

    st.write("💪 Strong Topics")
    st.write(strong)

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

elif menu.startswith("🤖 Personal Mentor"):

    st.markdown("## 🤖 Your Personal AI Mentor")

    # 🔔 notification clear
    if st.session_state.get("mentor_notification"):
        st.success("🎯 New guidance available!")
        st.session_state["mentor_notification"] = False

    # 💬 chat history show
    for msg in st.session_state.mentor_chat:

        if msg["role"] == "assistant":
            with st.chat_message("assistant"):
                typing_effect(msg["content"])  # 🔥 HERE

        else:
            st.chat_message("user").write(msg["content"])

    # 🧠 user reply
    user_msg = st.chat_input("Ask your mentor...")

    if user_msg:
        st.session_state.mentor_chat.append(
            {"role": "user", "content": user_msg}
        )

        from core.ai_teacher import ai_teacher

        reply = ai_teacher(user_msg, user)

        st.session_state.mentor_chat.append(
            {"role": "assistant", "content": reply}
        )

        st.rerun()