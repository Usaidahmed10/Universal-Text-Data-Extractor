# reader_pdf.py
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import io


def is_scanned_pdf(pdf_path):
    # try:
    #     with pdfplumber.open(pdf_path) as pdf:
    #         for page in pdf.pages:
    #             if page.extract_text():
    #                 return False  # has extractable text
    #     return True
    # except: 
    #     return True  # if any error, assume scanned
    return True  # Placeholder for actual implementation



def extract_text_pdf(pdf_path):
    try:
        text = ""
        if is_scanned_pdf(pdf_path):
            images = convert_from_path(pdf_path)
            print("scanned pdf")
            for image in images:
                scanned_text = pytesseract.image_to_string(image)
                scanned_text = scanned_text.strip() #.replace("\n", " ").replace("\t", " ")
                text += scanned_text + " "
        else:
            print("not scanned pdf")
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        page_text = page_text.strip() #.replace("\n", " ").replace("\t", " ")
                        text += page_text + " "
        return text.strip()
    except Exception as e:
        print(f"[ERROR] PDF Extraction Failed: {e}")
        return ""