import json, os

FILE = "data/leaderboard.json"

def load():
    if not os.path.exists(FILE):
        return {}
    return json.load(open(FILE))

def save(data):
    json.dump(data, open(FILE, "w"), indent=4)

def update_leaderboard(user, score):

    data = load()

    if user not in data:
        data[user] = []

    data[user].append(score)

    save(data)

def get_top_users():

    data = load()

    avg_scores = []

    for user, scores in data.items():
        avg = sum(scores) / len(scores)
        avg_scores.append((user, avg))

    return sorted(avg_scores, key=lambda x: x[1], reverse=True)[:5]