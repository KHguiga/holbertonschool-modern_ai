#!/usr/bin/env python3
"""
    Task 4 — Token Filtering
"""
import re


# GIVEN — matches pipeline placeholders (<NUM>, <URL>, <EMO>, <TIME>, <EMAIL>).
# Case-insensitive to cover both uppercase-inserted and lowercase-remapped tags.
# Deliberately strict — <3, </3, <word do NOT match.
_PLACEHOLDER_RE = re.compile(r'^<[A-Za-z]+>$')


# STUDENT IMPLEMENTS
def filter_tokens(tokens, min_len=2, strip_hashtag=False):
    if not tokens:
        return []

    filtered = []
    for t in tokens:
        if _PLACEHOLDER_RE.match(t):
            filtered.append(t)
            continue

        if strip_hashtag and t.startswith("#"):
            t = t[1:]

        if len(t) < min_len:
            continue

        if not re.search(r"[a-zA-Z]", t):
            continue

        filtered.append(t)

    return filtered
