import streamlit as st
import datetime


def render_practice_button(subject, topic):
    st.markdown("---")


# 🔥 MAIN ENTRY
def render_notes(data):
    st.info(f"📘 {data.get('topic')}")
    content = data.get("content", {})
    ui_type = data.get("ui_type", "default")

    render_definition(content)

    if ui_type == "polity":
        render_polity(content)

    elif ui_type == "economy":
        render_economy(content)

    elif ui_type == "history":
        render_history(content)

    render_mcqs(content)
    render_practice_button(data.get("subject"), data.get("topic"))


# 📘 DEFINITION (COMMON FOR ALL)
def render_definition(content):
    st.markdown("## 📘 Definition")

    tab1, tab2 = st.tabs(["English", "தமிழ்"])

    with tab1:
        st.write(content.get("definition", {}).get("en", ""))

    with tab2:
        st.write(content.get("definition", {}).get("ta", ""))


# 🏛 POLITY UI
def render_polity(content):

    def render_section(title, value):

        st.markdown(f"## 📜 {title.capitalize()}")

        # 🔹 Case 1: Definition (en/ta text)
        if isinstance(value, dict) and "en" in value and isinstance(value["en"], str):
            tab1, tab2 = st.tabs(["EN", "TA"])

            with tab1:
                st.write(value.get("en", ""))

            with tab2:
                st.write(value.get("ta", ""))

        # 🔹 Case 2: Points dict (importance type)
        elif (
            isinstance(value, dict) and "en" in value and isinstance(value["en"], list)
        ):
            tab1, tab2 = st.tabs(["EN", "TA"])

            with tab1:
                for p in value.get("en", []):
                    st.write("•", p)

            with tab2:
                for p in value.get("ta", []):
                    st.write("•", p)

        # 🔹 Case 3: List (keywords, objectives)
        elif isinstance(value, list):
            for item in value:
                st.subheader(f"📌 {item.get('title')}")

                tab1, tab2 = st.tabs(["EN", "TA"])

                with tab1:
                    for p in item.get("points", {}).get("en", []):
                        st.write("•", p)

                with tab2:
                    for p in item.get("points", {}).get("ta", []):
                        st.write("•", p)

                st.markdown("---")

        # 🔹 Case 4: Mind map (skip or custom render)
        elif title == "mind_map":
            st.info("Mind map UI coming soon 🔥")

        else:
            st.write(value)

        st.markdown("---")

    # 🔥 Loop all sections
    for key, value in content.items():
        render_section(key, value)


def render_economy(content):

    st.title("💰 Economy Notes")

    # =========================
    # Definition
    # =========================
    if "definition" in content:
        st.subheader("📘 Definition")

        tab1, tab2 = st.tabs(["EN", "TA"])

        with tab1:
            st.info(content["definition"].get("en", ""))
        with tab2:
            st.info(content["definition"].get("ta", ""))


import streamlit as st


def render_economy(content):

    st.title("💰 Economy Notes")

    # =========================
    # Definition
    # =========================
    if "definition" in content:

        st.subheader("📘 Definition")

        tab1, tab2 = st.tabs(["EN", "TA"])

        with tab1:
            st.info(content["definition"].get("en", ""))

        with tab2:
            st.info(content["definition"].get("ta", ""))

        st.markdown("---")

    # =========================
    # Generic Dynamic Renderer
    # =========================
    skip_keys = ["definition", "important_facts", "current_affairs", "mind_map"]

    for key, value in content.items():

        if key in skip_keys:
            continue

        if isinstance(value, list):

            section_title = key.replace("_", " ").title()

            st.header(f"📌 {section_title}")

            for item in value:

                title = item.get("title", "")

                if title:
                    st.subheader(f"🔹 {title}")

                tab1, tab2 = st.tabs(["EN", "TA"])

                with tab1:
                    for point in item.get("points", {}).get("en", []):
                        st.write("•", point)

                with tab2:
                    for point in item.get("points", {}).get("ta", []):
                        st.write("•", point)

                st.markdown("---")

    # =========================
    # Important Facts
    # =========================
    if "important_facts" in content:

        st.header("⭐ Important Facts")

        tab1, tab2 = st.tabs(["EN", "TA"])

        with tab1:
            for point in content["important_facts"].get("en", []):
                st.success(point)

        with tab2:
            for point in content["important_facts"].get("ta", []):
                st.success(point)

        st.markdown("---")

    # =========================
    # Current Affairs
    # =========================
    if "current_affairs" in content:

        st.header("📰 Current Affairs")

        for item in content["current_affairs"]:

            st.subheader(f"🟢 {item.get('title', '')}")

            tab1, tab2 = st.tabs(["EN", "TA"])

            with tab1:
                for point in item.get("points", {}).get("en", []):
                    st.write("•", point)

            with tab2:
                for point in item.get("points", {}).get("ta", []):
                    st.write("•", point)

            st.markdown("---")


# 🏛 HISTORY UI (same as economy structure)
import streamlit as st


def render_history(content):

    st.title("🏛️ History Notes")

    # ====================================
    # Definition / Introduction
    # ====================================

    if "definition" in content:

        st.subheader("📘 Definition")

        tab1, tab2 = st.tabs(["EN", "TA"])

        with tab1:
            st.info(content["definition"].get("en", ""))

        with tab2:
            st.info(content["definition"].get("ta", ""))

        st.markdown("---")

    # ====================================
    # Dynamic Sections
    # ====================================

    skip_keys = [
        "definition",
        "important_facts",
        "timeline",
        "current_affairs",
        "mind_map",
    ]

    for key, value in content.items():

        if key in skip_keys:
            continue

        if isinstance(value, list):

            section_title = key.replace("_", " ").title()

            st.header(f"📌 {section_title}")

            for item in value:

                title = item.get("title", "")

                if title:
                    st.subheader(f"🔹 {title}")

                tab1, tab2 = st.tabs(["EN", "TA"])

                # English
                with tab1:

                    for point in item.get("points", {}).get("en", []):
                        st.write("•", point)

                # Tamil
                with tab2:

                    for point in item.get("points", {}).get("ta", []):
                        st.write("•", point)

                st.markdown("---")

    # ====================================
    # Timeline
    # ====================================

    if "timeline" in content:

        st.header("⏳ Timeline")

        for item in content["timeline"]:

            year = item.get("year", "")
            event = item.get("event", "")

            st.markdown(f"✅ **{year}** → {event}")

        st.markdown("---")

    # ====================================
    # Important Facts
    # ====================================

    if "important_facts" in content:

        st.header("⭐ Important Facts")

        tab1, tab2 = st.tabs(["EN", "TA"])

        with tab1:

            for point in content["important_facts"].get("en", []):
                st.success(point)

        with tab2:

            for point in content["important_facts"].get("ta", []):
                st.success(point)

        st.markdown("---")

    # ====================================
    # Current Affairs Connection
    # ====================================

    if "current_affairs" in content:

        st.header("📰 Current Affairs Link")

        for item in content["current_affairs"]:

            st.subheader(f"🟢 {item.get('title', '')}")

            tab1, tab2 = st.tabs(["EN", "TA"])

            with tab1:

                for point in item.get("points", {}).get("en", []):
                    st.write("•", point)

            with tab2:

                for point in item.get("points", {}).get("ta", []):
                    st.write("•", point)

            st.markdown("---")

    # ====================================
    # Mind Map
    # ====================================

    if "mind_map" in content:

        st.header("🧠 Mind Map")

        for item in content["mind_map"]:
            st.markdown(f"- {item}")

        st.markdown("---")


# ❓ MCQ SECTION (COMMON)
def render_mcqs(content):

    mcqs = content.get("mcqs", [])

    if not mcqs:
        return

    st.markdown("## ❓ Practice Questions")

    for i, q in enumerate(mcqs, 1):
        st.markdown(f"**Q{i}. {q.get('question_en')}**")

        for opt in q.get("options", []):
            st.write("▫️", opt)

        st.success(f"✅ Answer: {q.get('answer')}")
