"""Parse A-D options without changing their text or order."""
import re

OPTION = re.compile(r"(?mi)^\s*\(?([A-D])\)?\s*[.)\-:]\s*")


def parse_options(blocks):
    questions, rejected = [], []
    for block in blocks or []:
        text = str(block.get("text") or "")
        matches = list(OPTION.finditer(text))
        if len(matches) < 4:
            rejected.append({"question_number": block.get("question_number"), "reason": "four A-D options not detected"})
            continue
        first = matches[0]
        options = {}
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            key, value = match.group(1).upper(), text[match.end():end].strip()
            if key in "ABCD" and key not in options:
                options[key] = value
        if tuple(options) != ("A", "B", "C", "D") or any(not value for value in options.values()):
            rejected.append({"question_number": block.get("question_number"), "reason": "options are incomplete or out of order"})
            continue
        questions.append({"question_number": block.get("question_number"), "page_number": block.get("page_number"), "question_text": text[:first.start()].strip(), "options": options})
    return {"questions": questions, "rejected": rejected}
