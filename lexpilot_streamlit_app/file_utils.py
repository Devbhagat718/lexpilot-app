from PyPDF2 import PdfReader
import docx

def extract_text_from_file(file):
    if file is None:
        return ""
    try:
        if file.type == "application/pdf":
            reader = PdfReader(file)
            return " ".join(page.extract_text() or "" for page in reader.pages)
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(file)
            return "\n".join(p.text for p in doc.paragraphs if p.text)
    except Exception as e:
        return f"Error: {e}"
    return ""
