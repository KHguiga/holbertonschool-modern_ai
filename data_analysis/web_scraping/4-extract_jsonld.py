import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """
    Extracts schema.org Quote objects from JSON-LD.
    Returns: ("JSON-LD", list_of_quote_dicts)
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    results = []

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            blob = json.loads(script.string or "{}")
        except json.JSONDecodeError:
            continue

        # Normalize to a list of potential quote entries
        items = []
        if isinstance(blob, list):
            items = blob
        elif blob.get("@type") == "Quote":
            items = [blob]
        elif "@graph" in blob:
            items = [n for n in blob["@graph"] if n.get("@type") == "Quote"]

        for itm in items:
            text = itm.get("text", "").strip()
            author = ""
            auth = itm.get("author")
            if isinstance(auth, dict):
                author = auth.get("name", "").strip()
            tags = itm.get("keywords") or []
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",")]

            results.append({"text": text, "author": author, "tags": tags})

    return "JSON-LD", results
