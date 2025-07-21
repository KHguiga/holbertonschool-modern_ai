from selenium import common
from selenium import webdriver
import time


def filter_and_scrape(url, category):
    """
    Clicks a sidebar filter and scrapes the resulting product list.
    Returns: list_of_product_dicts
    """
    opts = webdriver.chrome.options.Options()
    opts.headless = True
    driver = webdriver.Chrome(options=opts)
    driver.get(url)

    # Click the filter label
    try:
        label = driver.find_element(webdriver.common.by.By.XPATH,
                                    f"//label[normalize-space()='{category}']")
        label.click()
    except common.exceptions.StaleElementReferenceException:
        time.sleep(1)
        label = driver.find_element(webdriver.common.by.By.XPATH,
                                    f"//label[normalize-space()='{category}']")
        label.click()

    # Wait for products to refresh
    webdriver.support.ui.WebDriverWait(driver, 10).until(
        webdriver.support.expected_conditions.presence_of_element_located(
            (webdriver.common.by.By.CSS_SELECTOR, "div.thumbnail"))
    )

    # Extract products
    products = []
    for th in driver.find_elements(webdriver.common.by.By.CSS_SELECTOR,
                                   "div.thumbnail"):
        title = th.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                "a.title").get_attribute("title")
        price = th.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                "h4.price").text
        products.append({"title": title, "price": price})

    driver.quit()
    return products
