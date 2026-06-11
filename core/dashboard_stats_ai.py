from core.streak_ai import get_streak
from core.supabase_client import supabase
from core.weakness_ai import get_weakness
from core.xp_ai import get_user_xp, get_level_progress


def get_tests_attempted(user, progress=None):
    return len(progress or [])


def get_average_accuracy(user, progress=None):
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


def get_weak_subject(user, weak_data=None):
    if not weak_data:
        return "No Data"

    weak_topic = max(weak_data, key=weak_data.get)
    return weak_topic.replace("-", " -> ")


def get_user_rank(user, all_progress=None):
    rows = all_progress
    if rows is None:
        response = (
            supabase.table("users_progress").select("username, accuracy").execute()
        )
        rows = response.data or []

    user_scores = {}

    for row in rows:
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
    progress_response = (
        supabase.table("users_progress").select("username, accuracy").execute()
    )
    all_progress = progress_response.data or []
    user_progress = [row for row in all_progress if row.get("username") == user]
    weak_data = get_weakness(user)
    xp_data = get_user_xp(user)
    level_progress = get_level_progress(user)

    return {
        "tests_attempted": get_tests_attempted(user, user_progress),
        "accuracy": get_average_accuracy(user, user_progress),
        "streak": get_streak(user),
        "weak_subject": get_weak_subject(user, weak_data),
        "rank": get_user_rank(user, all_progress),
        "xp": xp_data["xp"],
        "level": xp_data["level"],
        "level_progress": level_progress,
    }
