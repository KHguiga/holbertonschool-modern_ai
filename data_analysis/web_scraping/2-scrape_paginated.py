#!/usr/bin/env python3
"""
Task 2
"""
from bs4 import BeautifulSoup
import time
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """
    Follows "Next" links on quotes.toscrape.com until none remain.
    - base_url: 'https://quotes.toscrape.com/'
    - Detect and follow <li class="next"><a href="...">
    - Polite delays between requests
    Returns: combined list of all quotes.
    """
    # STUDENT: implement me
    url = base_url
    all_quotes = []
    while True:
        # 1) scrape this page
        all_quotes.extend(scrape_basic(url))

        # 2) find Next link
        page_html = fetch_html(url, headers={"User-Agent": "scraper"},
                               timeout=10)
        soup = BeautifulSoup(page_html, "html.parser")
        nxt = soup.select_one("li.next > a")
        if not nxt:
            break
        url = base_url.rstrip("/") + nxt["href"]
        time.sleep(1)
    return all_quotes
