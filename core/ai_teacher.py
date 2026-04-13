import os

BASE_PATH = "data/notes"

# -------------------------------
# LOAD NOTES
# -------------------------------
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

                    notes_data.append({
                        "subject": subject,
                        "topic": file.replace(".txt", ""),
                        "content": content
                    })

    return notes_data


# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):
    return text.lower().replace("\n", " ")


# -------------------------------
# FIND BEST SENTENCES 🔥
# -------------------------------
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

    # take top 3 lines
    best_lines = [line for score, line in scored[:3]]

    return best_lines


# -------------------------------
# AI TEACHER 🔥🔥
# -------------------------------
from core.weakness_ai import get_weakness

def ai_teacher(question, user=None):

    notes = load_notes()

    best_match = None
    max_score = 0

    q_words = question.lower().split()

    for note in notes:

        content = clean_text(note["content"])

        score = sum(1 for word in q_words if word in content)

        if score > max_score:
            max_score = score
            best_match = note

    if not best_match:
        return "📘 Answer கிடைக்கவில்லை."

    lines = extract_best_lines(best_match["content"], question)

    answer = "\n".join(lines)

    # 🔥 MEMORY ADD
    memory_note = ""

    if user:
        weak_data = get_weakness(user)

        topic_key = f"{best_match['subject']}-{best_match['topic']}"

        if topic_key in weak_data:
            memory_note = "\n\n⚠️ You are weak in this topic. Revise properly!"

    return f"""
📘 {best_match['subject'].upper()} - {best_match['topic']}

🧠 {answer}

{memory_note}
"""

def explain_answer(question, correct, user_ans):
    return f"""
❌ Your Answer: {user_ans.upper()}

✅ Correct Answer: {correct.upper()}

📘 Explanation:
This question is important for TNPSC exams. Focus on key facts and revise this topic properly.
"""