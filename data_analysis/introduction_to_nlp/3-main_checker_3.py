#!/usr/bin/env python3
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords

"""
Tests keeping certain stopwords that normally would be removed.
"""
tokens = ["not", "good", "at", "all"]
filtered = remove_stopwords(tokens, keep_words={"not"})

print("Input :", tokens)
print("Output:", filtered, end="")
