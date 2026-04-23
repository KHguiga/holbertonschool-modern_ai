#!/usr/bin/env python3
"""
Module for basic static web scraping.
"""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """
    Scrapes the first page of quotes from quotes.toscrape.com.

    This function fetches the HTML content from the given URL,
    parses it using BeautifulSoup, and extracts quote information
    including text, author, and associated tags.

    Args:
        url (str): The Quotes List endpoint URL

    Returns:
        list: A list of dictionaries, where each dictionary contains:
              - text (str): The quote text
              - author (str): The quote's author
              - tags (list): A list of tag strings
    """

    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    quotes = []
    quote_blocks = soup.find_all('div', class_='quote')

    for block in quote_blocks:
        text = block.find('span', class_='text').get_text()
        author = block.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in block.find_all('a', class_='tag')]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes