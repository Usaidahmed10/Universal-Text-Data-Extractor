# Universal-Text-Data-Extractor
A Python-based tool for extracting and cleaning text from multiple document formats including PDF, DOCX, PPTX, TXT, HTML, and XLS. Supports OCR for scanned files and optional LLM-powered cleaning.

- 📄 PDF (including OCR for scanned PDFs)
- 📚 DOCX (Word documents)
- 📊 PPTX (PowerPoint slides with OCR fallback)
- 📃 TXT (plain text files)
- 🌐 HTML (web pages via Selenium and BeautifulSoup)
- 📘 XLS (glossary-specific Excel files)

---

## 🧰 Features

- 🔍 Automatically detects file type
- 🧼 Cleans extracted text (removes gibberish, extra whitespace, etc.)
- 🧠 Optional LLM-based cleaning with Hugging Face models
- 🤖 OCR support for scanned PDFs and PPTX using `pytesseract`
- 📜 Saves cleaned output to a text file

---

## 🛠️ Requirements

- Python 3.7+
- pip packages listed in `requirements.txt`

### Recommended packages:
```bash
pip install -r requirements.txt

