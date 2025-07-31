#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def scroll_and_scrape(url: str, scroll_pause: float = 2.0) -> list:
    """
    Opens an infinite-scroll page, scrolls until fully loaded, and
    scrapes each product's title, price, description, and rating,
    deduplicating by (title, price).
    """
    # 1) Setup headless Chrome
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)

    # 2) Load the page and let initial content render
    driver.get(url)
    time.sleep(scroll_pause)

    # 3) Scroll until no new content is loaded
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 4) Extract product details with deduplication
    seen = set()
    results = []
    cards = driver.find_elements(By.CSS_SELECTOR, "div.thumbnail")
    for card in cards:
        title_el = card.find_element(By.CSS_SELECTOR, "a.title")
        price_el = card.find_element(By.CSS_SELECTOR, "h4.price")
        desc_el = card.find_element(By.CSS_SELECTOR, "p.description")
        stars = card.find_elements(By.CSS_SELECTOR, ".ratings .glyphicon-star")

        title = title_el.get_attribute("title").strip()
        price = price_el.text.strip()
        key = (title, price)
        if key in seen:
            continue
        seen.add(key)

        results.append({
            "title":       title,
            "price":       price,
            "description": desc_el.text.strip(),
            "rating":      len(stars),
        })

    driver.quit()
    return results
