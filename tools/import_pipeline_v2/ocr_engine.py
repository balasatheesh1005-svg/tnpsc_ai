"""OCR cleanup stage. External OCR is intentionally optional."""
import re


def cleanup_pages(pages):
    cleaned, warnings = [], []
    for page in pages or []:
        text = str(page.get("text") or "").replace("\x00", " ")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        cleaned.append({"page_number": page.get("page_number"), "text": text})
    if not any(page["text"] for page in cleaned):
        warnings.append("OCR cleanup cannot create text; provide a text PDF or OCR output.")
    return {"pages": cleaned, "warnings": warnings}
