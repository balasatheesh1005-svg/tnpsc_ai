from core.supabase_client import supabase

TABLE = "users_progress"


# =========================
# GET TOP USERS
# =========================


def get_top_users():

    response = supabase.table(TABLE).select("username, accuracy").execute()

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
        leaderboard.append((username, round(avg_accuracy, 2)))

    leaderboard.sort(key=lambda x: x[1], reverse=True)

    return leaderboard[:10]
