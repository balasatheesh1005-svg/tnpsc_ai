from core.revision_ai import add_revision, update_revision


def _normalize_topic_key(subject, topic):
    topic = topic.lower().replace(" ", "_")
    return f"{subject}-{topic}"


def handle_correct_revision(user, subject, topic):
    update_revision(user, _normalize_topic_key(subject, topic))


def handle_wrong_revision(user, subject, topic):
    add_revision(user, _normalize_topic_key(subject, topic))
