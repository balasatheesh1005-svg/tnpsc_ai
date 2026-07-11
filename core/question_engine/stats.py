from collections import Counter


def get_facets(questions, fields):
    facets = {}
    for field in fields:
        values = []
        for question in questions or []:
            value = question.get(field)
            if value in (None, ""):
                continue
            values.append(value)
        if field == "year":
            facets[field] = sorted(
                set(values),
                key=lambda value: int(value) if str(value).isdigit() else -1,
                reverse=True,
            )
        else:
            facets[field] = sorted(set(values), key=lambda value: str(value).lower())
    return facets


def most_repeated_topics(questions, limit=6):
    repeated = Counter()
    for question in questions or []:
        topic = question.get("topic")
        repeat_years = question.get("repeat_years") or []
        weight = len(repeat_years) if isinstance(repeat_years, list) else 0
        if topic:
            repeated[str(topic)] += max(weight, 1)
    return repeated.most_common(limit)


def count_by_field(questions, field):
    counter = Counter()
    for question in questions or []:
        value = question.get(field)
        if value not in (None, ""):
            counter[str(value)] += 1
    return counter
