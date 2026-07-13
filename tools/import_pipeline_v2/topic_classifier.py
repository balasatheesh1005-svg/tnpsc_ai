"""Conservative topic labels; blank when no reliable keyword is found."""
TOPICS = {"Polity": {"constitution": "Constitution", "parliament": "Parliament", "supreme court": "Judiciary"}, "History": {"freedom": "Freedom Movement", "dynasty": "Indian History"}, "Geography": {"river": "Rivers", "monsoon": "Climate"}, "Economy": {"inflation": "Inflation", "budget": "Budget"}, "Aptitude": {"percentage": "Percentage", "ratio": "Ratio and Proportion"}, "Reasoning": {"series": "Series", "coding": "Coding-Decoding"}}


def classify(question):
    text = str(question.get("question_en") or "").lower()
    for keyword, topic in TOPICS.get(question.get("subject"), {}).items():
        if keyword in text:
            return topic
    return ""
