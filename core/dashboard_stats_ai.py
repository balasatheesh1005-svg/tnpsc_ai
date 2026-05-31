from core.progress_ai import get_progress
from core.streak_ai import get_streak
from core.supabase_client import supabase
from core.weakness_ai import get_weakness


def get_tests_attempted(user):
    progress = get_progress(user)
    return len(progress or [])


def get_average_accuracy(user):
    progress = get_progress(user)

    if not progress:
        return 0

    scores = []

    for row in progress:
        try:
            scores.append(float(row.get("accuracy", 0)))
        except (TypeError, ValueError):
            continue

    if not scores:
        return 0

    return round(sum(scores) / len(scores), 1)


def get_weak_subject(user):
    weak_data = get_weakness(user)

    if not weak_data:
        return "No Data"

    weak_topic = max(weak_data, key=weak_data.get)
    return weak_topic.replace("-", " -> ")


def get_user_rank(user):
    response = supabase.table("users_progress").select("username, accuracy").execute()

    user_scores = {}

    for row in response.data or []:
        username = row.get("username")

        if not username:
            continue

        try:
            accuracy = float(row.get("accuracy", 0))
        except (TypeError, ValueError):
            continue

        user_scores.setdefault(username, []).append(accuracy)

    leaderboard = []

    for username, scores in user_scores.items():
        avg_accuracy = sum(scores) / len(scores)
        leaderboard.append((username, avg_accuracy))

    leaderboard.sort(key=lambda item: (-item[1], item[0]))

    for index, item in enumerate(leaderboard, 1):
        username, _score = item

        if username == user:
            return index

    return 0


def get_dashboard_stats(user):
    return {
        "tests_attempted": get_tests_attempted(user),
        "accuracy": get_average_accuracy(user),
        "streak": get_streak(user),
        "weak_subject": get_weak_subject(user),
        "rank": get_user_rank(user),
    }
