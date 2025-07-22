#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """
    Logs in to quotes.toscrape.com and scrapes protected quotes.
    Returns: list_of_quote_dicts
    """
    session = requests.Session()
    resp = session.get(login_url, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    token = soup.find("input", attrs={"name": "csrf_token"})["value"]

    payload = {
        "csrf_token": token,
        "username": user,
        "password": pwd
    }
    post = session.post(login_url, data=payload, timeout=10)
    post.raise_for_status()

    # After login, scrape the main quotes page (or /hidden if available)
    home = session.get("https://quotes.toscrape.com/", timeout=10)
    home.raise_for_status()
    soup2 = BeautifulSoup(home.text, "html.parser")

    quotes = []
    for block in soup2.select("div.quote"):
        text = block.select_one("span.text").get_text(strip=True)
        author = block.select_one("small.author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in block.select("div.tags a.tag")]
        quotes.append({"text": text, "author": author, "tags": tags})

    return quotes
