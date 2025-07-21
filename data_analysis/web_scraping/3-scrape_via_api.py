#!/usr/bin/env python3
"""
Task 3: API‑First Scraping (using fetch_html)
"""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """
    API‑first scraper for quotes.toscrape.com
    Returns: list_of_quote_dicts with keys: text, author, tags
    """
    quotes = []
    page = 1

    while True:
        api_url = f"{base_url.rstrip('/')}/api/quotes?page={page}"
        # fetch_html will raise for bad status
        text = fetch_html(api_url, headers={"User-Agent": "api-scraper"},
                          timeout=10)
        data = json.loads(text)

        # Collect quotes (text, author name, tags)
        for item in data.get("quotes", []):
            quotes.append({
                "text":   item.get("text", "").strip(),
                "author": item.get("author", {}).get("name", "").strip(),
                "tags":   item.get("tags", [])
            })

        if not data.get("has_next", False):
            break
        page += 1

    return quotes
