import json
import re
import time

import streamlit as st

from core.question_loader import load_questions
from core.streamlit_ui_engine import render_notes
from core.topics_loader import get_topics


@st.cache_data
def load_note(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def format_topic(topic):
    topic = topic.lower()
    topic = re.sub(r"[^a-z0-9 ]", "", topic)
    return topic.replace(" ", "_")


def render_notes_page(section):
    section("📘 Notes Section")

    # Debug marker to confirm Notes page render
    st.write("NOTES PAGE RENDERED")

    # ---------------- SUBJECT ----------------

    subject = st.selectbox("Select Subject", ["polity", "economy", "history"])

    # ---------------- TOPICS ----------------

    try:

        topics = get_topics(subject)

        if not topics:
            st.warning("No topics found")
            st.stop()

    except Exception as e:

        st.error("❌ Structure JSON Error")
        st.error(e)

        st.stop()

    # ---------------- TOPIC ----------------

    topic = st.selectbox("Select Topic", topics)

    # ---------------- FILE PATH ----------------

    topic_key = format_topic(topic)

    file_path = f"data/notes/" f"{subject}/" f"{topic_key}.json"

    # ---------------- LOAD NOTE ----------------

    try:

        data = load_note(file_path)

        # 🔥 MAIN RENDER ENGINE
        render_notes(data)

        st.caption(f"UI Type: " f"{data.get('ui_type', 'unknown')}")

    except FileNotFoundError:

        st.warning("📭 Notes not available yet")

    except Exception as e:

        st.error("❌ Error loading notes")
        st.exception(e)

    # ---------------- PRACTICE BUTTON ----------------

    if st.button("🧠 Practice from this Topic"):

        st.session_state.test_subject = subject

        st.session_state.test_topic = topic_key

        st.session_state.start_test = True

        st.session_state.start_time = time.time()

        st.session_state.progress_saved = False

        questions = load_questions(subject, topic_key, "easy")
        question_count = min(5, len(questions)) if questions is not None else 0

        st.success("✅ Practice Test Ready")
        st.info(
            f"📘 {question_count} questions generated from this topic.\n\n"
            "🚀 Open Daily Test from the sidebar and start practicing."
        )
        if hasattr(st, "toast"):
            st.toast(f"🚀 {question_count} Questions loaded successfully!")
