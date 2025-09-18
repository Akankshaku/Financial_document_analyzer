
from pathlib import Path

def read_pdf_text(path):
    try:
        from PyPDF2 import PdfReader
    except Exception:
        return None
    p = Path(path)
    if not p.exists():
        return None
    try:
        reader = PdfReader(str(p))
        text_parts = []
        for page in reader.pages:
            text_parts.append(page.extract_text() or '')
        return '\n'.join(text_parts)
    except Exception:
        return None
