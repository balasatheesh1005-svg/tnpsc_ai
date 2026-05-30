from core.weakness_ai import get_most_weak_topic
from core.revision_ai import get_revision_topics
from core.study_planner import get_today_plan


def get_smart_topic(user):

    weak_topic, count = get_most_weak_topic(user)

    if not weak_topic:
        return "polity-historical_background"

    return weak_topic
