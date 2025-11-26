#!/usr/bin/env python3
generate_ngrams = __import__('6-generate_ngrams').generate_ngrams

"""
Test 3: Return empty list when tokens < n.
"""

tokens = ["hello"]
ngrams = generate_ngrams(tokens, n=2)

print("Input tokens:", tokens)
print("Output", ngrams, end="")
