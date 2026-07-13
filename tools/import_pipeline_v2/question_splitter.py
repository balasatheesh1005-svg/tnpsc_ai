"""Split extracted booklet text into numbered question blocks."""
import re

QUESTION = re.compile(r"(?m)^\s*(\d{1,3})\s*[.)]\s+")


def split_questions(pages):
    blocks, warnings = [], []
    for page in pages or []:
        text = str(page.get("text") or "")
        matches = list(QUESTION.finditer(text))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            blocks.append({"question_number": int(match.group(1)), "page_number": page.get("page_number"), "text": text[match.end():end].strip()})
    if not blocks:
        warnings.append("No numbered questions detected.")
    return {"question_blocks": blocks, "warnings": warnings}
