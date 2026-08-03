import streamlit as st
from core.question_engine.session import set_session_value
from core.question_engine.practice_session import set_practice_question_index


def render_question_palette(
    prefix: str,
    total_questions: int,
    current_index: int,
    answered_map: dict = None,
    bookmarked_set: set = None,
):
    st.markdown("### 🗂️ Question Palette")

    # Step 1: Verify & Consolidate Session State
    if answered_map is None:
        if prefix == "practice":
            answered_map = st.session_state.get("practice_answers", {})
        else:
            answered_map = st.session_state.get(f"{prefix}_answers", {})

    if bookmarked_set is None:
        bookmarked_set = (
            st.session_state.get(f"{prefix}_bookmarks", set())
            | st.session_state.get("practice_bookmarks", set())
            | st.session_state.get(f"{prefix}_review", set())
        )

    # Track visited questions set in session state
    visited_key = f"{prefix}_visited"
    visited_set = st.session_state.get(visited_key)
    if visited_set is None:
        visited_set = set()
        st.session_state[visited_key] = visited_set
    visited_set.add(current_index)
    if prefix == "practice":
        st.session_state["practice_visited"] = visited_set

    # Question list for ID bookmark checks if present
    questions_list = []
    if prefix == "practice":
        questions_list = st.session_state.get("practice_questions", [])
    elif f"{prefix}_qs" in st.session_state:
        questions_list = st.session_state.get(f"{prefix}_qs", [])

    # Consolidate state sets
    submitted_questions = set()
    if prefix == "practice":
        prac_ans = st.session_state.get("practice_answers", {})
        if isinstance(prac_ans, dict):
            submitted_questions.update(prac_ans.keys())
    else:
        prefix_sub = st.session_state.get(f"{prefix}_submitted", set())
        if isinstance(prefix_sub, (set, list)):
            submitted_questions.update(prefix_sub)
        prefix_ans = st.session_state.get(f"{prefix}_answers", {})
        if isinstance(prefix_ans, dict):
            submitted_questions.update(prefix_ans.keys())
        prefix_att = st.session_state.get(f"{prefix}_attempts", [])
        if isinstance(prefix_att, list):
            for att in prefix_att:
                if isinstance(att, dict) and "q_idx" in att:
                    submitted_questions.add(att["q_idx"])

    answered_questions = set(submitted_questions)
    if answered_map and isinstance(answered_map, dict):
        answered_questions.update(answered_map.keys())
    if prefix == "practice" and st.session_state.get("practice_selected_answer"):
        answered_questions.add(current_index)
    elif st.session_state.get(f"{prefix}_selected_answer"):
        answered_questions.add(current_index)

    visited_questions = set(visited_set)
    visited_questions.add(current_index)

    marked_questions = set(bookmarked_set)
    current_question = current_index

    # Render Legend
    st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 14px; font-size: 0.82rem; align-items: center;">
            <span style="background: #E5E7EB; color: #1F2937; padding: 4px 10px; border-radius: 6px; font-weight: 700; border: 1px solid #D1D5DB;">⚪ Not Visited</span>
            <span style="background: #3B82F6; color: #FFFFFF; padding: 4px 10px; border-radius: 6px; font-weight: 700; border: 1px solid #2563EB;">🔵 Visited</span>
            <span style="background: #10B981; color: #FFFFFF; padding: 4px 10px; border-radius: 6px; font-weight: 700; border: 1px solid #059669;">🟢 Answered</span>
            <span style="background: #8B5CF6; color: #FFFFFF; padding: 4px 10px; border-radius: 6px; font-weight: 700; border: 1px solid #7C3AED;">🟣 Submitted</span>
            <span style="background: #F97316; color: #FFFFFF; padding: 4px 10px; border-radius: 6px; font-weight: 700; border: 1px solid #EA580C;">🟠 Marked for Review</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Render CSS Overrides (Dedicated <style> block)
    st.markdown(
        """<style>
        /* Base sizing & reset for palette buttons */
        div[data-testid="stColumn"]:has(.palette-not-visited) button,
        div[data-testid="stColumn"]:has(.palette-visited) button,
        div[data-testid="stColumn"]:has(.palette-answered) button,
        div[data-testid="stColumn"]:has(.palette-submitted) button,
        div[data-testid="stColumn"]:has(.palette-marked) button,
        div[data-testid="column"]:has(.palette-not-visited) button,
        div[data-testid="column"]:has(.palette-visited) button,
        div[data-testid="column"]:has(.palette-answered) button,
        div[data-testid="column"]:has(.palette-submitted) button,
        div[data-testid="column"]:has(.palette-marked) button,
        div:has(> .palette-not-visited) button,
        div:has(> .palette-visited) button,
        div:has(> .palette-answered) button,
        div:has(> .palette-submitted) button,
        div:has(> .palette-marked) button,
        .pal-btn-wrap button {
            min-height: 2.3rem !important;
            height: 2.3rem !important;
            font-weight: 700 !important;
            border-radius: 8px !important;
            padding: 0 !important;
            transition: all 0.15s ease-in-out !important;
            box-shadow: none !important;
        }

        /* 1. Not Visited -> Gray */
        div[data-testid="stColumn"]:has(.palette-not-visited) button,
        div[data-testid="column"]:has(.palette-not-visited) button,
        div[data-testid="stElementContainer"]:has(.palette-not-visited) + div[data-testid="stElementContainer"] button,
        div:has(.palette-not-visited) button,
        .palette-not-visited button,
        .pal-btn-gray button {
            background: #E5E7EB !important;
            background-image: none !important;
            color: #1F2937 !important;
            border: 1px solid #D1D5DB !important;
        }
        div[data-testid="stColumn"]:has(.palette-not-visited) button:hover,
        div:has(.palette-not-visited) button:hover {
            background: #D1D5DB !important;
            background-image: none !important;
            color: #1F2937 !important;
        }

        /* 2. Visited -> Blue */
        div[data-testid="stColumn"]:has(.palette-visited) button,
        div[data-testid="column"]:has(.palette-visited) button,
        div[data-testid="stElementContainer"]:has(.palette-visited) + div[data-testid="stElementContainer"] button,
        div:has(.palette-visited) button,
        .palette-visited button,
        .pal-btn-blue button {
            background: #3B82F6 !important;
            background-image: none !important;
            color: #FFFFFF !important;
            border: 1px solid #2563EB !important;
        }
        div[data-testid="stColumn"]:has(.palette-visited) button:hover,
        div:has(.palette-visited) button:hover {
            background: #2563EB !important;
            background-image: none !important;
            color: #FFFFFF !important;
        }

        /* 3. Answered -> Green */
        div[data-testid="stColumn"]:has(.palette-answered) button,
        div[data-testid="column"]:has(.palette-answered) button,
        div[data-testid="stElementContainer"]:has(.palette-answered) + div[data-testid="stElementContainer"] button,
        div:has(.palette-answered) button,
        .palette-answered button,
        .pal-btn-green button {
            background: #10B981 !important;
            background-image: none !important;
            color: #FFFFFF !important;
            border: 1px solid #059669 !important;
        }
        div[data-testid="stColumn"]:has(.palette-answered) button:hover,
        div:has(.palette-answered) button:hover {
            background: #059669 !important;
            background-image: none !important;
            color: #FFFFFF !important;
        }

        /* 4. Submitted -> Purple (Highest Priority) */
        div[data-testid="stColumn"]:has(.palette-submitted) button,
        div[data-testid="column"]:has(.palette-submitted) button,
        div[data-testid="stElementContainer"]:has(.palette-submitted) + div[data-testid="stElementContainer"] button,
        div:has(.palette-submitted) button,
        .palette-submitted button,
        .pal-btn-purple button {
            background: #8B5CF6 !important;
            background-image: none !important;
            color: #FFFFFF !important;
            border: 1px solid #7C3AED !important;
        }
        div[data-testid="stColumn"]:has(.palette-submitted) button:hover,
        div:has(.palette-submitted) button:hover {
            background: #7C3AED !important;
            background-image: none !important;
            color: #FFFFFF !important;
        }

        /* 5. Marked for Review -> Orange */
        div[data-testid="stColumn"]:has(.palette-marked) button,
        div[data-testid="column"]:has(.palette-marked) button,
        div[data-testid="stElementContainer"]:has(.palette-marked) + div[data-testid="stElementContainer"] button,
        div:has(.palette-marked) button,
        .palette-marked button,
        .pal-btn-orange button {
            background: #F97316 !important;
            background-image: none !important;
            color: #FFFFFF !important;
            border: 1px solid #EA580C !important;
        }
        div[data-testid="stColumn"]:has(.palette-marked) button:hover,
        div:has(.palette-marked) button:hover {
            background: #EA580C !important;
            background-image: none !important;
            color: #FFFFFF !important;
        }

        /* Current Question Highlight -> Dark Blue Border */
        div[data-testid="stColumn"]:has(.palette-current) button,
        div[data-testid="column"]:has(.palette-current) button,
        div[data-testid="stElementContainer"]:has(.palette-current) + div[data-testid="stElementContainer"] button,
        div:has(.palette-current) button,
        .palette-current button,
        .pal-btn-curr button {
            border: 3px solid #0F172A !important;
            box-shadow: 0 0 0 2px #FACC15, 0 4px 12px rgba(0, 0, 0, 0.25) !important;
            font-weight: 900 !important;
            transform: scale(1.04);
        }
        </style>""",
        unsafe_allow_html=True,
    )

    cols_per_row = 10
    total_rows = (total_questions + cols_per_row - 1) // cols_per_row

    for r in range(total_rows):
        cols = st.columns(cols_per_row, gap="small")
        for c in range(cols_per_row):
            q_idx = r * cols_per_row + c
            if q_idx >= total_questions:
                break

            q_num = q_idx + 1

            # Get question ID if available for bookmark check
            q_id = None
            if 0 <= q_idx < len(questions_list):
                q_obj = questions_list[q_idx]
                q_id = q_obj.get("id") if isinstance(q_obj, dict) else getattr(q_obj, "id", None)

            is_marked = (q_idx in marked_questions) or (q_id and q_id in marked_questions)

            # Step 2: Exact State Priority Hierarchy
            if q_idx in submitted_questions:
                palette_class = "palette-submitted pal-btn-purple"
            elif is_marked:
                palette_class = "palette-marked pal-btn-orange"
            elif q_idx in answered_questions:
                palette_class = "palette-answered pal-btn-green"
            elif q_idx in visited_questions:
                palette_class = "palette-visited pal-btn-blue"
            else:
                palette_class = "palette-not-visited pal-btn-gray"

            # Step 3: Current Question Highlight
            if q_idx == current_question:
                palette_class += " palette-current pal-btn-curr"

            label = f"[{q_num}]" if q_idx == current_question else f"{q_num}"

            with cols[c]:
                st.markdown(f'<div class="{palette_class}"></div>', unsafe_allow_html=True)
                if st.button(label, key=f"{prefix}_pal_{q_idx}", use_container_width=True):
                    # Record visited state
                    visited_set.add(q_idx)
                    st.session_state[visited_key] = visited_set
                    if prefix == "practice":
                        st.session_state["practice_visited"] = visited_set
                        set_practice_question_index(q_idx)
                    else:
                        set_session_value(st.session_state, prefix, "index", q_idx)
                        st.session_state["q_index"] = q_idx
                        # Restore answered state if available
                        if answered_map and q_idx in answered_map:
                            set_session_value(st.session_state, prefix, "answered", True)
                            ans_val = answered_map[q_idx]
                            sel = ans_val.get("selected_option") or ans_val.get("selected_answer") if isinstance(ans_val, dict) else ans_val
                            set_session_value(st.session_state, prefix, "selected_answer", sel)
                        else:
                            set_session_value(st.session_state, prefix, "answered", False)
                            set_session_value(st.session_state, prefix, "selected_answer", None)
                    st.rerun()

