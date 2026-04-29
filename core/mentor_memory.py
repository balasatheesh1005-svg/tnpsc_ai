import json
import os

FILE = "data/mentor_memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_memory(user, score, total, weak_data):
    data = load_memory()

    percent = int((score / total) * 100) if total else 0

    if user not in data:
        data[user] = {}

    data[user]["last_score"] = percent
    data[user]["weak_topics"] = list(weak_data.keys())[:3]

    save_memory(data)

def get_memory(user):
    data = load_memory()
    return data.get(user, {})