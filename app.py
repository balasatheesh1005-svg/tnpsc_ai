import streamlit as st
import json, os, random

st.set_page_config(page_title="TNPSC AI", layout="wide")

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

.card {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

.title {
    font-size: 22px;
    font-weight: bold;
}

.green {
    color: green;
}

.red {
    color: red;
}

.orange {
    color: orange;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-weight: bold;
    border: none;
}
</style>
""", unsafe_allow_html=True)
from ui.dashboard import show_dashboard
from core.weakness_ai import add_weakness, get_total_weakness
from core.study_planner import get_today_plan
from core.ai_teacher import ai_teacher
from core.revision_ai import get_revision_topics

username = st.text_input("Enter your name")

if not username:
    st.stop()

user = username

menu = st.sidebar.radio("📂 Menu", [
    "🏠 Home",
    "🧠 Weakness",
    "📊 Progress",
    "🏆 Leaderboard",
    "🤖 AI Teacher"
])


# ✅ correct menu handling
if menu == "🏠 Home":

    st.markdown(f"""
    <div style="
    background: linear-gradient(90deg, #667eea, #764ba2);
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
    ">
    <h2>👋 Welcome {user}</h2>
    <p>Your TNPSC AI Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "🤖 AI Teacher":
    st.write("AI Teacher Page")
    st.markdown("""
<div style="
background: linear-gradient(90deg, #667eea, #764ba2);
padding:20px;
border-radius:15px;
color:white;
text-align:center;
">
<h1>🔥 TNPSC AI</h1>
<p>Your Smart Preparation Partner</p>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style='
    background: linear-gradient(90deg, #ff512f, #dd2476);
    -webkit-background-clip: text;
    color: transparent;
'>
🔥 Tnpsc AI Test
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg, #36d1dc, #5b86e5);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

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


# ---------------- LOAD QUESTIONS ----------------
def load_questions(subject, topic, level="easy"):
    path = f"data/questions/{subject.lower()}/{topic}_{level}.json"

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
        st.write(path)
# ---------------- START TEST ----------------
from core.smart_selector import get_smart_topic
from core.difficulty_ai import get_user_level
st.markdown("""
<div style="
background:white;
padding:15px;
border-radius:12px;
box-shadow:0 2px 8px rgba(0,0,0,0.1);
margin-bottom:15px;
">
<h3>📘 Daily Test</h3>
<p>Practice smart AI-based questions</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start Daily Test"):

        st.session_state.test_active = True

        topic_key, mode = get_smart_topic(user)

        if isinstance(topic_key, tuple):
            topic_key = topic_key[0]

        if not topic_key:
            topic_key = "polity-historical_background"

        subject, topic = topic_key.lower().split("-")

        level = get_user_level(user)

        if mode == "weak":
            st.error(f"💀 Weak Focus: {topic_key}")
        elif mode == "revision":
            st.warning(f"🔁 Revision Focus: {topic_key}")
        else:
            st.info(f"📘 New Topic: {topic_key}")

        st.info(f"🎯 Difficulty: {level.upper()}")

        questions = load_questions(subject, topic, level)

        if not questions:
            st.error(f"No questions found: {subject}/{topic}/{level}")
            st.stop()

        selected = random.sample(questions, min(len(questions), 5))

        st.session_state.test_qs = selected
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.answered = False

        st.rerun()

    with col2:
        if st.button("🔥 Practice Weak Topics"):

            st.session_state.test_active = True

            from core.weakness_ai import get_weakness

            weak_topics = get_weakness(user)

            if not weak_topics:
                st.warning("No weak topics found. Practice normal test 👍")
                st.stop()

            # 🔥 highest weak topic
            top_topic = sorted(weak_topics.items(), key=lambda x: x[1], reverse=True)[0][0]

            # format fix
            if "-" not in top_topic:
                top_topic = f"polity-{top_topic}"

            subject, topic = top_topic.lower().split("-")

            level = get_user_level(user)

            st.error(f"💀 Weak Focus: {top_topic}")
            st.info(f"🎯 Difficulty: {level.upper()}")

            questions = load_questions(subject, topic, level)

            if not questions:
                st.error(f"No questions found: {subject}/{topic}/{level}")
                st.stop()

            selected = random.sample(questions, min(len(questions), 5))

            st.session_state.test_qs = selected
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.answered = False

            st.rerun()        
# ---------------- SAFETY ----------------
if not st.session_state.test_active:
    st.info("👉 Click Start Daily Test")
    st.stop()

# ---------------- SHOW QUESTION ----------------
if st.session_state.q_index < len(st.session_state.test_qs):

    q = st.session_state.test_qs[st.session_state.q_index]

    st.subheader(f"Question {st.session_state.q_index + 1}")

    st.markdown(f"""
    <div style="
    background:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 6px rgba(0,0,0,0.1);
    ">
    <h4>📘 {q['question_en']}</h4>
    <p style='color:gray'>{q['question_ta']}</p>
    </div>
    """, unsafe_allow_html=True)

    options = [
        f"{q['options_en'][i]} / {q['options_ta'][i]}"
        for i in range(len(q["options_en"]))
    ]

    selected = st.radio("Choose answer:", options)

    # SUBMIT
    if st.button("Submit Answer"):

        correct = q["answer"].lower().strip()

        selected_index = options.index(selected)
        selected_letter = ["a","b","c","d"][selected_index]

        if not st.session_state.answered:

            from core.ai_teacher import explain_answer

            if selected_letter == correct:
                st.success("✅ Correct")
                st.session_state.score += 1
            else:
                st.error("❌ Wrong Answer")

                explanation = explain_answer(
                q["question_en"],
                correct,
                selected_letter
                )

                st.info(explanation)

                subject = q.get("subject", "polity")
                topic = q.get("topic", "general")

                add_weakness(user, subject, topic)

                st.warning("📌 Added to your weak topics!")

        st.session_state.answered = True
    # EXPLANATION
    if st.session_state.answered:
        st.info(q.get("explanation_en", ""))

        if st.button("Next ➡️"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.rerun()


# ---------------- RESULT ----------------
# ---------------- RESULT ----------------
else:
    total = st.session_state.score
    total_q = len(st.session_state.test_qs)

    percent = int((total / total_q) * 100) if total_q > 0 else 0
    st.progress(percent / 100)
    st.session_state.last_percent = percent

    from core.progress_ai import save_progress
    if st.session_state.test_qs:
        if st.session_state.test_qs:
            subject = st.session_state.test_qs[0].get("subject", "general")
        else:
            subject = "general"
    else:
        subject = "general"
    save_progress(user, subject, percent)

    # 🎨 CARD UI START
    st.markdown(f"""
<div style="
background: linear-gradient(135deg, #43cea2, #185a9d);
padding:20px;
border-radius:15px;
color:white;
text-align:center;
">
<h2>🏁 Test Completed</h2>
<h3>{percent}%</h3>
<p>Score: {total}/{total_q}</p>
</div>
""", unsafe_allow_html=True)
    if percent >= 80:
        st.markdown('<p class="green">🔥 Topper Level</p>', unsafe_allow_html=True)
    elif percent >= 50:
        st.markdown('<p class="orange">👍 Average</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="red">❌ Need Improvement</p>', unsafe_allow_html=True)
    st.session_state.test_active = False


    from core.streak_ai import update_streak
    streak = update_streak(user)

    st.markdown(f"🔥 Streak: {streak} days")

    st.markdown('</div>', unsafe_allow_html=True)

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
            st.success(f"🎯 Your Expected Rank: {rank}")
    
from core.weakness_ai import get_weakness
st.markdown("## 🧠 Weakness Heatmap")

weak_data = get_weakness(user)

if not weak_data:
    st.success("🔥 No Weakness!")
else:
    for topic, count in weak_data.items():
        color = "#28a745"
        if count >= 5:
            color = "#dc3545"
        elif count >= 2:
            color = "#ffc107"

        st.markdown(f"""
        <div style="
        background:white;
        padding:10px;
        border-radius:10px;
        margin-bottom:8px;
        border-left:6px solid {color};
        ">
        <b>{topic}</b> → {count}
        </div>
        """, unsafe_allow_html=True)
from core.streak_ai import get_streak
streak = get_streak(user)
st.markdown(f"""
<div style="
background: linear-gradient(90deg, #ff9966, #ff5e62);
padding:10px;
border-radius:10px;
color:white;
font-weight:bold;
text-align:center;
">
🔥 {streak} Day Streak
</div>
""", unsafe_allow_html=True)
st.success(f"🔥 Current Streak: {streak} days")

if streak == 0:
    st.warning("⚡ Start your streak today!")
elif streak < 3:
    st.info("👍 Good start! Keep going!")
elif streak < 7:
    st.success("🔥 Strong consistency!")
else:
    st.success("🚀 Unstoppable! TNPSC Ready!")

from core.weakness_ai import get_weakness

def get_today_plan(user):

    weak = get_weakness(user)

    if not weak:
        return ["Revise strong topic", "Take 1 mock test"]

    top_weak = sorted(weak.items(), key=lambda x: x[1], reverse=True)[:2]

    plan = []
    for t, _ in top_weak:
        plan.append(f"Revise {t}")

    plan.append("Take 1 Test")

    return plan

st.markdown("## 📅 Today's Plan")

plan = get_today_plan(user)

for p in plan:
    st.write(f"✅ {p}")

st.markdown("""
<div style="
background:#ffffff;
padding:15px;
border-radius:12px;
box-shadow:0 2px 8px rgba(0,0,0,0.1);
">
<h3>🤖 AI Teacher</h3>
</div>
""", unsafe_allow_html=True)

user_q = st.text_input("Ask your doubt:")

if st.button("Ask AI"):
    if user_q:
        with st.spinner("Thinking... 🤖"):
            answer = ai_teacher(user_q, user)
            st.success(answer)

st.markdown('</div>', unsafe_allow_html=True)

from core.revision_ai import get_revision_topics

st.markdown("## 🔁 Smart Revision")

rev = get_revision_topics(user)

if rev:
    for t in rev:
        st.write(f"🔁 Revise: {t}")
else:
    st.success("No revision needed 🔥")

from core.leaderboard_ai import get_top_users

st.markdown("## 🏆 Leaderboard")

leaders = get_top_users()

for i, (u, s) in enumerate(leaders, 1):

    if u == user:
        st.success(f"⭐ {i}. {u} → {int(s)}%")
    else:
        st.write(f"{i}. {u} → {int(s)}%")


if st.button("Start Full Mock Test (100Q)"):

    all_questions = load_questions("polity", "historical_background")

    selected = random.sample(all_questions, min(len(all_questions), 100))

    st.session_state.test_qs = selected
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False

    st.rerun()                

import pandas as pd
from core.progress_ai import get_progress

st.markdown("## 📊 Progress Analytics")

progress = get_progress(user)
total_scores = []

if not progress:
    st.info("No data yet")
else:
    df_data = []

    for subject, scores in progress.items():
        avg = sum(scores) / len(scores)
        df_data.append({
            "Subject": subject,
            "Average Score": avg
        })

    df = pd.DataFrame(df_data)

    st.bar_chart(df.set_index("Subject"))

for scores in progress.values():
    total_scores.extend(scores)

if total_scores:
    overall = sum(total_scores) / len(total_scores)
  

    st.markdown("## 🎯 Exam Readiness")

    if overall >= 75:
        st.success(f"🔥 Ready for Exam ({int(overall)}%)")
    elif overall >= 50:
        st.warning(f"⚠️ Moderate ({int(overall)}%)")
    else:
        st.error(f"❌ Not Ready ({int(overall)}%)")