#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrape_products_list(url: str, delay: float = 2.0) -> list:
    opts = Options()
    opts.add_argument("--headless")               # headless mode
    opts.add_argument("--no-sandbox")             # sandbox fix
    opts.add_argument("--disable-dev-shm-usage")  # shared memory fix
    opts.add_argument("--disable-gpu")            # sometimes needed in CI

    driver = webdriver.Chrome(options=opts)
    driver.get(url)
    time.sleep(delay)  # allow static content to load

    cards = driver.find_elements(By.CSS_SELECTOR, ".thumbnail")
    results = []
    for card in cards:
        title_el = card.find_element(By.CSS_SELECTOR, "a.title")
        price_el = card.find_element(By.CSS_SELECTOR, "h4.price")
        desc_el  = card.find_element(By.CSS_SELECTOR, "p.description")
        stars    = card.find_elements(By.CSS_SELECTOR, ".ratings .glyphicon-star")

        results.append({
            "title":       title_el.get_attribute("title").strip(),
            "price":       price_el.text.strip(),
            "description": desc_el.text.strip(),
            "rating":      len(stars),
        })

    driver.quit()
    return results


if __name__ == "__main__":
    url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
    products = scrape_products_list(url)
    print(f"Found {len(products)} products; sample: {products[0]}", end="")
