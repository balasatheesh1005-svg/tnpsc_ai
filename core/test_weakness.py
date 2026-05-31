import streamlit as st

from core.weakness_ai import add_weakness, reduce_weakness


def _normalize_topic(topic):
    return topic.lower().replace(" ", "_")


def handle_correct_answer(user, subject, topic):
    if topic:

        topic = _normalize_topic(topic)

    else:

        st.error("No weak topic available.")

        st.stop()

    reduce_weakness(user, subject, topic)  # ✅ ONLY HERE

    return topic


def handle_wrong_answer(user, subject, topic):
    topic = _normalize_topic(topic)

    st.session_state["weak_subject"] = st.session_state.test_topic

    add_weakness(user, subject, topic)  # ✅ ONLY HERE

    return topic
