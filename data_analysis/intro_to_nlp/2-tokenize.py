#!/usr/bin/env python3
"""
    Task 2 — Tokenisation
"""
import nltk


# STUDENT IMPLEMENTS
def tokenize_text(text, method="tweet"):
    if not isinstance(text, str):
        return []

    if method == "tweet":
        tokenizer = nltk.tokenize.TweetTokenizer(strip_handles=True,
                                                 reduce_len=True)
        return tokenizer.tokenize(text)
    elif method == "word":
        return nltk.tokenize.word_tokenize(text)
    elif method == "split":
        return text.split()
    else:
        raise ValueError("Invalid tokenizer method")
