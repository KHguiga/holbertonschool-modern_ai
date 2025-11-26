#!/usr/bin/env python3
"""
Task 6 — NGram
"""


def generate_ngrams(tokens, n=2):
    """
    Generate n-grams from a list of tokens.
    Each n-gram is returned as a string joined with '_'.

    Example:
        tokens = ["free", "entry", "now"]
        n=2 → ["free_entry", "entry_now"]
    """
    if not isinstance(tokens, list):
        return []

    if len(tokens) < n:
        return []

    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = "_".join(tokens[i:i + n])
        ngrams.append(ngram)

    return ngrams
