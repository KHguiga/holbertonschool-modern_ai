from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException

def make_driver():
    from selenium.webdriver.chrome.options import Options
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")

    try:
        driver = webdriver.Chrome(options=opts)
        return driver
    except SessionNotCreatedException as e:
        print("❌ SessionNotCreatedException:", e.msg)  # detailed ChromeDriver message
        raise
    except WebDriverException as e:
        print("❌ WebDriverException:", e.msg)
        raise
