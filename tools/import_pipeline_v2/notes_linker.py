"""Link a note only when an exact topic filename is available."""
from pathlib import Path
import re


def link_notes(questions, notes_root="data/notes"):
    root = Path(notes_root)
    rows, linked = [], 0
    for question in questions or []:
        row = dict(question)
        subject = re.sub(r"[^a-z0-9]+", "", str(row.get("subject") or "").lower())
        topic = re.sub(r"[^a-z0-9]+", "_", str(row.get("topic") or "").lower()).strip("_")
        candidate = root / subject / f"{topic}.json"
        value = str(candidate).replace("\\", "/") if topic and candidate.is_file() else ""
        row["related_note"] = value
        row["related_notes"] = value
        linked += bool(value)
        rows.append(row)
    return {"questions": rows, "linked_count": linked}
