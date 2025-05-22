import pandas as pd

def extract_text_glossary(file_path):
    try:
        df = pd.read_excel(file_path, header=None)
        lines = []
        for _, row in df.iterrows():
            # Join columns with "|", ignore NaN cells
            row_text = " | ".join(str(cell).strip() for cell in row if pd.notna(cell))
            lines.append(row_text)
        return "\n".join(lines).strip()
    except Exception as e:
        print(f"[ERROR] Reading glossary file failed: {e}")
        return ""