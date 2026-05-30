import time

import streamlit as st


def reset_test_state():
    if "correct_streak" not in st.session_state:
        st.session_state.correct_streak = 0

    if "wrong_count" not in st.session_state:
        st.session_state.wrong_count = 0

    if "level" not in st.session_state:
        st.session_state.level = "easy"

    if "exam" not in st.session_state:
        st.session_state["exam"] = "group1"

    if "user" not in st.session_state:
        st.session_state["user"] = "satheeshkumar"

    if "start_time" not in st.session_state:
        st.session_state.start_time = 0

    if "test_active" not in st.session_state:
        st.session_state.test_active = False

    if "start_test" not in st.session_state:
        st.session_state.start_test = False

    if "test_qs" not in st.session_state:
        st.session_state.test_qs = []

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "mentor_notification" not in st.session_state:
        st.session_state["mentor_notification"] = False

    if "mentor_chat" not in st.session_state:
        st.session_state["mentor_chat"] = []

    if "answered" not in st.session_state:
        st.session_state.answered = False

    if "test_subject" not in st.session_state:
        st.session_state.test_subject = None

    if "test_topic" not in st.session_state:
        st.session_state.test_topic = None


def start_test():
    st.session_state.start_time = time.time()
    st.session_state.test_active = True
    st.session_state.score = 0
    st.session_state.q_index = 0


def finish_test():
    st.session_state.test_active = False
    st.session_state.test_qs = []
