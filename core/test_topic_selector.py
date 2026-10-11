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

    level = st.session_state.get("level", "easy") if hasattr(st, "session_state") else "easy"

    return {"subject": subject, "topic": topic, "level": level}


def _get_weak_test_config(user):
    weak = get_weakness(user)
    if not weak:
        return None

    topic = sorted(weak.items(), key=lambda x: x[1], reverse=True)[0][0]

    if "-" not in topic:
        topic = f"polity-{topic}"

    parts = topic.split("-", 1)
    subject = parts[0]
    topic = parts[1] if len(parts) > 1 else parts[0]

    level = get_user_level(user)

    return {"subject": subject, "topic": topic, "level": level}


def _get_revision_test_config(user):
    topics = get_due_revisions(user)

    # =========================
    # NO REVISIONS
    # =========================

    if not topics:
        return None

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

    level = st.session_state.get("level", "easy") if hasattr(st, "session_state") else "easy"

    return {"subject": subject, "topic": topic, "level": level}


def start_practice_test(
    subject: str,
    topic: str,
    level: str = "easy",
    mode: str = "daily",
    q_count: int = 10,
    navigate: bool = False,
):
    """
    Safely starts a test session only if questions are available.
    Returns (True, "") on success, or (False, error_message) on failure.
    Ensures test_active is never set to True with empty questions.
    """
    from core.question_loader import load_questions

    clean_subject = (subject or "polity").lower().strip()
    clean_topic = (topic or "historical_background").lower().strip().replace(" ", "_")
    clean_level = (level or "easy").lower().strip()

    questions = load_questions(clean_subject, clean_topic, clean_level)
    if not questions and clean_level != "easy":
        # Safe fallback: attempt foundation/easy tier if specific qtype has no dedicated file
        questions = load_questions(clean_subject, clean_topic, "easy")

    if not questions:
        return False, "No questions found for this topic."

    sample_size = min(q_count, len(questions))
    selected_qs = random.sample(questions, sample_size)

    if hasattr(st, "session_state"):
        st.session_state.update(
            {
                "q_index": 0,
                "score": 0,
                "answered": False,
                "test_active": True,
                "test_mode": mode,
                "test_results_processed": False,
                "test_start_xp": st.session_state.get("xp", 0),
                "test_subject": clean_subject,
                "test_topic": clean_topic,
            }
        )
        st.session_state.test_qs = selected_qs

        if navigate:
            st.session_state["navigate_to"] = "🔥 Daily Challenge"
            st.session_state["main_menu"] = "🔥 Daily Challenge"
            if "sidebar_main_menu" in st.session_state:
                st.session_state["sidebar_main_menu"] = "🔥 Daily Challenge"

    return True, ""
