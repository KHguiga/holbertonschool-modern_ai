#!/usr/bin/env python3
"""
    Task 4 — Token Filtering
"""
import re

_PLACEHOLDER_RE = re.compile(r'^<[A-Za-z]+>$')


def filter_tokens(tokens, min_len=2, strip_hashtag=False):
    """
    Task 4 — Token Filtering
    """
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
