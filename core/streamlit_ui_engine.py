import streamlit as st
import datetime


def render_practice_button(subject, topic):
    st.markdown("---")


from ui.notes.renderer import render_notes_engine


# 🔥 MAIN ENTRY
def render_notes(data):
    render_notes_engine(data)


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


def render_aptitude(content):
    st.title("🔢 Aptitude Notes")

    # 1. 📘 Definition
    if "definition" in content and (
        content["definition"].get("en") or content["definition"].get("ta")
    ):
        st.subheader("📘 Definition")
        tab1, tab2 = st.tabs(["EN", "TA"])
        with tab1:
            st.info(content["definition"].get("en", ""))
        with tab2:
            st.info(content["definition"].get("ta", ""))
        st.markdown("---")

    # ====================================
    # Formula Sheet
    # ====================================
    if "formula_sheet" in content:
        st.header("📌 Formula Sheet")
        for item in content["formula_sheet"]:
            title = item.get("title", "")
            if title:
                st.subheader(f"🔹 {title}")
            tab1, tab2 = st.tabs(["EN", "TA"])
            with tab1:
                st.info(f"**Formula:** {item.get('formula', '')}")
                st.write(item.get("explanation", {}).get("en", ""))
            with tab2:
                st.info(f"**சூத்திரம்:** {item.get('formula', '')}")
                st.write(item.get("explanation", {}).get("ta", ""))
            st.markdown("---")

    # ====================================
    # Shortcut Tricks
    # ====================================
    if "shortcut_tricks" in content:
        st.header("⚡ Shortcut Tricks")
        for item in content["shortcut_tricks"]:
            title = item.get("title", "")
            if title:
                st.subheader(f"🔸 {title}")
            tab1, tab2 = st.tabs(["EN", "TA"])
            with tab1:
                for point in item.get("points", {}).get("en", []):
                    st.success(point)
            with tab2:
                for point in item.get("points", {}).get("ta", []):
                    st.success(point)
            st.markdown("---")

    # ====================================
    # Exam Traps
    # ====================================
    if "exam_traps" in content:
        st.header("🔥 Exam Traps")
        for item in content["exam_traps"]:
            title = item.get("title", "")
            if title:
                st.subheader(f"⚠️ {title}")
            tab1, tab2 = st.tabs(["EN", "TA"])
            with tab1:
                for point in item.get("points", {}).get("en", []):
                    st.warning(point)
            with tab2:
                for point in item.get("points", {}).get("ta", []):
                    st.warning(point)
            st.markdown("---")

    # ====================================
    # Solved Examples
    # ====================================
    if "solved_examples" in content:
        st.header("📝 Solved Examples")
        for item in content["solved_examples"]:
            with st.expander(f"📖 {item.get('title', 'Solved Example')}"):
                tab1, tab2 = st.tabs(["EN", "TA"])
                with tab1:
                    st.write("**Question:**", item.get("question", {}).get("en", ""))
                    st.write("**Step 1:**", item.get("step1", {}).get("en", ""))
                    st.write("**Step 2:**", item.get("step2", {}).get("en", ""))
                    st.write("**Step 3:**", item.get("step3", {}).get("en", ""))
                    st.write("**Final Answer:**", item.get("answer", {}).get("en", ""))
                with tab2:
                    st.write("**வினா:**", item.get("question", {}).get("ta", ""))
                    st.write("**படி 1:**", item.get("step1", {}).get("ta", ""))
                    st.write("**படி 2:**", item.get("step2", {}).get("ta", ""))
                    st.write("**படி 3:**", item.get("step3", {}).get("ta", ""))
                    st.write("**இறுதி விடை:**", item.get("answer", {}).get("ta", ""))
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
    # Mind Map
    # ====================================
    if "mind_map" in content:
        st.header("🧠 Mind Map")
        for item in content["mind_map"]:
            st.markdown(f"- {item}")
        st.markdown("---")


def render_aptitude(content):
    st.title("🔢 Aptitude Notes")

    def has_value(value):
        if value is None:
            return False
        if isinstance(value, str):
            return bool(value.strip())
        if isinstance(value, (list, tuple, dict)):
            return bool(value)
        return True

    def as_list(value):
        if value is None:
            return []
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        return [value]

    def text_value(value, lang="en", fallback=""):
        if isinstance(value, dict):
            return (
                value.get(lang)
                or value.get(f"{lang}_text")
                or value.get(f"content_{lang}")
                or value.get(f"title_{lang}")
                or fallback
            )
        return value if value is not None else fallback

    def title_value(item, fallback=""):
        if not isinstance(item, dict):
            return fallback
        return item.get("title") or item.get("title_en") or item.get("name") or fallback

    def render_points(points, writer=st.write):
        for point in as_list(points):
            if not has_value(point):
                continue
            if isinstance(point, dict):
                value = (
                    point.get("text")
                    or point.get("content")
                    or point.get("point")
                    or point.get("en")
                    or point.get("ta")
                )
                if has_value(value):
                    writer(value)
            else:
                writer(point)

    def render_bilingual_text_section(title, value, writer=st.info):
        if not has_value(value):
            return
        st.header(title)
        tab1, tab2 = st.tabs(["EN", "TA"])
        with tab1:
            render_points(text_value(value, "en"), writer)
        with tab2:
            render_points(text_value(value, "ta"), writer)
        st.markdown("---")

    def render_bilingual_list_section(title, items, icon="🔹", writer=st.write):
        if not has_value(items):
            return
        st.header(title)
        for item in as_list(items):
            if isinstance(item, dict):
                item_title = title_value(item)
                if item_title:
                    st.subheader(f"{icon} {item_title}")

                tab1, tab2 = st.tabs(["EN", "TA"])
                with tab1:
                    points = (
                        item.get("points", {}).get("en", [])
                        if isinstance(item.get("points"), dict)
                        else item.get("content_en")
                        or item.get("en")
                        or item.get("content")
                        or item.get("text")
                    )
                    render_points(points, writer)
                with tab2:
                    points = (
                        item.get("points", {}).get("ta", [])
                        if isinstance(item.get("points"), dict)
                        else item.get("content_ta") or item.get("ta")
                    )
                    render_points(points, writer)
            else:
                writer(item)
            st.markdown("---")

    # 1. 📘 Definition
    render_bilingual_text_section("📘 Definition", content.get("definition"), st.info)

    # 2. 🎯 Exam Importance
    render_bilingual_text_section(
        "🎯 Exam Importance", content.get("exam_importance"), st.info
    )

    # 3. 📌 Formula Sheet
    formula_sheet = content.get("formula_sheet", [])
    if has_value(formula_sheet):
        st.header("📌 Formula Sheet")
        for item in as_list(formula_sheet):
            if isinstance(item, dict):
                title = title_value(item)
                if title:
                    st.subheader(f"🔹 {title}")

                tab1, tab2 = st.tabs(["EN", "TA"])
                with tab1:
                    if has_value(item.get("formula")):
                        st.info(f"**Formula:** {item.get('formula', '')}")
                    render_points(
                        (
                            item.get("explanation", {}).get("en", [])
                            if isinstance(item.get("explanation"), dict)
                            else item.get("explanation")
                            or item.get("content_en")
                            or item.get("en")
                        ),
                        st.write,
                    )
                with tab2:
                    if has_value(item.get("formula")):
                        st.info(f"**சூத்திரம்:** {item.get('formula', '')}")
                    render_points(
                        (
                            item.get("explanation", {}).get("ta", [])
                            if isinstance(item.get("explanation"), dict)
                            else item.get("content_ta") or item.get("ta")
                        ),
                        st.write,
                    )
            else:
                st.info(item)
            st.markdown("---")

    # 4. 🧠 Core Concepts
    render_bilingual_list_section(
        "🧠 Core Concepts", content.get("core_concepts", []), "🔹", st.write
    )

    # 5. ⚡ Shortcut Tricks
    shortcut_tricks = content.get("shortcut_tricks") or content.get("exam_tricks", [])
    render_bilingual_list_section(
        "⚡ Shortcut Tricks", shortcut_tricks, "🔸", st.success
    )

    # 6. 🔥 Exam Traps
    render_bilingual_list_section(
        "🔥 Exam Traps", content.get("exam_traps", []), "⚠️", st.warning
    )

    # 7. 📝 Solved Examples
    solved_examples = content.get("solved_examples", [])
    if has_value(solved_examples):
        st.header("📝 Solved Examples")
        for index, item in enumerate(as_list(solved_examples), 1):
            if not isinstance(item, dict):
                st.write(item)
                continue

            title = title_value(item, f"Solved Example {index}")
            with st.expander(f"📖 {title}"):
                tab1, tab2 = st.tabs(["EN", "TA"])
                with tab1:
                    st.write(
                        "**Question:**",
                        text_value(
                            item.get("question"), "en", item.get("question", "")
                        ),
                    )
                    for step_key in ["step1", "step2", "step3"]:
                        step = text_value(item.get(step_key), "en", "")
                        if has_value(step):
                            st.write(f"**{step_key.replace('step', 'Step ')}:**", step)
                    solution = text_value(item.get("solution"), "en", "")
                    if has_value(solution):
                        st.write("**Solution:**", solution)
                    st.write(
                        "**Final Answer:**",
                        text_value(item.get("answer"), "en", item.get("answer", "")),
                    )
                with tab2:
                    st.write("**வினா:**", text_value(item.get("question"), "ta", ""))
                    for label, step_key in [
                        ("படி 1", "step1"),
                        ("படி 2", "step2"),
                        ("படி 3", "step3"),
                    ]:
                        step = text_value(item.get(step_key), "ta", "")
                        if has_value(step):
                            st.write(f"**{label}:**", step)
                    solution = text_value(item.get("solution"), "ta", "")
                    if has_value(solution):
                        st.write("**தீர்வு:**", solution)
                    st.write(
                        "**இறுதி விடை:**", text_value(item.get("answer"), "ta", "")
                    )
        st.markdown("---")

    # 8. ⭐ Important Facts
    render_bilingual_text_section(
        "⭐ Important Facts", content.get("important_facts"), st.success
    )

    # 9. 📚 Quick Revision
    render_bilingual_text_section(
        "📚 Quick Revision", content.get("quick_revision"), st.info
    )

    # 10. 🎯 TNPSC Focus Areas
    tnpsc_focus = content.get("tnpsc_focus", {})
    if isinstance(tnpsc_focus, dict):
        render_bilingual_text_section("🎯 TNPSC Focus Areas", tnpsc_focus, st.success)
    elif has_value(tnpsc_focus):
        st.header("🎯 TNPSC Focus Areas")
        render_points(tnpsc_focus, st.success)
        st.markdown("---")

    # 11. ❓ Practice MCQs
    mcqs = content.get("mcqs") or content.get("practice_mcqs", [])
    if has_value(mcqs):
        st.header("❓ Practice MCQs")
        for i, q in enumerate(as_list(mcqs), 1):
            if not isinstance(q, dict):
                st.markdown(f"**Q{i}. {q}**")
                continue

            question = (
                q.get("question_en")
                or q.get("question")
                or text_value(q.get("question"), "en", "")
            )
            st.markdown(f"**Q{i}. {question}**")
            for opt in q.get("options", []):
                st.write("▫️", opt)
            if has_value(q.get("answer")):
                st.success(f"✅ Answer: {q.get('answer')}")
            if has_value(q.get("explanation")):
                st.info(q.get("explanation"))
            st.markdown("---")

        if content.get("mcqs"):
            content["mcqs"] = []

    # 12. 🚀 Expected Questions
    expected_questions = content.get("expected_questions", [])
    if has_value(expected_questions):
        st.header("🚀 Expected Questions")
        for i, item in enumerate(as_list(expected_questions), 1):
            if isinstance(item, dict):
                tab1, tab2 = st.tabs(["EN", "TA"])
                with tab1:
                    st.markdown(
                        f"**Q{i}. {item.get('question_en') or text_value(item.get('question'), 'en', item.get('en', ''))}**"
                    )
                    render_points(
                        (
                            item.get("points", {}).get("en", [])
                            if isinstance(item.get("points"), dict)
                            else item.get("answer_en") or item.get("answer", "")
                        ),
                        st.write,
                    )
                with tab2:
                    st.markdown(
                        f"**Q{i}. {item.get('question_ta') or text_value(item.get('question'), 'ta', item.get('ta', ''))}**"
                    )
                    render_points(
                        (
                            item.get("points", {}).get("ta", [])
                            if isinstance(item.get("points"), dict)
                            else item.get("answer_ta", "")
                        ),
                        st.write,
                    )
            else:
                st.markdown(f"**Q{i}. {item}**")
            st.markdown("---")

    # 13. 🧠 Mind Map
    mind_map = content.get("mind_map", [])
    if has_value(mind_map):
        st.header("🧠 Mind Map")
        for item in as_list(mind_map):
            if isinstance(item, dict):
                title = title_value(item)
                if title:
                    st.subheader(f"🔹 {title}")
                render_points(
                    item.get("points")
                    or item.get("items")
                    or item.get("children")
                    or item.get("en")
                    or item.get("ta"),
                    st.markdown,
                )
            else:
                st.markdown(f"- {item}")
        st.markdown("---")


def _nova_has_value(value):
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict)):
        return bool(value)
    return True


def _nova_as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    return [value]


def _nova_text(value, lang="en", fallback=""):
    if isinstance(value, dict):
        return (
            value.get(lang)
            or value.get(f"{lang}_text")
            or value.get(f"content_{lang}")
            or value.get(f"title_{lang}")
            or fallback
        )
    return value if value is not None else fallback


def _nova_title(item, fallback=""):
    if not isinstance(item, dict):
        return fallback
    return item.get("title") or item.get("title_en") or item.get("name") or fallback


def _nova_points(value, lang="en"):
    if isinstance(value, dict):
        if isinstance(value.get("points"), dict):
            return _nova_as_list(value["points"].get(lang, []))
        return _nova_as_list(
            value.get(lang)
            or value.get(f"content_{lang}")
            or value.get(f"text_{lang}")
            or value.get("content")
            or value.get("text")
            or value.get("point")
            or []
        )
    return _nova_as_list(value)


def _nova_render_points(points, mode="write"):
    for point in _nova_as_list(points):
        if not _nova_has_value(point):
            continue
        if isinstance(point, dict):
            point = (
                point.get("text")
                or point.get("content")
                or point.get("point")
                or point.get("en")
                or point.get("ta")
            )
        if not _nova_has_value(point):
            continue
        if mode == "success":
            st.success(point)
        elif mode == "warning":
            st.warning(point)
        elif mode == "error":
            st.error(point)
        elif mode == "info":
            st.info(point)
        else:
            st.markdown(f"- {point}")


def _nova_badge(label):
    if label:
        st.caption(label)


def _nova_difficulty_badge(value):
    difficulty = str(value or "Easy").strip().lower()
    if difficulty == "hard":
        return "🔴 Hard"
    if difficulty == "medium":
        return "🟡 Medium"
    return "🟢 Easy"


def _nova_inject_notes_css():
    st.markdown(
        """
        <style>
            .nova-hero {
                border: 1px solid rgba(49, 51, 63, 0.14);
                border-radius: 18px;
                padding: 1.2rem 1.1rem;
                margin: 0.3rem 0 1rem;
                background: linear-gradient(135deg, #fff7ed 0%, #eff6ff 52%, #ecfdf5 100%);
                box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
            }
            .nova-hero h1 {
                font-size: clamp(1.55rem, 4.8vw, 2.5rem);
                line-height: 1.15;
                margin: 0 0 0.85rem;
                color: #172033;
                letter-spacing: 0;
            }
            .nova-meta {
                display: flex;
                flex-wrap: wrap;
                gap: 0.55rem;
                align-items: center;
            }
            .nova-pill {
                display: inline-flex;
                align-items: center;
                min-height: 2rem;
                padding: 0.35rem 0.65rem;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.78);
                border: 1px solid rgba(49, 51, 63, 0.12);
                color: #243044;
                font-size: 0.88rem;
                font-weight: 650;
            }
            .nova-section-title {
                font-size: 1.3rem;
                line-height: 1.25;
                font-weight: 800;
                margin: 1.35rem 0 0.65rem;
                color: #172033;
            }
            .nova-muted {
                color: #64748b;
                font-size: 0.9rem;
                margin-top: -0.3rem;
                margin-bottom: 0.55rem;
            }
            .nova-answer {
                font-weight: 750;
                color: #166534;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _nova_section(title, caption=None):
    st.markdown(f'<div class="nova-section-title">{title}</div>', unsafe_allow_html=True)
    if caption:
        st.markdown(f'<div class="nova-muted">{caption}</div>', unsafe_allow_html=True)


def _nova_bilingual_card(title, value, mode="info"):
    if not _nova_has_value(value):
        return
    _nova_section(title)
    with st.container(border=True):
        tab_en, tab_ta = st.tabs(["EN", "TA"])
        with tab_en:
            _nova_render_points(_nova_text(value, "en"), mode)
        with tab_ta:
            _nova_render_points(_nova_text(value, "ta"), mode)


def _nova_topic_label(content):
    raw_topic = (
        content.get("topic_name")
        or content.get("topic")
        or content.get("topic_id")
        or "Aptitude Notes"
    )
    return str(raw_topic).replace("_", " ").strip().title()


def render_aptitude(content):
    _nova_inject_notes_css()

    definition = content.get("definition")
    exam_importance = content.get("exam_importance")
    formula_sheet = content.get("formula_sheet", [])
    core_concepts = content.get("core_concepts", [])
    shortcut_tricks = content.get("shortcut_tricks") or content.get("exam_tricks", [])
    exam_traps = content.get("exam_traps", [])
    solved_examples = content.get("solved_examples", [])
    important_facts = content.get("important_facts", {})
    quick_revision = content.get("quick_revision", {})
    tnpsc_focus = content.get("tnpsc_focus", {})
    mcqs = content.get("mcqs") or content.get("practice_mcqs", [])
    expected_questions = content.get("expected_questions", [])
    mind_map = content.get("mind_map", [])

    sections = [
        definition,
        exam_importance,
        formula_sheet,
        core_concepts,
        shortcut_tricks,
        exam_traps,
        solved_examples,
        important_facts,
        quick_revision,
        tnpsc_focus,
        mcqs,
        expected_questions,
        mind_map,
    ]
    completed = sum(1 for section in sections if _nova_has_value(section))
    progress = completed / len(sections)
    total_mcqs = len(_nova_as_list(mcqs))
    study_minutes = max(10, min(45, 8 + completed * 2 + total_mcqs))
    difficulty = content.get("difficulty") or content.get("level") or "Easy"
    subject = str(content.get("subject", "Aptitude")).title()

    st.markdown(
        f"""
        <div class="nova-hero">
            <h1>📘 {_nova_topic_label(content)}</h1>
            <div class="nova-meta">
                <span class="nova-pill">🏷 {subject}</span>
                <span class="nova-pill">🔥 TNPSC Group 1</span>
                <span class="nova-pill">⏱ {study_minutes} Minutes</span>
                <span class="nova-pill">❓ {total_mcqs} Questions</span>
                <span class="nova-pill">⭐ {str(difficulty).title()}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown("**Progress Tracker**")
        st.progress(progress)
        st.caption(f"{int(progress * 100)}% completed")

    _nova_bilingual_card("📘 Definition", definition, "info")
    _nova_bilingual_card("🎯 Exam Importance", exam_importance, "info")

    if _nova_has_value(formula_sheet):
        _nova_section("📌 Formula Sheet")
        for item in _nova_as_list(formula_sheet):
            with st.container(border=True):
                if isinstance(item, dict):
                    title = _nova_title(item, "Formula")
                    formula = item.get("formula", "")
                    st.subheader(f"📌 {title}")
                    if _nova_has_value(formula):
                        st.code(str(formula), language="text")
                    tab_en, tab_ta = st.tabs(["EN", "TA"])
                    with tab_en:
                        explanation = (
                            item.get("explanation", {}).get("en", [])
                            if isinstance(item.get("explanation"), dict)
                            else item.get("explanation")
                            or item.get("content_en")
                            or item.get("en")
                        )
                        _nova_render_points(explanation)
                    with tab_ta:
                        explanation = (
                            item.get("explanation", {}).get("ta", [])
                            if isinstance(item.get("explanation"), dict)
                            else item.get("content_ta") or item.get("ta")
                        )
                        _nova_render_points(explanation)
                else:
                    st.info(item)

    if _nova_has_value(core_concepts):
        _nova_section("🧠 Core Concepts")
        for index, item in enumerate(_nova_as_list(core_concepts), 1):
            title = _nova_title(item, f"Core Concept {index}")
            with st.expander(f"🧠 {title}", expanded=index == 1):
                if isinstance(item, dict):
                    tab_en, tab_ta = st.tabs(["EN", "TA"])
                    with tab_en:
                        _nova_render_points(_nova_points(item, "en"))
                    with tab_ta:
                        _nova_render_points(_nova_points(item, "ta"))
                else:
                    st.write(item)

    if _nova_has_value(shortcut_tricks):
        _nova_section("⚡ Shortcut Tricks")
        for item in _nova_as_list(shortcut_tricks):
            with st.container(border=True):
                if isinstance(item, dict):
                    title = _nova_title(item)
                    if title:
                        st.subheader(f"⚡ {title}")
                    tab_en, tab_ta = st.tabs(["EN", "TA"])
                    with tab_en:
                        _nova_render_points(_nova_points(item, "en"), "success")
                    with tab_ta:
                        _nova_render_points(_nova_points(item, "ta"), "success")
                else:
                    st.success(item)

    if _nova_has_value(exam_traps):
        _nova_section("🔥 Exam Traps")
        for item in _nova_as_list(exam_traps):
            with st.container(border=True):
                if isinstance(item, dict):
                    title = _nova_title(item)
                    if title:
                        st.subheader(f"🔥 {title}")
                    tab_en, tab_ta = st.tabs(["EN", "TA"])
                    with tab_en:
                        _nova_render_points(_nova_points(item, "en"), "error")
                    with tab_ta:
                        _nova_render_points(_nova_points(item, "ta"), "error")
                else:
                    st.error(item)

    if _nova_has_value(solved_examples):
        _nova_section("📝 Solved Examples")
        for index, item in enumerate(_nova_as_list(solved_examples), 1):
            title = _nova_title(item, f"Solved Example {index}")
            if isinstance(item, dict) and item.get("pyq"):
                title = f"{title}   🏆 PYQ {item.get('year', '')}".strip()
            with st.expander(f"📝 {title}", expanded=index == 1):
                if isinstance(item, dict):
                    question = _nova_text(item.get("question"), "en", item.get("question", ""))
                    st.markdown(f"**❓ Question**  \n{question}")
                    for step_key in ["step1", "step2", "step3"]:
                        step = _nova_text(item.get(step_key), "en", "")
                        if _nova_has_value(step):
                            st.markdown(f"**➡ {step_key.replace('step', 'Step ')}**  \n{step}")
                    solution = _nova_text(item.get("solution"), "en", "")
                    if _nova_has_value(solution):
                        st.markdown(f"**➡ Solution**  \n{solution}")
                    answer = _nova_text(item.get("answer"), "en", item.get("answer", ""))
                    if _nova_has_value(answer):
                        st.success(f"✅ Final Answer: {answer}")
                else:
                    st.write(item)

    _nova_bilingual_card("⭐ Important Facts", important_facts, "success")

    if _nova_has_value(quick_revision):
        _nova_section("📚 Quick Revision Box")
        with st.container(border=True):
            tab_en, tab_ta = st.tabs(["EN", "TA"])
            with tab_en:
                _nova_render_points(_nova_text(quick_revision, "en"), "info")
            with tab_ta:
                _nova_render_points(_nova_text(quick_revision, "ta"), "info")

    if _nova_has_value(tnpsc_focus):
        _nova_section("🎯 TNPSC Focus Areas")
        points = (
            _nova_points(tnpsc_focus, "en")
            if isinstance(tnpsc_focus, dict)
            else _nova_as_list(tnpsc_focus)
        )
        for point in points:
            if _nova_has_value(point):
                st.success(point)

    if _nova_has_value(mcqs):
        _nova_section("❓ Practice MCQs")
        for index, q in enumerate(_nova_as_list(mcqs), 1):
            with st.container(border=True):
                if not isinstance(q, dict):
                    st.markdown(f"**❓ Q{index}. {q}**")
                    continue
                if q.get("pyq"):
                    _nova_badge(f"🏆 PYQ {q.get('year', '')}".strip())
                _nova_badge(_nova_difficulty_badge(q.get("difficulty")))
                question = (
                    q.get("question_en")
                    or q.get("question")
                    or _nova_text(q.get("question"), "en", "")
                )
                st.markdown(f"**❓ Q{index}. {question}**")
                for option_index, option in enumerate(q.get("options", []), 1):
                    st.checkbox(
                        str(option),
                        value=False,
                        key=f"apt_mcq_{index}_{option_index}_{hash(str(option))}",
                        disabled=True,
                    )
                if _nova_has_value(q.get("answer")):
                    st.markdown(
                        f'<div class="nova-answer">✅ Answer: {q.get("answer")}</div>',
                        unsafe_allow_html=True,
                    )
                if _nova_has_value(q.get("explanation")):
                    st.info(f"💡 {q.get('explanation')}")
        if content.get("mcqs"):
            content["mcqs"] = []

    if _nova_has_value(expected_questions):
        _nova_section("🚀 Expected Group 1 Questions")
        for index, item in enumerate(_nova_as_list(expected_questions), 1):
            with st.container(border=True):
                if isinstance(item, dict):
                    if item.get("pyq"):
                        _nova_badge(f"🏆 PYQ {item.get('year', '')}".strip())
                    tab_en, tab_ta = st.tabs(["EN", "TA"])
                    with tab_en:
                        question = item.get("question_en") or _nova_text(item.get("question"), "en", item.get("en", ""))
                        st.warning(f"🚀 Q{index}. {question}")
                        _nova_render_points(item.get("answer_en") or item.get("answer", ""))
                    with tab_ta:
                        question = item.get("question_ta") or _nova_text(item.get("question"), "ta", item.get("ta", ""))
                        st.warning(f"🚀 Q{index}. {question}")
                        _nova_render_points(item.get("answer_ta", ""))
                else:
                    st.warning(f"🚀 Q{index}. {item}")

    if _nova_has_value(mind_map):
        _nova_section("🧠 Mind Map")
        with st.container(border=True):
            for item in _nova_as_list(mind_map):
                if isinstance(item, dict):
                    title = _nova_title(item)
                    if title:
                        st.markdown(f"**🧠 {title}**")
                    _nova_render_points(
                        item.get("points")
                        or item.get("items")
                        or item.get("children")
                        or item.get("en")
                        or item.get("ta")
                    )
                else:
                    st.markdown(f"- {item}")

    st.markdown("---")
    if st.button("✅ Mark Topic Completed", use_container_width=True):
        st.success("Topic marked as completed.")


def render_reasoning(content):
    st.title("🧠 Reasoning Notes")

    # ====================================
    # Definition
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
    # Concept Rules
    # ====================================
    if "concept_rules" in content:
        st.header("📌 Concept Rules")
        for item in content["concept_rules"]:
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

    # ====================================
    # Shortcut Methods
    # ====================================
    if "shortcut_methods" in content:
        st.header("🧠 Shortcut Methods")
        for item in content["shortcut_methods"]:
            title = item.get("title", "")
            if title:
                st.subheader(f"🔸 {title}")
            tab1, tab2 = st.tabs(["EN", "TA"])
            with tab1:
                for point in item.get("points", {}).get("en", []):
                    st.success(point)
            with tab2:
                for point in item.get("points", {}).get("ta", []):
                    st.success(point)
            st.markdown("---")

    # ====================================
    # Common Mistakes
    # ====================================
    if "common_mistakes" in content:
        st.header("🔥 Common Mistakes")
        for item in content["common_mistakes"]:
            title = item.get("title", "")
            if title:
                st.subheader(f"❌ {title}")
            tab1, tab2 = st.tabs(["EN", "TA"])
            with tab1:
                for point in item.get("points", {}).get("en", []):
                    st.error(point)
            with tab2:
                for point in item.get("points", {}).get("ta", []):
                    st.error(point)
            st.markdown("---")

    # ====================================
    # Solved Examples
    # ====================================
    if "solved_examples" in content:
        st.header("📝 Solved Examples")
        for item in content["solved_examples"]:
            with st.expander(f"📖 {item.get('title', 'Solved Example')}"):
                tab1, tab2 = st.tabs(["EN", "TA"])
                with tab1:
                    st.write("**Question:**", item.get("question", {}).get("en", ""))
                    st.write("**Solution:**", item.get("solution", {}).get("en", ""))
                    st.write("**Final Answer:**", item.get("answer", {}).get("en", ""))
                with tab2:
                    st.write("**வினா:**", item.get("question", {}).get("ta", ""))
                    st.write("**தீர்வு:**", item.get("solution", {}).get("ta", ""))
                    st.write("**இறுதி விடை:**", item.get("answer", {}).get("ta", ""))
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
