# from trafilatura import fetch_url, extract
# def extract_content(url):
    # given a url extract the text content in plain format (while change size etc later)
    # downloaded = fetch_url(url)
    # print(downloaded)
    # print(type(downloaded))
    # text = extract(downloaded)
    # print(text)
    # return text

# import requests
# import trafilatura

# def extract_content(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }

#     response = requests.get(url, headers=headers, timeout=20)
#     response.raise_for_status()

#     downloaded = response.text

#     text = trafilatura.extract(downloaded)

#     return text
from playwright.sync_api import sync_playwright
import trafilatura
import time
import random


def extract_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        # realistic browser visit
        page.goto(url, wait_until="networkidle")

        # human-ish pause
        time.sleep(random.uniform(2, 4))

        html = page.content()

        browser.close()

    text = trafilatura.extract(html)

    return text