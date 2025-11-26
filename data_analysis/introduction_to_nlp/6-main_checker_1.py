#!/usr/bin/env python3
generate_ngrams = __import__('6-generate_ngrams').generate_ngrams

"""
Test 2: Trigram generation.
"""

tokens = ["this", "is", "very", "important"]

ngrams = generate_ngrams(tokens, n=3)

print("Input tokens:", tokens)
print("Generated trigrams:", ngrams, end="")
