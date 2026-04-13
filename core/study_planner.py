from core.weakness_ai import get_most_weak_topic

def get_today_plan(user):

    weak = get_most_weak_topic(user)

    if weak:
        return {
            "topic": weak,
            "questions": 10,
            "mode": "Weakness Focus 🔥"
        }

    return {
        "topic": "polity-historical_background",
        "questions": 5,
        "mode": "Normal Study"
    }