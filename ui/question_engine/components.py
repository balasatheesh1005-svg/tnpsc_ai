import html
import time

import streamlit as st

from core.question_engine.navigator import next_index, previous_index
from core.question_engine.progress import build_progress_state, is_correct_answer
from core.question_engine.answer_key import get_correct_answer
from core.question_engine.session import (
    get_session_value,
    record_answer,
    reset_answer,
    set_session_value,
)
from ui.components.cards import glass_card_html, html_fragment


OPTION_KEYS = ("A", "B", "C", "D")


def _format_time(seconds):
    seconds = max(0, int(seconds or 0))
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def _extract_options(question):
    options = question.get("options")
    if isinstance(options, dict):
        return [(key, str(options.get(key, ""))) for key in OPTION_KEYS if key in options]

    options_en = question.get("options_en")
    options_ta = question.get("options_ta")
    if isinstance(options_en, list):
        rows = []
        for index, value in enumerate(options_en):
            key = OPTION_KEYS[index] if index < len(OPTION_KEYS) else str(index + 1)
            tamil = ""
            if isinstance(options_ta, list) and index < len(options_ta):
                tamil = f" / {options_ta[index]}"
            rows.append((key, f"{value}{tamil}"))
        return rows

    return []


def _correct_answer(question):
    if not question:
        return None
    official_answer = get_correct_answer(question.get("id")) if question else None
    return official_answer or question.get("correct_answer") or question.get("answer") or question.get("correct")


def _has_verified_answer(question):
    return bool(_correct_answer(question))


def _format_official_answers(correct_answers):
    if isinstance(correct_answers, (list, tuple, set)):
        answers = [str(answer) for answer in correct_answers if str(answer)]
    elif correct_answers:
        answers = [str(correct_answers)]
    else:
        answers = []
    return answers


def _question_text(question):
    return question.get("question_en") or question.get("question") or "Question text not available."


def render_timer(prefix, total_seconds=None):
    if not total_seconds:
        return

    start_key = f"{prefix}_started_at"
    if not st.session_state.get(start_key):
        st.session_state[start_key] = time.time()

    elapsed = int(time.time() - st.session_state[start_key])
    remaining = max(0, int(total_seconds) - elapsed)
    st.markdown(
        f'<span class="progress-pill">Remaining Time: {_format_time(remaining)}</span>',
        unsafe_allow_html=True,
    )


def render_explanation(question, prefix, actions=None):
    correct_answers = _format_official_answers(_correct_answer(question))
    correct_key = correct_answers[0] if len(correct_answers) == 1 else ""
    options = dict(_extract_options(question))
    correct_text = options.get(correct_key, "")
    explanation = question.get("explanation") or {}
    english = None
    tamil = None
    if isinstance(explanation, dict):
        english = explanation.get("english") or explanation.get("en")
        tamil = explanation.get("tamil") or explanation.get("ta")
    english = english or question.get("explanation_en") or "Explanation will be available soon."
    tamil = tamil or question.get("explanation_ta") or "Explanation will be available soon."

    if len(correct_answers) == 1:
        answer_html = (
            '<div class="answer-feedback correct">'
            f"<strong>Correct Answer: {html.escape(str(correct_key))}</strong>"
            f'<p class="nova-card-copy">{html.escape(str(correct_text or correct_key))}</p>'
            "</div>"
        )
    elif correct_answers:
        answer_html = (
            '<div class="answer-feedback correct">'
            "<strong>Official TNPSC Final Key accepts multiple answers:</strong>"
            f'<p class="nova-card-copy">{html.escape(", ".join(correct_answers))}</p>'
            "</div>"
        )
    else:
        answer_html = (
            '<div class="answer-feedback">'
            "<strong>Official answer key has not yet been verified.</strong>"
            "</div>"
        )
    st.html(glass_card_html("Answer Review", extra_html=html_fragment(answer_html)))

    st.markdown(
        f"""
        <section class="explanation-card">
            <h4>Tamil Explanation</h4>
            <p>{html.escape(str(tamil))}</p>
        </section>
        <section class="explanation-card">
            <h4>English Explanation</h4>
            <p>{html.escape(str(english))}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    if actions:
        columns = st.columns(len(actions), gap="small")
        for column, action in zip(columns, actions):
            with column:
                if st.button(
                    action["label"],
                    key=f"{prefix}_{action['key']}",
                    use_container_width=True,
                    disabled=action.get("disabled", False),
                ):
                    callback = action.get("callback")
                    if callback:
                        callback(question)

        # Clear old error if question ID has changed
        last_q_key = f"{prefix}_last_q_id"
        current_q_id = None
        if question:
            if hasattr(question, "get"):
                current_q_id = question.get("id")
            else:
                current_q_id = getattr(question, "id", None)
        
        if st.session_state.get(last_q_key) != current_q_id:
            st.session_state[last_q_key] = current_q_id
            st.session_state.pop(f"{prefix}_notes_error", None)

        # Render notes warning message gracefully
        error_key = f"{prefix}_notes_error"
        if st.session_state.get(error_key):
            st.warning(st.session_state[error_key])


def render_navigation(prefix, total_questions):
    previous_col, submit_col, next_col = st.columns(3, gap="small")
    with previous_col:
        if st.button("Previous", key=f"{prefix}_prev", use_container_width=True):
            set_session_value(
                st.session_state,
                prefix,
                "index",
                previous_index(get_session_value(st.session_state, prefix, "index", 0), total_questions),
            )
            reset_answer(st.session_state, prefix)
            st.rerun()

    with submit_col:
        submitted = st.button(
            "Submit",
            key=f"{prefix}_submit",
            use_container_width=True,
            disabled=get_session_value(st.session_state, prefix, "answered", False),
        )

    with next_col:
        if st.button("Next", key=f"{prefix}_next", use_container_width=True):
            set_session_value(
                st.session_state,
                prefix,
                "index",
                next_index(get_session_value(st.session_state, prefix, "index", 0), total_questions),
            )
            reset_answer(st.session_state, prefix)
            st.rerun()

    return submitted


def render_review(question, prefix, actions=None):
    chosen = get_session_value(st.session_state, prefix, "selected_answer", "")
    correct = _correct_answer(question)
    if not correct:
        st.warning("Official answer key has not yet been verified.")
    elif is_correct_answer(chosen, correct):
        st.success("Correct")
    else:
        answers = _format_official_answers(correct)
        if len(answers) == 1:
            st.error(f"Wrong. Correct option is {answers[0]}.")
        else:
            st.error(
                "Wrong. Official TNPSC Final Key accepts multiple answers: "
                f"{', '.join(answers)}."
            )
    render_explanation(question, prefix, actions=actions)


def render_question_card(
    question,
    question_number,
    total_questions,
    prefix,
    meta_fields=None,
    timer_seconds=None,
    explanation_actions=None,
):
    from ui.question_engine.universal_renderer import render_universal_question_card
    render_universal_question_card(
        question_data=question,
        question_number=question_number,
        total_questions=total_questions,
        prefix=prefix,
        timer_seconds=timer_seconds,
        explanation_actions=explanation_actions,
    )

