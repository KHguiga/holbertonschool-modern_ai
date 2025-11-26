#!/usr/bin/env python3
tokenize_text = __import__('2-tokenize').tokenize_text

"""
Tests basic tokenization on simple text.
"""
text = "hello world this is a test"
tokens = tokenize_text(text, method="split")
print(repr(tokens), end="")
