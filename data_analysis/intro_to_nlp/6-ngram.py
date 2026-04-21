#!/usr/bin/env python3
"""
    Task 6 — N-gram Generation
"""
import nltk


def generate_ngrams(tokens, n=2):
    if not isinstance(tokens, list) or len(tokens) < n:
        return []

    return ["_".join(ng) for ng in nltk.ngrams(tokens, n)]
