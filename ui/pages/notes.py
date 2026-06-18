import json
import re
import time
from pathlib import Path

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
    topic = re.sub(r"[^a-z0-9_ ]", "", topic)
    return topic.replace(" ", "_")


def render_notes_page(section):
    section("📘 Notes Section")

    # Debug marker to confirm Notes page render
    st.write("NOTES PAGE RENDERED")

    # ---------------- SUBJECT ----------------

    notes_root = Path("data/notes")

    subjects = sorted([p.name for p in notes_root.iterdir() if p.is_dir()])

    subject = st.selectbox("Select Subject", subjects)

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

    # DEBUG OUTPUTS
    st.write(f"DEBUG: Selected Topic: {topic}")
    st.write(f"DEBUG: Generated File Path: {file_path}")

    # ---------------- LOAD NOTE ----------------

    try:
        data = load_note(file_path)

        # DEBUG OUTPUTS
        st.write(f"DEBUG: Loaded UI Type: {data.get('ui_type')}")
        st.write(f"DEBUG: Content Keys: {list(data.get('content', {}).keys())}")

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
        st.session_state.notes_practice_trigger = True

        st.success("✅ Topic Prepared for Practice")
        st.info("🚀 Open **Daily Test** from the sidebar to begin your session.")
