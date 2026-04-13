import json
import os
from datetime import date

FILE = "data/streak.json"

def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# 🔥 Update streak
def update_streak(user):

    data = load()
    today = str(date.today())

    if user not in data:
        data[user] = {
            "last_date": today,
            "streak": 1
        }
    else:
        last = data[user]["last_date"]

        if last == today:
            pass  # already updated

        else:
            data[user]["streak"] += 1
            data[user]["last_date"] = today

    save(data)
    return data[user]["streak"]

# 📊 Get streak
def get_streak(user):
    data = load()
    return data.get(user, {}).get("streak", 0)