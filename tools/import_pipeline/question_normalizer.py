"""Stage 2: normalize raw extracted questions into the approved schema."""

import json
import re
from pathlib import Path
from typing import Any, Dict, List


OPTION_KEYS = ("A", "B", "C", "D")


def normalize_questions(
    input_path,
    output_path=None,
    exam="Group 1",
    year=2011,
    subject="General Knowledge",
) -> Dict[str, Any]:
    """Normalize raw_questions.json into normalized_questions.json safely."""
    summary = {
        "input_path": str(input_path or ""),
        "output_path": str(output_path or "normalized_questions.json"),
        "question_count": 0,
        "errors": [],
    }

    try:
        source = _read_json(Path(input_path))
        raw_questions = source.get("raw_questions") if isinstance(source, dict) else []
        if not isinstance(raw_questions, list):
            raw_questions = []

        normalized = []
        for raw in raw_questions:
            if not isinstance(raw, dict):
                continue
            question_number = _safe_int(raw.get("question_number"))
            if not question_number:
                continue
            normalized.append(_normalize_row(raw, exam, year, subject, question_number, source.get("source_pdf", "")))

        output = Path(output_path or "normalized_questions.json")
        _write_json(output, {"questions": normalized})
        summary["output_path"] = str(output)
        summary["question_count"] = len(normalized)
        return summary
    except Exception as exc:
        summary["errors"].append(f"unexpected normalizer error: {exc}")
        _safe_write_empty(output_path or "normalized_questions.json")
        return summary


def _normalize_row(
    raw: Dict[str, Any],
    exam: str,
    year: int,
    subject: str,
    number: int,
    source_pdf: str,
) -> Dict[str, Any]:
    return {
        "id": f"PYQ_G1_{int(year)}_{number:03d}",
        "exam": str(exam),
        "year": int(year),
        "subject": _clean_text(raw.get("subject") or subject),
        "topic": "",
        "subtopic": "",
        "difficulty": "",
        "question_en": _clean_text(raw.get("question_text", "")),
        "question_ta": "",
        "options": _normalize_options(raw.get("options")),
        "correct_answer": "",
        "explanation": {"en": "", "ta": ""},
        "related_note": "",
        "tags": [],
        "repeat_years": [],
        "ai_trick": "",
        "source": source_pdf,
        "source_page": raw.get("page_number"),
        "question_number": number,
    }


def _normalize_options(options: Any) -> Dict[str, str]:
    if not isinstance(options, dict):
        return {}
    normalized = {}
    for key in OPTION_KEYS:
        value = options.get(key)
        if value not in (None, ""):
            normalized[key] = _clean_text(value)
    return normalized


def _clean_text(value: Any) -> str:
    text = str(value or "").replace("\x00", " ").replace("\ufeff", "")
    text = "".join(char for char in text if char == "\n" or char == "\t" or ord(char) >= 32)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _safe_int(value) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _read_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)
        file.write("\n")


def _safe_write_empty(output_path) -> None:
    try:
        _write_json(Path(output_path), {"questions": []})
    except Exception:
        return
