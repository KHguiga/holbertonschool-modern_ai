#!/usr/bin/env python3
tokenize_text = __import__('2-tokenize').tokenize_text

"""
Tests TweetTokenizer handling of emojis and repeated punctuation.
"""
text = "OMG 😂😂!!! I'm sooo happppyyy!!!"
tokens = tokenize_text(text, method="tweet")
print(repr(tokens), end="")
