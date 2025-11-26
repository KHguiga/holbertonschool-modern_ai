#!/usr/bin/env python3
normalize_tokens = __import__('5-normalize_tokens').normalize_tokens

"""
Test: Lemmatization must NOT alter placeholders.
"""

tokens = ["<EMO>", "<NUM>", "<URL>", "calls", "messages"]

lemmatized = normalize_tokens(tokens, method="lemmatize")

print("Input :", tokens)
print("Output:", lemmatized, end="")
