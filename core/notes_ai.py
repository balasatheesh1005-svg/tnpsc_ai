import json
import os


def load_notes(subject, topic):
    subject = subject.lower()
    topic = topic.lower()

    file_path = f"data/notes/{subject}/{topic}.json"

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
