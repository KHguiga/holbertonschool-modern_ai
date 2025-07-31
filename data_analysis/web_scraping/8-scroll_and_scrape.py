#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def scroll_and_scrape(url: str, scroll_pause: float = 2.0) -> list:
    """
    Scrolls an infinite-scroll page, deduplicates by (title, price),
    and returns a list of product dicts.
    """
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=opts)

    driver.get(url)
    time.sleep(scroll_pause)

    # Scroll until no new height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract products with deduplication
    seen = set()
    results = []
    cards = driver.find_elements(By.CSS_SELECTOR, "div.thumbnail")
    for card in cards:
        title_el = card.find_element(By.CSS_SELECTOR, "a.title")
        price_el = card.find_element(By.CSS_SELECTOR, "h4.price")
        title = title_el.get_attribute("title").strip()
        price = price_el.text.strip()
        key = (title, price)
        if key not in seen:
            seen.add(key)
            results.append({"title": title, "price": price})

    driver.quit()
    return results
