"""Generate approved empty explanation placeholders only."""


def add_placeholders(questions):
    rows = []
    for question in questions or []:
        row = dict(question)
        row["explanation"] = {"en": "", "ta": ""}
        row["english_explanation"] = ""
        row["tamil_explanation"] = ""
        row["ai_trick"] = ""
        rows.append(row)
    return rows
