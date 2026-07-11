def normalize_text(value):
    return str(value or "").strip().lower()


def question_search_blob(question):
    values = [
        question.get("id"),
        question.get("exam"),
        question.get("year"),
        question.get("subject"),
        question.get("topic"),
        question.get("subtopic"),
        question.get("difficulty"),
        question.get("question_en"),
        question.get("question_ta"),
        question.get("ai_trick"),
        question.get("source"),
        question.get("practice_set"),
        question.get("related_note"),
    ]

    for option_key in ("options", "options_en", "options_ta"):
        options = question.get(option_key)
        if isinstance(options, dict):
            values.extend(options.values())
        elif isinstance(options, list):
            values.extend(options)

    explanation = question.get("explanation")
    if isinstance(explanation, dict):
        values.extend(explanation.values())
    else:
        values.extend([question.get("explanation_en"), question.get("explanation_ta")])

    tags = question.get("tags")
    if isinstance(tags, list):
        values.extend(tags)

    return " ".join(str(value or "") for value in values).lower()


def matches_field(question, fields, expected):
    expected_text = normalize_text(expected)
    return any(normalize_text(question.get(field)) == expected_text for field in fields)


def search_questions(questions, keyword):
    term = normalize_text(keyword)
    if not term:
        return list(questions or [])
    return [question for question in questions or [] if term in question_search_blob(question)]


def filter_questions(questions, criteria=None, keyword=None, all_value_prefix="All"):
    filtered = list(questions or [])

    for field, expected in (criteria or {}).items():
        if not expected or str(expected).startswith(all_value_prefix):
            continue
        filtered = [
            question
            for question in filtered
            if str(question.get(field, "")) == str(expected)
        ]

    return search_questions(filtered, keyword)

