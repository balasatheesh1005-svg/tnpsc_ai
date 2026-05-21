import json
import os

FILE = "data/progress.json"


def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)


import json
import os


def get_top_users():

    progress_file = "data/progress.json"

    if not os.path.exists(progress_file):
        return []

    with open(progress_file, "r", encoding="utf-8") as f:
        progress = json.load(f)

    leaderboard = []

    for user, subjects in progress.items():

        all_scores = []

        for subject, topics in subjects.items():

            if isinstance(topics, dict):

                for topic, scores in topics.items():

                    if isinstance(scores, list):
                        all_scores.extend(scores)

            elif isinstance(topics, list):

                all_scores.extend(topics)

        clean_scores = []

        for s in all_scores:

            try:
                clean_scores.append(float(s))
            except:
                pass

        if clean_scores:
            avg = sum(clean_scores) / len(clean_scores)
        else:
            avg = 0

        leaderboard.append((user, round(avg, 2)))

    leaderboard.sort(key=lambda x: x[1], reverse=True)

    return leaderboard[:10]
