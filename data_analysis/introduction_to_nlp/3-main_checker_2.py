#!/usr/bin/env python3
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords

"""
Tests adding custom extra stopwords.
"""
tokens = ["hey", "there", "friend"]
filtered = remove_stopwords(tokens, extra_words={"hey", "friend"})

print("Input :", tokens)
print("Output:", filtered, end="")
