from core.weakness_ai import get_weakness


# -------------------------------
# GET REVISION TOPICS 🔁
# -------------------------------
def get_revision_topics(user):

    weak_data = get_weakness(user)

    if not weak_data:
        return []

    # sort by highest weakness
    sorted_topics = sorted(
        weak_data.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # take top 3 weak topics
    top_weak = [topic for topic, count in sorted_topics[:3]]

    return top_weak