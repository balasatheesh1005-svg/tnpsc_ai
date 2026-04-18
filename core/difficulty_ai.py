def get_user_level(user):
    return "easy"


def get_next_level(current, correct_streak, wrong_count):

    # 🔥 upgrade faster
    if correct_streak >= 2:
        if current == "easy":
            return "medium"
        elif current == "medium":
            return "hard"

    # 🔥 downgrade
    if wrong_count >= 2:
        if current == "hard":
            return "medium"
        elif current == "medium":
            return "easy"

    return current