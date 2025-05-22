# reader_html.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def extract_text_html(page_url):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(page_url)
        time.sleep(2)
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator=" ").strip().replace("\n", " ").replace("\t", " ")
        return text
    except Exception as e:
        print(f"[ERROR] HTML Extraction Failed: {e}")
        return ""
