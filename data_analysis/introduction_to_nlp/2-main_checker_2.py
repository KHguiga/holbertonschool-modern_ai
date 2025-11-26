#!/usr/bin/env python3
tokenize_text = __import__('2-tokenize').tokenize_text

"""
Tests nltk.word_tokenize handling of punctuation and contractions.
"""
text = "Don't worry, I'll be there soon."
tokens = tokenize_text(text, method="word")
print(repr(tokens), end="")
