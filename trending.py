from typing import List

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options


def get_source_with_webdriver(headless=False) -> str:
    #TODO: decide if headless is necessary
    chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox") # linux only
    if headless:
        chrome_options.add_argument("--headless")
        # chrome_options.headless = True # also works
    browser = webdriver.Chrome(options=chrome_options)

    browser.get('https://www.twitter.com/explore/tabs/trending')
    try:
        element_located = EC.presence_of_element_located((By.XPATH, '//*[text()[contains(.,"United States")]]'))
        WebDriverWait(browser, timeout=100).until(element_located)
        print('Located element United States done')
    except Exception as e:
        print('WebDriver timed out!', e)

    source = browser.page_source
    return source


def get_trending(source: str) -> List[str]:
    soup = BeautifulSoup(source, features='html.parser')
    text = list(soup.stripped_strings)

    topics = []
    for i in range(len(text)):
        if 'Trending' in text[i]:
            topics.append(text[i + 1])
    topics.remove('News')
    return topics

if __name__ == "__main__":
    source:str = get_source_with_webdriver()
    topics: List[str] = get_trending(source)
    print(topics)
    print("Num trending:", len(topics))
