import json
import os
import streamlit as st

from core.topics_loader import get_topic_metadata_by_id
from core.weakness_ai import get_weakness

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(os.path.dirname(CURRENT_DIR), "data", "notes")


def extract_en_text(obj):
    """Recursively extracts English text from the notes JSON structure, skipping Tamil content."""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, list):
        return " ".join([extract_en_text(i) for i in obj])
    if isinstance(obj, dict):
        if "en" in obj:
            return extract_en_text(obj["en"])
        return " ".join([extract_en_text(v) for k, v in obj.items() if k != "ta"])
    return ""


@st.cache_data
def load_notes():
    notes_data = []

    if not os.path.exists(BASE_PATH):
        return notes_data

    for subject in os.listdir(BASE_PATH):
        subject_path = os.path.join(BASE_PATH, subject)
        if not os.path.isdir(subject_path):
            continue

        for file in os.listdir(subject_path):
            if file.endswith(".json"):
                file_path = os.path.join(subject_path, file)
                try:
                    if os.path.getsize(file_path) == 0:
                        continue

                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        content = extract_en_text(data.get("content", {}))

                        note_file_stem = file.replace(".json", "")
                        meta = get_topic_metadata_by_id(subject, note_file_stem)

                        notes_data.append(
                            {
                                "subject": subject,
                                "topic_id": meta["topic_id"],
                                "repository_id": meta["repository_id"],
                                "display_title": meta["display_title"],
                                "content": content,
                            }
                        )
                except Exception as e:
                    print(f"⚠️ Warning: Skipping invalid note {file_path}. Error: {e}")
                    continue

    return notes_data


def clean_text(text):
    return text.lower().replace("\n", " ")


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

    scored.sort(reverse=True)
    return [line for score, line in scored[:3]]


def ai_teacher(question, user=None):
    notes = load_notes()
    best_match = None
    max_score = 0
    q_words = question.lower().split()

    for note in notes:
        content = clean_text(note["content"])
        score = 0

        for word in q_words:
            if word in content:
                score += 2
            if word in note["display_title"].lower():
                score += 5
            if word in note["subject"].lower():
                score += 3

        if score > max_score:
            max_score = score
            best_match = note

    if not best_match:
        return "📘 Answer கிடைக்கவில்லை.\n\nTry asking with more keywords 😄"

    lines = extract_best_lines(best_match["content"], question)
    answer = "".join([f"\n{i}. {line}\n" for i, line in enumerate(lines, start=1)])

    confidence = min(max_score * 10, 100)
    memory_note = ""

    if user:
        weak_data = get_weakness(user)
        repo_key = f"{best_match['subject']}-{best_match['repository_id']}"
        topic_key = f"{best_match['subject']}-{best_match['topic_id']}"

        if weak_data and (repo_key in weak_data or topic_key in weak_data):
            memory_note = "\n⚠️ You have a weak accuracy score in this topic area.\nRevise properly!"

    return f"""
📘 {best_match['subject'].upper()}
- {best_match['display_title']}

🎯 Confidence: {confidence}%

🧠 Answer:
{answer}
{memory_note}
🚀 Powered by Nova AI Teacher
"""


def explain_answer(question, correct, user_ans):
    return f"""
❌ Your Answer:
{user_ans.upper()}

✅ Correct Answer:
{correct.upper()}

📘 Explanation:
This question is important for TNPSC exams.
Focus on key facts and revise this topic properly.

🚀 Nova AI Analysis Complete
"""
