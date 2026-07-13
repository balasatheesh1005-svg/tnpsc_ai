"""Official answer key helpers for PYQ verification.

Answer keys are intentionally stored outside question JSON files under:
data/official/answer_keys/<exam>/<year>.json
"""

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional


DEFAULT_ANSWER_KEY_ROOT = Path("data/official/answer_keys")


def load_answer_key(exam, year):
    """Load an official answer key map, or return None safely.

    Each map value is a list of one or more accepted A/B/C/D options.
    """
    try:
        key_path = _answer_key_path(exam, year)
        if not key_path or not key_path.exists() or not key_path.is_file():
            return None

        answers = _read_answer_key_file(str(key_path))
        return answers if answers else None
    except Exception:
        return None


def get_correct_answer(question_id):
    """Return official accepted option(s) for a question id, or None.

    A one-item list represents a normal question; multiple items represent an
    official multi-answer key.  The list form keeps both cases unambiguous.
    """
    try:
        target = _normalize_question_id(question_id)
        if not target:
            return None

        for key_path in _iter_answer_key_files(DEFAULT_ANSWER_KEY_ROOT):
            answers = _read_answer_key_file(str(key_path))
            answer = answers.get(target)
            if answer:
                return answer
    except Exception:
        return None
    return None


def verify_answer(question_id, selected_option):
    """Return True/False when a key exists, or None when unavailable."""
    try:
        correct_answer = get_correct_answer(question_id)
        selected = _normalize_option(selected_option)
        if not correct_answer or not selected:
            return None
        return selected in correct_answer
    except Exception:
        return None


def answer_key_exists(exam, year):
    """Return whether an official answer key file exists for exam/year."""
    try:
        key_path = _answer_key_path(exam, year)
        return bool(key_path and key_path.exists() and key_path.is_file())
    except Exception:
        return False


def _answer_key_path(exam, year) -> Optional[Path]:
    exam_key = _normalize_exam(exam)
    year_key = _normalize_year(year)
    if not exam_key or not year_key:
        return None
    directory = DEFAULT_ANSWER_KEY_ROOT / exam_key
    legacy_path = directory / f"{year_key}.json"
    named_path = directory / f"{exam_key}_{year_key}_answer_key.json"
    return legacy_path if legacy_path.exists() else named_path


def _normalize_exam(exam) -> str:
    try:
        value = str(exam or "").strip().lower()
        if not value:
            return ""
        compact = "".join(char for char in value if char.isalnum())
        aliases = {
            "group1": "group1",
            "g1": "group1",
            "groupi": "group1",
            "groupone": "group1",
        }
        return aliases.get(compact, compact)
    except Exception:
        return ""


def _normalize_year(year) -> str:
    try:
        value = str(year or "").strip()
        return value if value.isdigit() else ""
    except Exception:
        return ""


def _normalize_question_id(question_id) -> str:
    try:
        return str(question_id or "").strip()
    except Exception:
        return ""


def _normalize_option(option) -> str:
    try:
        value = str(option or "").strip().upper()
        return value[:1] if value[:1] in {"A", "B", "C", "D"} else ""
    except Exception:
        return ""


def _iter_answer_key_files(root: Path):
    try:
        root_path = Path(root)
        if not root_path.exists() or not root_path.is_dir():
            return []
        return sorted(path for path in root_path.glob("*/*.json") if path.is_file())
    except Exception:
        return []


@lru_cache(maxsize=64)
def _read_answer_key_file(path: str) -> Dict[str, List[str]]:
    try:
        with Path(path).open("r", encoding="utf-8") as file:
            data = json.load(file)
        return _extract_answers(data)
    except Exception:
        return {}


def _extract_answers(data: Any) -> Dict[str, List[str]]:
    if isinstance(data, dict):
        rows = data.get("answers")
        if isinstance(rows, dict):
            return _normalize_answer_map(rows)
        if isinstance(rows, list):
            return _normalize_answer_rows(rows)
        return _normalize_answer_map(data)

    if isinstance(data, list):
        return _normalize_answer_rows(data)

    return {}


def _normalize_answer_map(rows: Dict[str, Any]) -> Dict[str, List[str]]:
    answers = {}
    for question_id, option in rows.items():
        normalized_id = _normalize_question_id(question_id)
        normalized_options = _normalize_options(option)
        if normalized_id and normalized_options:
            answers[normalized_id] = normalized_options
    return answers


def _normalize_answer_rows(rows) -> Dict[str, List[str]]:
    answers = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        question_id = _normalize_question_id(row.get("id") or row.get("question_id"))
        options = _normalize_options(
            row.get("correct_answers")
            or row.get("correct_answer")
            or row.get("answer")
        )
        if question_id and options:
            answers[question_id] = options
    return answers


def _normalize_options(value: Any) -> List[str]:
    if isinstance(value, dict):
        value = value.get("correct_answers") or value.get("correct_answer") or value.get("answer")
    values = value if isinstance(value, (list, tuple, set)) else [value]
    options = []
    for item in values:
        option = _normalize_option(item)
        if option and option not in options:
            options.append(option)
    return options


def refresh_answer_key_cache():
    """Clear cached official answer key files after updates."""
    _read_answer_key_file.cache_clear()
