#!/usr/bin/env python3
import time
from selenium import webdriver


def scrape_products(url, delay=2.0):
    opts = webdriver.chrome.options.Options()
    opts.add_argument("--headless")
    opts.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=opts)
    driver.get(url)
    time.sleep(delay)  # let static content load

    cards = driver.find_elements(webdriver.common.by.By.CSS_SELECTOR,
                                 ".thumbnail")
    results = []
    for card in cards:
        title_el = card.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                     "a.title")
        price_el = card.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                     "h4.price")
        desc_el = card.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                    "p.description")
        stars = card.find_elements(webdriver.common.by.By.CSS_SELECTOR,
                                   ".ratings .glyphicon-star")

        results.append({
            "title":       title_el.get_attribute("title").strip(),
            "price":       price_el.text.strip(),
            "description": desc_el.text.strip(),
            "rating":      len(stars),
        })

    driver.quit()
    return results
