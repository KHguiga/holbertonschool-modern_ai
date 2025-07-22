#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def scrape_dynamic_table(url: str, max_scrolls: int = 10) -> list:
    """
    Scrolls dynamic e-commerce page and extracts product titles and prices.

    Returns:
        list of {"title": ..., "price": ...}
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    try:
        product_selector = "div.thumbnail"
        scroll_pause = 2
        results = []
        seen = set()

        for _ in range(max_scrolls):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)

            # Grab all visible products
            products = driver.find_elements(By.CSS_SELECTOR, product_selector)
            current_count = len(products)

            if current_count == len(seen):
                break  # No new content, stop

            for item in products:
                try:
                    title = item.find_element(By.CLASS_NAME,
                                              "title"
                                              ).get_attribute("title").strip()
                    price = item.find_element(By.CLASS_NAME,
                                              "price"
                                              ).text.strip()
                    key = (title, price)
                    if key not in seen:
                        seen.add(key)
                        results.append({"title": title, "price": price})
                except Exception:
                    continue

        return results

    finally:
        driver.quit()
