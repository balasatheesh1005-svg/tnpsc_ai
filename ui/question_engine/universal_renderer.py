import streamlit as st
from ui.question_engine.parser import UniversalQuestionAdapter, NormalizedQuestion
from ui.question_engine.header_component import render_question_header
from ui.question_engine.body_component import render_question_body
from ui.question_engine.option_component import render_option_cards
from ui.question_engine.footer_component import render_question_footer
from ui.question_engine.explanation_component import render_explanation_card
from ui.question_engine.palette_component import render_question_palette
from ui.question_engine.result_component import render_universal_result_screen
from core.question_engine.session import get_session_value, record_answer, set_session_value, reset_answer


def render_universal_question_card(
    question_data: dict,
    question_number: int,
    total_questions: int,
    prefix: str = "daily",
    timer_seconds: int = None,
    show_palette: bool = True,
    explanation_actions: list = None,
):
    if not question_data:
        st.info("No question selected.")
        return

    # 1. Normalize question data via Universal Adapter
    q: NormalizedQuestion = UniversalQuestionAdapter.normalize(question_data)

    # 2. Render Header (Progress, Timer, Badges, Language Toggle, Bookmarks)
    render_question_header(
        q=q,
        current_index=question_number - 1,
        total_questions=total_questions,
        prefix=prefix,
        timer_seconds=timer_seconds,
    )

    # 3. Optional Question Palette expander
    if show_palette and total_questions > 1:
        with st.expander("🗂️ Question Palette & Jump Navigation", expanded=False):
            render_question_palette(
                prefix=prefix,
                total_questions=total_questions,
                current_index=question_number - 1,
                bookmarked_set=st.session_state.get(f"{prefix}_bookmarks", set()),
            )

    # 4. Render Body (Dynamic Question Type Layout: MCQ, Statements, AR, Match, Chronology)
    lang_mode = st.session_state.get(f"{prefix}_lang_mode", "BOTH")
    render_question_body(q=q, lang_mode=lang_mode)

    # 5. Render Options
    is_answered = get_session_value(st.session_state, prefix, "answered", False)
    selected_option = get_session_value(st.session_state, prefix, "selected_answer", "")

    chosen_key, option_labels = render_option_cards(
        q=q,
        prefix=prefix,
        disabled=is_answered,
        selected_option_key=selected_option,
    )

    # 6. Render Footer (Navigation Controls + Confidence Meter)
    submitted = render_question_footer(
        prefix=prefix,
        current_index=question_number - 1,
        total_questions=total_questions,
    )

    # Handle Answer Submission
    if submitted:
        is_correct = (chosen_key == q.correct_answer)
        set_session_value(st.session_state, prefix, "selected_answer", chosen_key)
        set_session_value(st.session_state, prefix, "answered", True)
        
        # Record answer in score
        if is_correct:
            current_score = get_session_value(st.session_state, prefix, "score", 0)
            set_session_value(st.session_state, prefix, "score", current_score + 1)

        record_answer(
            st.session_state,
            prefix,
            chosen_key,
            is_correct,
            q.id,
        )
        st.rerun()

    # 7. Render Explanation (when answered)
    if get_session_value(st.session_state, prefix, "answered", False):
        user_choice = get_session_value(st.session_state, prefix, "selected_answer", "")
        render_explanation_card(
            q=q,
            prefix=prefix,
            user_choice=user_choice,
            actions=explanation_actions,
        )
