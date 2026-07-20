from collections import Counter

from core.question_engine.constants import OPTION_KEYS, REQUIRED_QUESTION_FIELDS
from core.question_engine.models import ValidationResult


def validate_question_schema(question, required_fields=None):
    errors = []
    warnings = []
    row = question if isinstance(question, dict) else {}
    required = required_fields or REQUIRED_QUESTION_FIELDS

    if not isinstance(question, dict):
        return ValidationResult(False, ["invalid schema: question must be a dictionary"])

    for field in required:
        if field == "correct_answer" and "correct_answers" in row:
            val = row.get("correct_answers")
            if val in (None, "", [], {}):
                errors.append("missing required field: correct_answers")
            continue
        if row.get(field) in (None, "", [], {}):
            errors.append(f"missing required field: {field}")

    options = row.get("options")
    if isinstance(options, list):
        options_dict = {}
        for opt in options:
            if isinstance(opt, dict) and "id" in opt:
                val = opt.get("en") or opt.get("ta") or ""
                options_dict[opt["id"]] = val
        options = options_dict
    elif not isinstance(options, dict):
        errors.append("invalid schema: options must be a dictionary")
        options = {}

    if not options:
        errors.append("empty options")
    else:
        for key in OPTION_KEYS:
            if key not in options:
                warnings.append(f"missing option: {key}")
            elif options.get(key) in (None, ""):
                errors.append(f"empty option: {key}")

    correct_answer = row.get("correct_answer")
    correct_answers = row.get("correct_answers")
    if correct_answers is not None:
        values = correct_answers if isinstance(correct_answers, (list, tuple, set)) else [correct_answers]
    elif correct_answer is not None:
        values = [correct_answer]
    else:
        values = []

    for val in values:
        option_key = str(val or "").strip().upper()
        if option_key and option_key not in options:
            errors.append(f"correct answer '{option_key}' is not present in options")

    explanation = row.get("explanation")
    if explanation is not None and not isinstance(explanation, dict):
        errors.append("invalid schema: explanation must be a dictionary")

    tags = row.get("tags")
    if tags is not None and not isinstance(tags, list):
        errors.append("invalid schema: tags must be a list")

    repeat_years = row.get("repeat_years")
    if repeat_years is not None and not isinstance(repeat_years, list):
        errors.append("invalid schema: repeat_years must be a list")

    return ValidationResult(valid=not errors, errors=errors, warnings=warnings)


def validate_duplicate_ids(questions):
    ids = [str(q.get("id")) for q in questions or [] if isinstance(q, dict) and q.get("id")]
    duplicate_ids = sorted(question_id for question_id, count in Counter(ids).items() if count > 1)
    if duplicate_ids:
        return ValidationResult(False, [f"duplicate IDs: {', '.join(duplicate_ids)}"])
    return ValidationResult(True)


def validate_questions(questions, required_fields=None):
    errors = []
    warnings = []
    rows = [q for q in questions or [] if isinstance(q, dict)]

    if len(rows) != len(questions or []):
        errors.append("invalid schema: all questions must be dictionaries")

    duplicate_result = validate_duplicate_ids(rows)
    errors.extend(duplicate_result.errors)

    for index, question in enumerate(rows):
        result = validate_question_schema(question, required_fields=required_fields)
        errors.extend(f"question {index + 1}: {error}" for error in result.errors)
        warnings.extend(f"question {index + 1}: {warning}" for warning in result.warnings)

    return ValidationResult(valid=not errors, errors=errors, warnings=warnings)

