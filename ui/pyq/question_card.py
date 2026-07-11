from ui.pyq.explanation import get_pyq_explanation_actions
from ui.question_engine.components import render_question_card as render_engine_question_card


def render_question_card(question, question_number, total_questions):
    render_engine_question_card(
        question,
        question_number,
        total_questions,
        prefix="pyq",
        meta_fields=["exam", "year", "subject"],
        explanation_actions=get_pyq_explanation_actions(),
    )
