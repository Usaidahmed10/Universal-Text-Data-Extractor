
# Universal Text Data Extractor

This is a Python-based universal text extraction and cleaning tool that supports multiple file formats and both digital and scanned documents. It is designed to extract text from the following file types:

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

### Recommended installation:
```bash
pip install -r requirements.txt
````

Contents of `requirements.txt`:

```
pdfplumber
pytesseract
pdf2image
python-docx
python-pptx
pandas
openpyxl
ftfy
beautifulsoup4
selenium
transformers
torch
```

> ⚠️ Note: You will also need to install Tesseract OCR and a compatible browser driver (e.g., ChromeDriver) for Selenium.

---

## 🚀 How to Use

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/universal-text-extractor.git
cd universal-text-extractor
```

2. Run the program:

```bash
python reader.py
```

3. Input the path or URL to your file when prompted.

4. Extracted text will be saved to:

```
extracted_text_<filename>.txt
```

---

## 📦 Folder Structure

```
.
├── reader.py               # Main script
├── reader_pdf.py           # PDF extractor (with OCR support)
├── reader_word.py          # DOCX extractor
├── reader_ppt.py           # PPTX extractor (with OCR fallback)
├── reader_txt.py           # TXT file extractor
├── reader_html.py          # HTML page extractor
├── reader_glossary.py      # XLS glossary extractor
├── requirements.txt
└── README.md
```

---

## 💡 Future Plans

* Add semantic chunking for downstream NLP tasks
* Support multilingual OCR
* Integrate cleaned text directly into vector stores (e.g., OpenSearch, Pinecone)

---

## 📄 License

MIT License. Feel free to use, modify, and contribute!

---

## 🙋‍♂️ Contributions

PRs and suggestions welcome! If you find a bug or want to improve the extractor's performance or compatibility, feel free to open an issue or submit a pull request.

```

Let me know if you want this converted into a downloadable file or customized with your GitHub username.
```
