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
        elif isinstance(value, dict) and "en" in value and isinstance(value["en"], list):
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


# 💰 ECONOMY UI
def render_economy(content):
    st.markdown("## 📊 Key Concepts")

    for sec in content.get("sections", []):

        st.subheader(f"📌 {sec.get('title')}")

        tab1, tab2 = st.tabs(["EN", "TA"])

        with tab1:
            for p in sec.get("points", {}).get("en", []):
                st.write("•", p)

        with tab2:
            for p in sec.get("points", {}).get("ta", []):
                st.write("•", p)

        st.markdown("---")


# 🏛 HISTORY UI (same as economy structure)
def render_history(content):

    st.markdown("## 🏺 Key Topics")

    for sec in content.get("sections", []):

        st.subheader(f"📌 {sec.get('title')}")

        tab1, tab2 = st.tabs(["EN", "TA"])

        with tab1:
            for p in sec.get("points", {}).get("en", []):
                st.write("•", p)

        with tab2:
            for p in sec.get("points", {}).get("ta", []):
                st.write("•", p)

        st.markdown("---")
    if "timeline" in content:
        st.markdown("## ⏳ Timeline")
        for t in content["timeline"]:
            st.write("•", t)


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
