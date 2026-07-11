"""Stage 1: extract raw question text from official TNPSC PDFs.

This module performs extraction only. It does not validate, normalize, enrich,
or import questions.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional


OPTION_PATTERN = re.compile(r"^\s*([A-D])\s*[\).]\s*(.*)$")
QUESTION_PATTERN = re.compile(r"^\s*(\d{1,3})\s*[\).]\s*(.*)$")


def extract_pdf(pdf_path, output_path=None) -> Dict[str, Any]:
    """Read a PDF and write raw_questions.json without crashing."""
    summary = {
        "input_pdf": str(pdf_path or ""),
        "output_path": str(output_path or "raw_questions.json"),
        "question_count": 0,
        "warnings": [],
        "errors": [],
    }

    try:
        pdf = Path(pdf_path)
        output = Path(output_path or "raw_questions.json")
        pages = _extract_pages(pdf, summary)
        raw_questions = _parse_questions(pages)

        payload = {
            "source_pdf": str(pdf),
            "raw_questions": raw_questions,
            "pages": pages,
            "warnings": list(summary["warnings"]),
        }
        _write_json(output, payload)

        summary["output_path"] = str(output)
        summary["question_count"] = len(raw_questions)
        return summary
    except Exception as exc:
        summary["errors"].append(f"unexpected extractor error: {exc}")
        _safe_write_failure(output_path or "raw_questions.json", summary)
        return summary


def _extract_pages(pdf: Path, summary: Dict[str, Any]) -> List[Dict[str, Any]]:
    if not pdf.exists() or not pdf.is_file():
        summary["errors"].append("PDF file not found")
        return []

    pages = _extract_with_pypdf(pdf, summary)
    if pages:
        return pages

    pages = _extract_with_pymupdf(pdf, summary)
    if pages:
        return pages

    summary["warnings"].append(
        "No extractable text found. Scanned PDFs require OCR before normalization."
    )
    return []


def _extract_with_pypdf(pdf: Path, summary: Dict[str, Any]) -> List[Dict[str, Any]]:
    reader_cls = None
    try:
        from pypdf import PdfReader

        reader_cls = PdfReader
    except Exception:
        try:
            from PyPDF2 import PdfReader

            reader_cls = PdfReader
        except Exception:
            summary["warnings"].append("pypdf/PyPDF2 is not available")
            return []

    try:
        reader = reader_cls(str(pdf))
        pages = []
        for index, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            if text.strip():
                pages.append({"page_number": index, "text": text})
        return pages
    except Exception as exc:
        summary["warnings"].append(f"pypdf extraction failed: {exc}")
        return []


def _extract_with_pymupdf(pdf: Path, summary: Dict[str, Any]) -> List[Dict[str, Any]]:
    try:
        import fitz
    except Exception:
        summary["warnings"].append("PyMuPDF is not available")
        return []

    try:
        document = fitz.open(str(pdf))
        pages = []
        for index, page in enumerate(document, start=1):
            text = page.get_text("text") or ""
            if text.strip():
                pages.append({"page_number": index, "text": text})
        return pages
    except Exception as exc:
        summary["warnings"].append(f"PyMuPDF extraction failed: {exc}")
        return []


def _parse_questions(pages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    questions = []
    current: Optional[Dict[str, Any]] = None

    for page in pages:
        page_number = page.get("page_number")
        for line in str(page.get("text") or "").splitlines():
            cleaned = _clean_line(line)
            if not cleaned:
                continue

            question_match = QUESTION_PATTERN.match(cleaned)
            option_match = OPTION_PATTERN.match(cleaned)

            if question_match:
                if current:
                    questions.append(current)
                current = {
                    "question_number": int(question_match.group(1)),
                    "page_number": page_number,
                    "question_text": question_match.group(2).strip(),
                    "options": {},
                    "raw_lines": [cleaned],
                }
                continue

            if current:
                current["raw_lines"].append(cleaned)
                if option_match:
                    current["options"][option_match.group(1)] = option_match.group(2).strip()
                elif len(current["options"]) < 1:
                    current["question_text"] = f"{current['question_text']} {cleaned}".strip()

    if current:
        questions.append(current)

    return questions


def _clean_line(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "").replace("\x00", " ")).strip()


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)
        file.write("\n")


def _safe_write_failure(output_path, summary: Dict[str, Any]) -> None:
    try:
        _write_json(Path(output_path), {"source_pdf": summary.get("input_pdf"), "raw_questions": []})
    except Exception:
        return
