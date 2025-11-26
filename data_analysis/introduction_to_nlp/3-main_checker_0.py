#!/usr/bin/env python3
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords

"""
Tests that common English stopwords are removed.
"""
tokens = ["this", "is", "a", "simple", "test"]
filtered = remove_stopwords(tokens)

print("Input :", tokens)
print("Output:", filtered, end="")
