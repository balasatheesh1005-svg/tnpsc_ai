def clamp_index(index, total):
    if total <= 0:
        return 0
    try:
        current = int(index)
    except (TypeError, ValueError):
        current = 0
    return max(0, min(current, total - 1))


def next_index(index, total):
    return clamp_index(clamp_index(index, total) + 1, total)


def previous_index(index, total):
    return clamp_index(clamp_index(index, total) - 1, total)


def get_current_question(questions, index):
    rows = list(questions or [])
    if not rows:
        return None, 0
    current = clamp_index(index, len(rows))
    return rows[current], current


def has_next(index, total):
    return total > 0 and clamp_index(index, total) < total - 1


def has_previous(index, total):
    return total > 0 and clamp_index(index, total) > 0

