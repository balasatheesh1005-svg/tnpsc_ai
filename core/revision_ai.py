import json, os
import datetime
from core.utils import load_json, save_json

FILE = "data/revision.json"


def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_revision_topics(user):
    data = load()
    return data.get(user, [])


def add_revision(user, topic_key):
    data = load_json("revision.json")

    if user not in data:
        data[user] = {}

    data[user][topic_key] = {
        "level": 1,
        "next_due": str(datetime.date.today() + datetime.timedelta(days=1)),
    }

    save_json("revision.json", data)


def update_revision(user, topic_key):
    data = load_json("revision.json")

    if user not in data or topic_key not in data[user]:
        return

    level = data[user][topic_key]["level"]

    level += 1
    level = min(level, 5)

    days_map = {1: 1, 2: 3, 3: 7, 4: 15, 5: 30}

    next_due = datetime.date.today() + datetime.timedelta(days=days_map[level])

    data[user][topic_key] = {"level": level, "next_due": str(next_due)}

    save_json("revision.json", data)


def get_due_revisions(user):
    data = load_json("revision.json")

    if user not in data:
        return []

    today = datetime.date.today()
    due = []

    for topic, info in data[user].items():
        due_date = datetime.date.fromisoformat(info["next_due"])

        if due_date <= today:
            due.append({"topic": topic, "next_due": info["next_due"]})

    return due
