import os
import streamlit as st

BASE_PATH = "data/notes"


# ===============================
# LOAD NOTES
# ===============================


@st.cache_data
def load_notes():

    notes_data = []

    for subject in os.listdir(BASE_PATH):

        subject_path = os.path.join(BASE_PATH, subject)

        if not os.path.isdir(subject_path):
            continue

        for file in os.listdir(subject_path):

            if file.endswith(".txt"):

                file_path = os.path.join(subject_path, file)

                with open(file_path, "r", encoding="utf-8") as f:

                    content = f.read()

                    notes_data.append(
                        {
                            "subject": subject,
                            "topic": file.replace(".txt", ""),
                            "content": content,
                        }
                    )

    return notes_data


# ===============================
# CLEAN TEXT
# ===============================


def clean_text(text):

    return text.lower().replace("\n", " ")


# ===============================
# EXTRACT BEST LINES
# ===============================


def extract_best_lines(content, question):

    content = content.replace("\n", ". ")

    sentences = content.split(".")

    q_words = question.lower().split()

    scored = []

    for line in sentences:

        score = 0

        for word in q_words:

            if word in line.lower():
                score += 1

        if score > 0:

            scored.append((score, line.strip()))

    # sort by score
    scored.sort(reverse=True)

    # top 3 lines
    best_lines = [line for score, line in scored[:3]]

    return best_lines


# ===============================
# AI TEACHER
# ===============================

from core.weakness_ai import get_weakness


def ai_teacher(question, user=None):

    notes = load_notes()

    best_match = None

    max_score = 0

    q_words = question.lower().split()

    # ===========================
    # FIND BEST NOTE
    # ===========================

    for note in notes:

        content = clean_text(note["content"])

        score = 0

        for word in q_words:

            # content match
            if word in content:
                score += 2

            # topic match
            if word in note["topic"].lower():
                score += 5

            # subject match
            if word in note["subject"].lower():
                score += 3

        if score > max_score:

            max_score = score

            best_match = note

    # ===========================
    # NO ANSWER
    # ===========================

    if not best_match:

        return "📘 Answer கிடைக்கவில்லை.\n\n" "Try asking with more keywords 😄"

    # ===========================
    # EXTRACT ANSWER
    # ===========================

    lines = extract_best_lines(best_match["content"], question)

    answer = ""

    for i, line in enumerate(lines, start=1):

        answer += f"\n{i}. {line}\n"

    # ===========================
    # CONFIDENCE
    # ===========================

    confidence = min(max_score * 10, 100)

    # ===========================
    # WEAKNESS MEMORY
    # ===========================

    memory_note = ""

    if user:

        weak_data = get_weakness(user)

        topic_key = f"{best_match['subject']}" f"-{best_match['topic']}"

        if topic_key in weak_data:

            memory_note = "\n⚠️ You are weak in this topic." "\nRevise properly!"

    # ===========================
    # FINAL RESPONSE
    # ===========================

    return f"""

📘 {best_match['subject'].upper()}
- {best_match['topic']}

🎯 Confidence: {confidence}%

🧠 Answer:
{answer}

{memory_note}

🚀 Powered by Nova AI Teacher
"""


# ===============================
# EXPLAIN ANSWER
# ===============================


def explain_answer(question, correct, user_ans):

    return f"""

❌ Your Answer:
{user_ans.upper()}

✅ Correct Answer:
{correct.upper()}

📘 Explanation:

This question is important
for TNPSC exams.

Focus on key facts and
revise this topic properly.

🚀 Nova AI Analysis Complete
"""
