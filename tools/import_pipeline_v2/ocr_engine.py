"""OCR cleanup stage with an optional Tesseract fallback for image PDFs."""
import re
from pathlib import Path
from io import BytesIO


def cleanup_pages(pages, pdf_path=None, dpi=200):
    cleaned, warnings = [], []
    for page in pages or []:
        text = str(page.get("text") or "").replace("\x00", " ")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        cleaned.append({"page_number": page.get("page_number"), "text": text})
    if not any(page["text"] for page in cleaned):
        ocr_pages, ocr_warnings = _ocr_pdf(pdf_path, dpi)
        cleaned = ocr_pages or cleaned
        warnings.extend(ocr_warnings)
    if not any(page["text"] for page in cleaned):
        warnings.append("OCR cleanup cannot create text; provide a text PDF or OCR output.")
    return {"pages": cleaned, "warnings": warnings}


def _ocr_pdf(pdf_path, dpi):
    if not pdf_path or not Path(pdf_path).is_file():
        return [], ["OCR skipped: source PDF is unavailable."]
    try:
        import fitz
        import pytesseract
        from PIL import Image
        executable = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
        if executable.is_file():
            pytesseract.pytesseract.tesseract_cmd = str(executable)
        document = fitz.open(str(pdf_path))
        scale = max(1.0, float(dpi) / 72.0)
        pages = []
        for number, page in enumerate(document, 1):
            pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csGRAY, alpha=False)
            image = Image.open(BytesIO(pixmap.tobytes("png")))
            text = pytesseract.image_to_string(image, config="--psm 6")
            pages.append({"page_number": number, "text": text})
        return pages, []
    except Exception as exc:
        return [], [f"OCR failed: {exc}"]
