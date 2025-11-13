#!/usr/bin/env python3
"""
    Task 7
"""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    opts = webdriver.chrome.options.Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=opts)
    driver.get(url)
    time.sleep(delay)  # ensure content loads

    title_el = driver.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                   ".caption h4:nth-of-type(2)")
    price_el = driver.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                   ".price")
    desc_el = driver.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                  ".description")
    stars = driver.find_elements(webdriver.common.by.By.CSS_SELECTOR,
                                 ".ratings .ws-icon.ws-icon-star")

    result = {
        "title":       title_el.text.strip(),
        "price":       price_el.text.strip(),
        "description": desc_el.text.strip(),
        "rating":      len(stars),
    }

    driver.quit()
    return result
