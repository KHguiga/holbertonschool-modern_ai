#!/usr/bin/env python3
from selenium import webdriver
import time


def scrape_dynamic_table(url):
    """
    Scrapes JS‑rendered laptop listings by scrolling to load all items.
    Returns: list_of_product_dicts
    """
    opts = webdriver.chrome.options.Options()
    opts.headless = True
    driver = webdriver.Chrome(options=opts)
    driver.get(url)

    # Scroll until no new content
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # wait for new thumbnails
        webdriver.support.ui.WebDriverWait(driver, 10).until(
            webdriver.support.expected_conditions.presence_of_element_located(
                (webdriver.common.by.By.CSS_SELECTOR, "div.thumbnail"))
        )
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract products
    products = []
    thumbs = driver.find_elements(webdriver.common.by.By.CSS_SELECTOR,
                                  "div.thumbnail")
    for th in thumbs:
        title = th.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "a.title"
            ).get_attribute("title")
        price = th.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "h4.price"
            ).text
        products.append({"title": title, "price": price})

    driver.quit()
    return products
