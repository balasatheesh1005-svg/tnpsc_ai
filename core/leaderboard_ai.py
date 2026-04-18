import json, os

FILE = "data/progress.json"

def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def get_top_users(limit=10):
    data = load()

    scores = []

    for user, subjects in data.items():
        all_scores = []
        for s in subjects.values():
            all_scores.extend(s)

        if all_scores:
            avg = sum(all_scores) / len(all_scores)
            scores.append((user, avg))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:limit]