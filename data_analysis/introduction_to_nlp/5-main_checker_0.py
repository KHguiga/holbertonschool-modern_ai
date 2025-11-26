#!/usr/bin/env python3
normalize_tokens = __import__('5-normalize_tokens').normalize_tokens

"""
Test: Lemmatization should convert plural nouns and verb tenses to base form.
"""

tokens = ["running", "cars", "better", "went"]

lemmatized = normalize_tokens(tokens, method="lemmatize")

print("Input :", tokens)
print("Lemma :", lemmatized, end="")
