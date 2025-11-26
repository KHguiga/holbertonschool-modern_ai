#!/usr/bin/env python3
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords

"""
Tests that stopword removal works regardless of token casing.
"""
tokens = ["This", "IS", "An", "Example"]
filtered = remove_stopwords(tokens)

print("Input :", tokens)
print("Output:", filtered, end="")
