#!/usr/bin/env python3
import requests


def fetch_html(url, headers=None, timeout=10):
    """
    Fetches the given URL and returns its HTML as text.
    - url: the page to GET
    - headers: optional HTTP headers (e.g. {'User-Agent': '...'})
    - timeout: seconds before aborting
    Raises an exception on any HTTP status >= 400.
    Returns: the full HTML as a string.
    """
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.text
