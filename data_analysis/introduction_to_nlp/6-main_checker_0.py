#!/usr/bin/env python3
generate_ngrams = __import__('6-generate_ngrams').generate_ngrams

"""
Test 1: Basic bigram generation.
"""

tokens = ["free", "entry", "now"]

ngrams = generate_ngrams(tokens, n=2)

print("Input tokens:", tokens)
print("Generated bigrams:", ngrams, end="")
