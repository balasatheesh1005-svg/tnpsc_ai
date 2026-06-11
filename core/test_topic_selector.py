import datetime
import random

import streamlit as st

from core.difficulty_ai import get_user_level
from core.revision_ai import get_due_revisions
from core.smart_selector import get_smart_topic
from core.weakness_ai import get_weakness


def get_test_config(user, mode="smart"):
    if mode == "weak":
        return _get_weak_test_config(user)

    if mode == "revision":
        return _get_revision_test_config(user)

    return _get_smart_test_config(user)


def _get_smart_test_config(user):
    topic_data = get_smart_topic(user)

    # 🔥 Flatten tuple completely
    while isinstance(topic_data, tuple):
        topic_data = topic_data[0]

    topic_key = topic_data

    if not topic_key:
        topic_key = "polity-historical_background"

    parts = topic_key.split("-")
    if len(parts) == 2:
        subject, topic = parts
    else:
        subject = "polity"  # default
        topic = parts[0]

    topic = topic.lower().replace(" ", "_")

    level = st.session_state.level

    return {"subject": subject, "topic": topic, "level": level}


def _get_weak_test_config(user):
    weak = get_weakness(user)
    if not weak:
        st.warning("No weak topics")
        st.stop()

    topic = sorted(weak.items(), key=lambda x: x[1], reverse=True)[0][0]

    if "-" not in topic:
        topic = f"polity-{topic}"

    subject, topic = topic.split("-")

    level = get_user_level(user)

    return {"subject": subject, "topic": topic, "level": level}


def _get_revision_test_config(user):
    topics = get_due_revisions(user)

    # =========================
    # NO REVISIONS
    # =========================

    if not topics:

        st.success("🔥 No revisions due!")

        st.stop()

    # =========================
    # PICK REVISION
    # =========================

    topic_key, next_due = random.choice(topics)

    try:
        due_date = datetime.date.fromisoformat(str(next_due))
    except (TypeError, ValueError):
        due_date = datetime.date.today()

    today = datetime.date.today()

    days_left = (due_date - today).days

    # =========================
    # REVISION STATUS
    # =========================

    st.info(f"📅 Next Revision: {next_due}")

    st.warning(f"⏳ Days Left: {days_left}")

    if days_left == 0:

        st.error("🔥 Revision due TODAY!")

    elif days_left <= 2:

        st.warning("⚠️ Upcoming revision soon")

    # =========================
    # SPLIT SUBJECT/TOPIC
    # =========================

    if "-" in topic_key:
        subject, topic = topic_key.split("-", 1)
    else:
        subject = "polity"
        topic = topic_key

    # =========================
    # DISPLAY TOPIC
    # =========================

    display_topic = topic.replace("_", " ").title()

    st.success(f"📚 Revision Topic: " f"{display_topic}")

    st.info(f"📅 Next Revision Date: " f"{next_due}")

    # =========================
    # LEVEL
    # =========================

    level = st.session_state.level

    return {"subject": subject, "topic": topic, "level": level}
