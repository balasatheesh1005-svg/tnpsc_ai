import json
import os

import streamlit as st


@st.cache_data
def load_questions(subject, topic, level):
    subject = subject.lower()
    topic = topic.lower()

    file_path = f"data/questions/{subject}/{topic}_{level}.json"

    if not os.path.exists(file_path):
        print("âŒ Missing:", file_path)
        return []

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
