#!/usr/bin/env python3
generate_ngrams = __import__('6-generate_ngrams').generate_ngrams

"""
Test 4: N-grams should keep placeholders such as <URL>, <NUM>, <EMO>.
"""

tokens = ["visit", "<URL>", "for", "<NUM>", "<EMO>", "deals"]

ngrams = generate_ngrams(tokens, n=2)

print("Input tokens:", tokens)
print("Generated bigrams:", ngrams, end="")
