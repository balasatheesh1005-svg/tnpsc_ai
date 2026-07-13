"""Transparent heuristic difficulty labels."""


def classify(question):
    text = str(question.get("question_en") or "")
    options = question.get("options") or {}
    if len(text) > 350 or any(token in text.lower() for token in ("statement", "assertion", "calculate", "match the following")):
        return "Hard"
    if len(text) > 140 or question.get("subject") in {"Aptitude", "Reasoning"}:
        return "Medium"
    return "Easy"
