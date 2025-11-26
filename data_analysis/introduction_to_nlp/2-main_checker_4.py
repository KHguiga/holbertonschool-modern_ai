#!/usr/bin/env python3
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text

"""
Integration test with clean_text().
"""
raw = "Visit www.freeoffers.com 😂 now!!!"
cleaned = clean_text(raw)
tokens = tokenize_text(cleaned, method="tweet")

print("Raw   :", repr(raw))
print("Clean :", repr(cleaned))
print("Tokens:", repr(tokens), end="")
