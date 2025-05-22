# reader_word.py
import docx

def extract_text_docx(docx_path):
    try:
        doc = docx.Document(docx_path)
        text = " ".join([para.text.strip() for para in doc.paragraphs if para.text.strip()])
        return text.replace("\n", " ").replace("\t", " ")
    except Exception as e:
        print(f"[ERROR] DOCX Extraction Failed: {e}")
        return ""
