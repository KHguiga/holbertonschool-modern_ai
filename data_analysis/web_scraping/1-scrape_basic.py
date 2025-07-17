#!/usr/bin/env python3
"""
    Task 1
"""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """
    Uses requests + bs4 to scrape the first page of quotes.toscrape.com.
    - url: the Quotes List endpoint (e.g. 'https://quotes.toscrape.com/')
    - Must extract for each quote:
      * 'text': the quote text
      * 'author': the quote's author
      * 'tags': list of tag strings
    - No regular expressions allowed.
    Returns: list of dicts.
    """
    html = fetch_html(url, headers={"User-Agent": "scraper"}, timeout=10)
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for q in soup.select("div.quote"):
        text = q.select_one("span.text").get_text(strip=True)
        author = q.select_one("small.author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in q.select("div.tags a.tag")]
        results.append({"text": text, "author": author, "tags": tags})
    return results
