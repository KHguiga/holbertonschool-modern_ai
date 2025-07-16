#!/usr/bin/env python3
fetch_html = __import__('0-fetch_html').fetch_html
# Test 1: quotes.toscrape.com — basic fetch, expect title in HTML
url1 = "https://quotes.toscrape.com/"
try:
    html1 = fetch_html(url1, headers={"User-Agent": "test-agent"}, timeout=5)
except Exception as e:
    html1 = e

print(str(html1))
