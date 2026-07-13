"""Match normalized records to the existing official answer-key system."""
from core.question_engine.answer_key import load_answer_key


def match(questions, exam, year):
    answers = load_answer_key(exam, year) or {}
    matched, missing = [], []
    for question in questions or []:
        accepted = answers.get(question.get("id"))
        if not accepted:
            missing.append(question.get("id"))
            continue
        row = dict(question)
        row["correct_answer"] = accepted[0] if len(accepted) == 1 else list(accepted)
        matched.append(row)
    return {"questions": matched, "matched_count": len(matched), "missing_ids": missing, "answer_key_found": bool(answers)}
