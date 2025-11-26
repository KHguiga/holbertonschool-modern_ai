#!/usr/bin/env python3
normalize_tokens = __import__('5-normalize_tokens').normalize_tokens

"""
Test: Stemming should reduce words aggressively.
"""

tokens = ["running", "happiness", "studies", "worked"]

stemmed = normalize_tokens(tokens, method="stem")

print("Input :", tokens)
print("Stem  :", stemmed, end="")
