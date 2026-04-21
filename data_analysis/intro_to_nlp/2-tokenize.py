#!/usr/bin/env python3
"""
    Task 2 — Tokenization
"""
import nltk


EMOTICON_MAP = {
    "<3":   "<EMO>",
    "</3":  "<EMO>",
    ":)":   "<EMO>",
    ":-)":  "<EMO>",
    ":(":   "<EMO>",
    ":-(":  "<EMO>",
    ":d":   "<EMO>",
    ";)":   "<EMO>",
    ":|":   "<EMO>",
    ">:(":  "<EMO>",
    ":p":   "<EMO>",
    "b)":   "<EMO>",
    "o:)":  "<EMO>",
}


def normalize_emoticons(tokens, emoticon_action="replace"):
    """
    Replace or remove text emoticons isolated as single tokens by TweetTokenizer.
    Must run immediately after tokenize_text().

    Args:
        tokens          : list of tokens
        emoticon_action : "replace" → <EMO> | "remove" → drop | "keep" → untouched
    """
    if not isinstance(tokens, list):
        return []
    if emoticon_action == "keep":
        return tokens
    result = []
    for t in tokens:
        mapped = EMOTICON_MAP.get(t.lower())
        if mapped:
            if emoticon_action == "replace":
                result.append(mapped)
        else:
            result.append(t)
    return result


def tokenize_text(text, method="tweet"):
    if not isinstance(text, str):
        return []

    if method == "tweet":
        tokenizer = nltk.tokenize.TweetTokenizer(strip_handles=False,
                                                 reduce_len=True)
        return tokenizer.tokenize(text)
    elif method == "word":
        return nltk.tokenize.word_tokenize(text)
    elif method == "split":
        return text.split()
    else:
        raise ValueError("Invalid tokenizer method")
