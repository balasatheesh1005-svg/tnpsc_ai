import json, os

FILE = "data/progress.json"

def load():
    if not os.path.exists(FILE):
        return {}
    return json.load(open(FILE))

def save(data):
    json.dump(data, open(FILE, "w"), indent=4)

# -------------------------------
# SAVE SCORE
# -------------------------------
def save_progress(user, subject, score):

    data = load()

    if user not in data:
        data[user] = {}

    if subject not in data[user]:
        data[user][subject] = []

    data[user][subject].append(score)

    save(data)


# -------------------------------
# GET SUBJECT PROGRESS
# -------------------------------
def get_progress(user):

    data = load()

    return data.get(user, {})