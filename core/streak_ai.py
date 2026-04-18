import json, os
from datetime import datetime

FILE = "data/streak.json"

def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_streak(user):
    data = load()

    today = datetime.now().strftime("%Y-%m-%d")

    if user not in data:
        data[user] = {"last_date": today, "streak": 1}
    else:
        last_date = data[user]["last_date"]

        if last_date == today:
            return data[user]["streak"]

        from datetime import timedelta
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        if last_date == yesterday:
            data[user]["streak"] += 1
        else:
            data[user]["streak"] = 1

        data[user]["last_date"] = today

    save(data)
    return data[user]["streak"]

def get_streak(user):
    data = load()
    return data.get(user, {}).get("streak", 0)