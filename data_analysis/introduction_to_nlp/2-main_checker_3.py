#!/usr/bin/env python3
tokenize_text = __import__('2-tokenize').tokenize_text

"""
Tests invalid tokenizer method handling.
"""
try:
    tokenize_text("hello", method="invalid")
except ValueError as e:
    print(str(e), end="")
