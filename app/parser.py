import os
from PyPDF2 import PdfReader
from docx import Document


def parse_file(path: str) -> str:
    # مسار تحويل 
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")

    # TXT
    if path.endswith(".txt"):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    # PDF
    elif path.endswith(".pdf"):
        reader = PdfReader(full_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    # docx
    elif path.endswith(".docx"):
        doc = Document(full_path)
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        raise ValueError("Unsupported file type")