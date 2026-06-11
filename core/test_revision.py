from core.revision_ai import add_revision_topic, update_revision
from core.xp_ai import add_xp


def _normalize_topic_key(subject, topic):
    topic = topic.lower().replace(" ", "_")
    return f"{subject}-{topic}"


def handle_correct_revision(user, subject, topic):
    update_revision(user, _normalize_topic_key(subject, topic))

    # 🔥 Award XP for revision completion
    add_xp(user, 20, reward_type="revision_completion")


def handle_wrong_revision(user, subject, topic):
    add_revision_topic(user, subject, topic)
