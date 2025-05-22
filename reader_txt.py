# reader_txt.py

def extract_text_txt(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            text = f.read()
            return text.strip().replace("\n", " ").replace("\t", " ")
    except Exception as e:
        print(f"[ERROR] TXT Extraction Failed: {e}")
        return ""
