clean_text = __import__('1-clean_text').clean_text

"""
Tests that URLs and numbers are replaced by placeholders <URL> and <NUM>.
"""
if __name__ == "__main__":
    cleaned = []
    texts = [
        "Visit https://example.com for 2 days!",
        "Call www.test.org or dial 12345"
    ]
    for t in texts:
        cleaned.append(clean_text(t))
    print(repr(cleaned))
