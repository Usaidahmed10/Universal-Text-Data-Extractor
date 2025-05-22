# reader.py
import os
import mimetypes
from urllib.parse import urlparse
import re # for the cleaning function
from ftfy import fix_text # for fixing text encoding issues

from reader_pdf import extract_text_pdf
from reader_word import extract_text_docx
from reader_txt import extract_text_txt
from reader_ppt import extract_text_ppt
from reader_html import extract_text_html
from reader_glossary import extract_text_glossary

# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# model_name = "tiiuae/falcon-rw-1b"  # change this to a more powerful one if you have GPU
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# def clean_text_with_llm(text):
#     prompt = (
#         "You are a helpful assistant that cleans extracted text. "
#         "Remove gibberish, extra spaces, newlines, and tabs. "
#         "Improve formatting and coherence but do NOT change the original meaning. "
#         "Clean the following text:\n\n" + text.strip()
#     )

#     response = pipe(prompt, max_new_tokens=500)[0]['generated_text']
#     return response



# Function to clean OCR text
def clean_ocr_text(raw_text):
    # Replace multiple spaces, tabs, and newlines with a single space
    text = re.sub(r"[\t\n\r\f\v]+", " ", raw_text)
    text = re.sub(r"\s{2,}", " ", text)

    # Remove gibberish: lines with mostly symbols or single letters
    lines = text.split(" ")
    lines = [line for line in lines if re.search(r"[a-zA-Z]", line) and len(line) > 2]
    
    # Optional: remove non-ASCII chars
    text = " ".join(lines)
    text = re.sub(r"[^\x00-\x7F]+", "", text)  # remove unicode noise
    return text.strip()

def get_file_type(file_url):
    if file_url.startswith("http"):
        return "html"
    ext = os.path.splitext(file_url)[1].lower()
    if ext == ".pdf":
        return "pdf"
    elif ext == ".docx":
        return "docx"
    elif ext == ".txt":
        return "txt"
    elif ext == ".pptx":
        return "pptx"
    else:
        return "unknown"

def extract_text(file_or_page_url):
    base_name = os.path.basename(file_or_page_url)

    # Special case for the glossary file
    if base_name.lower() == "glossaryofacronyms.xls":
        return extract_text_glossary(file_or_page_url)
    
    file_type = get_file_type(file_or_page_url)
    if file_type == "pdf":
        return extract_text_pdf(file_or_page_url)
    elif file_type == "docx":
        return extract_text_docx(file_or_page_url)
    elif file_type == "txt":
        return extract_text_txt(file_or_page_url)
    elif file_type == "pptx":
        return extract_text_ppt(file_or_page_url)
    elif file_type == "html":
        return extract_text_html(file_or_page_url)
    else:
        print(f"[ERROR] Unsupported file type: {file_type}")
        return ""
    
if __name__ == "__main__":
    import sys
    import os

    # Example input (you can replace this with your file path or URL)
    input_path = input("Enter file path or URL to extract text from: ").strip()

    print("\n[INFO] Extracting text...\n")
    result = extract_text(input_path)

    # Create a filename based on the input file name
    base_name = os.path.basename(input_path)
    output_file = f"extracted_text_{os.path.splitext(base_name)[0]}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"[INFO] Text successfully written to '{output_file}'")