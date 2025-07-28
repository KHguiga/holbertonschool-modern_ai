#!/usr/bin/env python3
import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def scrape_products_list(url: str, delay: float = 2.0) -> list:
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    # ensure each session has its own user-data-dir
    temp_dir = tempfile.mkdtemp(prefix="selenium-user-data-")
    opts.add_argument(f"--user-data-dir={temp_dir}")
    driver = webdriver.Chrome(options=opts)
    driver.get(url)
    time.sleep(delay)  # let static content load

    cards = driver.find_elements(By.CSS_SELECTOR, ".thumbnail")
    results = []
    for card in cards:
        title_el = card.find_element(By.CSS_SELECTOR, "a.title")
        price_el = card.find_element(By.CSS_SELECTOR, "h4.price")
        desc_el = card.find_element(By.CSS_SELECTOR, "p.description")
        stars = card.find_elements(By.CSS_SELECTOR, ".ratings .glyphicon-star")

        results.append({
            "title":       title_el.get_attribute("title").strip(),
            "price":       price_el.text.strip(),
            "description": desc_el.text.strip(),
            "rating":      len(stars),
        })

    driver.quit()
    return results
