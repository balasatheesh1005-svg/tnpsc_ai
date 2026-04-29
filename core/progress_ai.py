import json
import os

FILE = "data/progress.json"


def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ✅ SAVE PROGRESS
def save_progress(user, subject, topic, score):

    data = load_data()

    if user not in data:
        data[user] = {}

    if subject not in data[user]:
        data[user][subject] = {}

    if topic not in data[user][subject]:
        data[user][subject][topic] = []

    data[user][subject][topic].append(score)

    save_data(data)


# ✅ GET PROGRESS
def get_progress(user):

    data = load_data()

    return data.get(user, {})


import datetime


def save_note_progress(user, subject, topic):

    data = load()

    if user not in data:
        data[user] = {"scores": {}, "notes": {}}

    if "notes" not in data[user]:
        data[user]["notes"] = {}

    if subject not in data[user]["notes"]:
        data[user]["notes"][subject] = {}

    data[user]["notes"][subject][topic] = {
        "status": "completed",
        "last_read": str(datetime.date.today()),
    }

    save(data)
