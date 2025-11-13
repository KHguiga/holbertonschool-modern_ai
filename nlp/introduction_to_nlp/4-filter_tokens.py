#!/usr/bin/env python3
"""
Task 4 — Filtering
Low info token removal (assumes prior cleaning and stopword removal)
"""
import re


def filter_tokens(tokens, min_len=2):
    """
    Remove low-information tokens from a token list.

    Responsibilities:
      - Remove tokens shorter than `min_len`
      - Remove tokens without alphabetic characters (except placeholders)
    """
    if not tokens:
        return []

    filtered = []
    for t in tokens:
        t_lower = t.lower()

        # Keep placeholders starting with '<'
        if t_lower.startswith("<"):
            filtered.append(t)
            continue

        # Remove short tokens
        if len(t_lower) < min_len:
            continue

        # Remove tokens without alphabetic characters
        if not re.search(r"[a-zA-Z]", t_lower):
            continue

        filtered.append(t)

    return filtered
