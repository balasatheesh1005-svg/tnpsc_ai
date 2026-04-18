from core.weakness_ai import get_most_weak_topic
from core.revision_ai import get_revision_topics
from core.study_planner import get_today_plan

def get_smart_topic(user):

    # 💀 Weak topic first
    weak_topic, count = get_most_weak_topic(user)

    if weak_topic and count >= 2:
        return str(weak_topic), "weak"

    # 🔁 Revision next
    rev = get_revision_topics(user)
    if rev:
        return rev[0], "revision"

    # 📘 Normal plan
    plan = get_today_plan(user)

    if isinstance(plan, list):
        topic = plan[0]
    else:
        topic = plan.get("topic", "polity-historical_background")

    return topic, "normal"
