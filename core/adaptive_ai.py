from core.weakness_ai import get_weakness
from core.questions import load_questions
import random

# -------------------------------
# GET WEAK TOPIC FIRST 🔥
# -------------------------------
def get_adaptive_topic(user):

    weak_data = get_weakness(user)

    if not weak_data:
        return None

    # highest weak topic
    top_topic = max(weak_data, key=weak_data.get)

    return top_topic

# -------------------------------
# GET ADAPTIVE QUESTIONS 🔥
# -------------------------------
def generate_adaptive_questions(user, qcount=5):

    weak_data = get_weakness(user)

    # 👉 weak topic இருந்தா
    if weak_data:

        weak_topic = max(weak_data, key=weak_data.get)

        subject, topic = weak_topic.split("-")

        questions = load_questions(subject, topic)

        if questions:
            return random.sample(questions, min(len(questions), qcount))

    # 👉 fallback (no weakness)
    questions = load_questions("polity", "historical_background")

    return random.sample(questions, min(len(questions), qcount))