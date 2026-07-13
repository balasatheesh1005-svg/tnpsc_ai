"""Detect duplicates in the candidate and existing JSON repository."""
import hashlib
import json
from pathlib import Path


def check(questions, repository_root="data/pyq"):
    existing_ids, existing_fingerprints = set(), set()
    for path in Path(repository_root).rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            rows = data.get("questions", []) if isinstance(data, dict) else data
            for row in rows if isinstance(rows, list) else []:
                if isinstance(row, dict):
                    existing_ids.add(str(row.get("id") or ""))
                    existing_fingerprints.add(_fingerprint(row))
        except Exception:
            continue
    seen, unique, duplicates = set(), [], []
    for question in questions or []:
        fingerprint = _fingerprint(question)
        reason = "" if fingerprint not in seen and fingerprint not in existing_fingerprints and str(question.get("id") or "") not in existing_ids else "duplicate question text/options"
        if reason:
            duplicates.append({"id": question.get("id"), "reason": reason})
        else:
            seen.add(fingerprint)
            unique.append(question)
    return {"unique_questions": unique, "duplicates": duplicates}


def _fingerprint(question):
    options = question.get("options") or {}
    text = "|".join([str(question.get("question_en") or "").strip().lower(), *(str(options.get(key) or "").strip().lower() for key in "ABCD")])
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
