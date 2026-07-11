def session_key(prefix, name):
    return f"{prefix}_{name}"


def init_question_session(state, prefix, defaults=None):
    base_defaults = {
        "index": 0,
        "answered": False,
        "selected_answer": None,
        "attempts": [],
        "started_at": 0,
        "bookmarks": [],
    }
    base_defaults.update(defaults or {})

    for name, value in base_defaults.items():
        state.setdefault(session_key(prefix, name), value)


def get_session_value(state, prefix, name, default=None):
    return state.get(session_key(prefix, name), default)


def set_session_value(state, prefix, name, value):
    state[session_key(prefix, name)] = value


def reset_answer(state, prefix):
    set_session_value(state, prefix, "answered", False)
    set_session_value(state, prefix, "selected_answer", None)


def record_answer(state, prefix, selected_answer, is_correct=None, question_id=None):
    set_session_value(state, prefix, "answered", True)
    set_session_value(state, prefix, "selected_answer", selected_answer)

    attempts = list(get_session_value(state, prefix, "attempts", []))
    attempts.append(
        {
            "question_id": question_id,
            "selected_answer": selected_answer,
            "is_correct": is_correct,
        }
    )
    set_session_value(state, prefix, "attempts", attempts)

