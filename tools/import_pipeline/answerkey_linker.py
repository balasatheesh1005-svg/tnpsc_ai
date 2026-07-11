"""Stage 4: attach official answers when verified keys exist."""

import json
from pathlib import Path
from typing import Any, Dict, List

from core.question_engine.answer_key import get_correct_answer


def link_answer_key(input_path, output_path=None) -> Dict[str, Any]:
    """Attach correct_answer values from official answer keys when available."""
    summary = {
        "input_path": str(input_path or ""),
        "output_path": str(output_path or "verified_questions.json"),
        "linked_count": 0,
        "unverified_count": 0,
        "errors": [],
    }

    try:
        rows = _load_questions(Path(input_path))
        verified = []
        for question in rows:
            row = dict(question)
            official_answer = get_correct_answer(row.get("id"))
            if official_answer:
                row["correct_answer"] = official_answer
                summary["linked_count"] += 1
            else:
                row["correct_answer"] = ""
                summary["unverified_count"] += 1
            verified.append(row)

        output = Path(output_path or "verified_questions.json")
        _write_json(output, {"questions": verified})
        summary["output_path"] = str(output)
        return summary
    except Exception as exc:
        summary["errors"].append(f"unexpected answer-key linker error: {exc}")
        _safe_write_empty(output_path or "verified_questions.json")
        return summary


def _load_questions(path: Path) -> List[Dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, dict) and isinstance(data.get("questions"), list):
            return [row for row in data["questions"] if isinstance(row, dict)]
        if isinstance(data, list):
            return [row for row in data if isinstance(row, dict)]
    except Exception:
        return []
    return []


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
