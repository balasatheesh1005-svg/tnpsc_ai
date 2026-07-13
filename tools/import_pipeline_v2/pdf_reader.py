"""PDF text extraction with safe, dependency-optional fallbacks."""
from pathlib import Path


def read_pdf(pdf_path):
    result = {"source_pdf": str(pdf_path), "pages": [], "warnings": [], "errors": []}
    path = Path(pdf_path)
    if not path.is_file():
        result["errors"].append("PDF file not found")
        return result
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        result["pages"] = [{"page_number": i, "text": page.extract_text() or ""} for i, page in enumerate(reader.pages, 1)]
    except Exception as exc:
        result["errors"].append(f"PDF extraction failed: {exc}")
    if not any(page["text"].strip() for page in result["pages"]):
        result["warnings"].append("No embedded text found; OCR input required.")
    return result
