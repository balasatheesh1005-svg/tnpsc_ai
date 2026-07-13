"""Build OCR-assisted raw records for the image-only official 2011 paper.

The local PDF remains the canonical source.  The downloaded public transcript
is used only to recover selectable English text from its scanned pages.
"""

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).parent
PDF = "official_group1_2011.pdf"


def clean(fragment):
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.I)
    parts = re.findall(r"<p[^>]*>(.*?)</p>|<td[^>]*>(.*?)</td>", fragment, flags=re.I | re.S)
    values = []
    for pair in parts:
        value = html.unescape(re.sub(r"<[^>]+>", " ", pair[0] or pair[1]))
        value = re.sub(r"\s+", " ", value).strip()
        # The site emits Tamil with a legacy encoding; retain its English text only.
        if value and "à" not in value and not re.search(r"[\u0b80-\u0bff]", value):
            values.append(value)
    return "\n".join(values).strip()


def parse_page(path):
    source = path.read_text(encoding="utf-8", errors="replace")
    records, rejected = [], []
    for block in re.split(r'<div class="mt-4 mt-50 mg-bottom-30 qus">', source)[1:]:
        number = re.search(r'<div class="qusnum">\s*(\d+)\.', block)
        question = re.search(r'<div class="qusdes">(.*?)</div>\s*</div>', block, re.S)
        if not number or not question:
            continue
        options = {}
        for option_block in re.split(r'onclick="changeemoji\([^"]+"', block)[1:5]:
            key = re.search(r'<div class="qusnum">\s*([A-D])\.', option_block)
            value = re.search(r'<div class="qusdes">(.*?)</div>\s*</div>', option_block, re.S)
            if key and value:
                options[key.group(1)] = clean(value.group(1))
        row = {
            "question_number": int(number.group(1)),
            "question_text": clean(question.group(1)),
            "options": options,
            "source_pdf": PDF,
        }
        if not row["question_text"] or set(options) != {"A", "B", "C", "D"} or any(not value for value in options.values()):
            rejected.append({"question_number": row["question_number"], "reason": "missing question text or complete A-D options"})
        else:
            records.append(row)
    return records, rejected


def main():
    all_rows, rejected = [], []
    for page in sorted(ROOT.glob("transcript_page_*.html")):
        rows, errors = parse_page(page)
        all_rows.extend(rows)
        rejected.extend(errors)
    all_rows.sort(key=lambda row: row["question_number"])
    # The existing seed was transcribed directly from the official scans for
    # questions 1–12.  Prefer it over the OCR-assist transcript where it
    # preserves scan punctuation, spelling, and mathematical glyphs.
    seed_path = Path("data/pyq/group1/group1_2011_seed.json")
    if seed_path.exists():
        seed = json.loads(seed_path.read_text(encoding="utf-8"))
        for row, verified in zip(all_rows[:12], seed[:12]):
            row["question_text"] = verified["question_en"]
            row["options"] = verified["options"]
    numbers = [row["question_number"] for row in all_rows]
    expected = list(range(1, max(numbers, default=0) + 1))
    missing = sorted(set(expected) - set(numbers))
    payload = {"source_pdf": PDF, "raw_questions": all_rows, "ocr_assist": True}
    (ROOT / "raw_questions.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {"accepted_count": len(all_rows), "rejected": rejected, "missing_question_numbers": missing}
    (ROOT / "ocr_ingestion_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
