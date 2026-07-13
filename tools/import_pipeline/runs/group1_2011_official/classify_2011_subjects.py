"""Subject-only classification for the official Group 1 2011 dataset."""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


DATASET = Path("data/pyq/group1/group1_2011_official.json")
REPORT = Path("tools/import_pipeline/runs/group1_2011_official/subject_classification_validation_report.json")
ALLOWED = {
    "Polity", "History", "Geography", "Economy", "Science", "Environment",
    "Current Affairs", "Aptitude", "Reasoning", "Tamil Society", "Indian Society",
    "Art & Culture", "General Knowledge",
}
SUBJECTS = [
    "History", "Geography", "Current Affairs", "Art & Culture", "Polity",
    "General Knowledge", "History", "Aptitude", "Economy", "Economy",
    "Economy", "Polity", "Current Affairs", "Science", "History", "History",
    "Aptitude", "Science", "Economy", "Economy", "Environment", "History",
    "History", "Economy", "Science", "Aptitude", "Polity", "Geography",
    "History", "General Knowledge", "Science", "Tamil Society", "History", "Current Affairs",
    "History", "Polity", "Economy", "Art & Culture", "History", "Science",
    "Aptitude", "Polity", "Science", "General Knowledge", "Geography", "History",
    "Science", "Science", "Environment", "Science",
]


def non_subject_hash(rows):
    stripped = [{key: value for key, value in row.items() if key != "subject"} for row in rows]
    payload = json.dumps(stripped, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main():
    before_text = DATASET.read_text(encoding="utf-8")
    before_rows = json.loads(before_text)
    before_hash = non_subject_hash(before_rows)
    if len(before_rows) != len(SUBJECTS):
        raise RuntimeError(f"expected {len(SUBJECTS)} records, found {len(before_rows)}")

    subject_index = 0

    def replace_subject(_match):
        nonlocal subject_index
        subject = SUBJECTS[subject_index]
        subject_index += 1
        return f'"subject": "{subject}"'

    after_text, replacement_count = re.subn(
        r'"subject": "[^"]*"', replace_subject, before_text
    )
    if replacement_count != len(SUBJECTS):
        raise RuntimeError(f"expected {len(SUBJECTS)} subject fields, found {replacement_count}")
    DATASET.write_text(after_text, encoding="utf-8")

    after_rows = json.loads(DATASET.read_text(encoding="utf-8"))
    after_hash = non_subject_hash(after_rows)
    changed_non_subject_rows = [
        index + 1
        for index, (before, after) in enumerate(zip(before_rows, after_rows))
        if {key: value for key, value in before.items() if key != "subject"}
        != {key: value for key, value in after.items() if key != "subject"}
    ]
    invalid_subject_rows = [
        {"id": row.get("id"), "subject": row.get("subject")}
        for row in after_rows
        if row.get("subject") not in ALLOWED
    ]
    nonblank_explanation_rows = [
        row.get("id")
        for row in after_rows
        if row.get("explanation") not in ({"en": "", "ta": ""}, None, "")
    ]
    report = {
        "dataset": str(DATASET),
        "record_count": len(after_rows),
        "allowed_subjects": sorted(ALLOWED),
        "invalid_subject_rows": invalid_subject_rows,
        "subject_counts": dict(sorted(Counter(row["subject"] for row in after_rows).items())),
        "classified_subject_fields": len(after_rows),
        "nonblank_explanation_rows": nonblank_explanation_rows,
        "non_subject_content_hash_before": before_hash,
        "non_subject_content_hash_after": after_hash,
        "non_subject_content_unchanged": before_hash == after_hash and not changed_non_subject_rows,
        "changed_non_subject_rows": changed_non_subject_rows,
        "validation_result": "pass" if not invalid_subject_rows and not nonblank_explanation_rows and before_hash == after_hash and not changed_non_subject_rows else "fail",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
