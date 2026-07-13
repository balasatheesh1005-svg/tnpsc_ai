def build_progress_state(index, total):
    total = max(int(total or 0), 0)
    if total == 0:
        return {"current": 0, "total": 0, "percent": 0}

    current = max(1, min(int(index or 0) + 1, total))
    return {
        "current": current,
        "total": total,
        "percent": current / total,
    }


def is_correct_answer(selected_answer, correct_answer):
    selected = str(selected_answer or "").strip()
    if isinstance(correct_answer, (list, tuple, set)):
        return selected in {str(answer or "").strip() for answer in correct_answer}
    return selected == str(correct_answer or "").strip()


def score_attempts(attempts):
    rows = list(attempts or [])
    if not rows:
        return {"attempted": 0, "correct": 0, "accuracy": 0}

    correct = sum(1 for item in rows if item.get("is_correct"))
    return {
        "attempted": len(rows),
        "correct": correct,
        "accuracy": round((correct / len(rows)) * 100, 2),
    }
