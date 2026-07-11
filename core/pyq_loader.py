from pathlib import Path

from core.question_engine.filters import matches_field, normalize_text, search_questions
from core.question_engine.loader import (
    iter_json_files,
    load_questions_from_path,
    refresh_question_cache,
    safe_read_json,
)
from core.question_engine.stats import get_facets


PYQ_ROOT = Path("data/pyq")

EXAM_FOLDER_MAP = {
    "group 1": "group1",
    "group1": "group1",
    "g1": "group1",
    "group 2": "group2",
    "group2": "group2",
    "g2": "group2",
    "group 2a": "group2a",
    "group2a": "group2a",
    "g2a": "group2a",
    "group 4": "group4",
    "group4": "group4",
    "g4": "group4",
    "vao": "vao",
}


def _normalize_exam_key(exam):
    normalized = normalize_text(exam).replace("-", " ")
    compact = normalized.replace(" ", "")
    return EXAM_FOLDER_MAP.get(normalized) or EXAM_FOLDER_MAP.get(compact) or compact


def refresh_pyq_cache():
    """Clear cached PYQ data after adding or updating JSON files."""
    refresh_question_cache()


def load_all_pyq():
    """Load all PYQ questions safely from data/pyq."""
    return load_questions_from_path(PYQ_ROOT)


def load_exam_pyq(exam):
    """Load PYQ questions for one exam folder or matching exam label."""
    exam_key = _normalize_exam_key(exam)
    exam_root = PYQ_ROOT / exam_key

    if exam_root.exists() and exam_root.is_dir():
        questions = []
        for file_path in iter_json_files(exam_root):
            questions.extend(safe_read_json(file_path))
        return questions

    return [
        question
        for question in load_all_pyq()
        if _normalize_exam_key(question.get("exam")) == exam_key
    ]


def load_year_pyq(exam, year):
    """Load PYQ questions for a specific exam and year."""
    try:
        year_value = int(year)
    except (TypeError, ValueError):
        return []

    rows = []
    for question in load_exam_pyq(exam):
        try:
            question_year = int(question.get("year") or 0)
        except (TypeError, ValueError):
            question_year = 0
        if question_year == year_value:
            rows.append(question)
    return rows


def load_subject_pyq(subject):
    """Load PYQ questions across exams for a specific subject."""
    return [
        question
        for question in load_all_pyq()
        if matches_field(question, ("subject",), subject)
    ]


def search_pyq(keyword):
    """Search PYQ text, options, explanations, tags, and metadata."""
    return search_questions(load_all_pyq(), keyword)


def get_pyq_facets(questions=None):
    """Return sorted filter values for dashboard controls."""
    facets = get_facets(questions if questions is not None else load_all_pyq(), ("exam", "year", "subject"))
    return {
        "exams": [str(value).strip() for value in facets["exam"]],
        "years": [
            int(value)
            for value in facets["year"]
            if str(value).isdigit()
        ],
        "subjects": [str(value).strip() for value in facets["subject"]],
    }
