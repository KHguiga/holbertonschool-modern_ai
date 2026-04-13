#!/usr/bin/env python3
"""
    Task 3 — Stopword Removal
"""
import nltk


# GIVEN
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

# GIVEN
def normalize_emoticons(tokens, emoticon_action="replace"):
    """
    Replace or remove text emoticons that survive tokenisation as single tokens.
    Runs after tokenize_text(), before remove_stopwords().

    Args:
        tokens          : list of tokens from tokenize_text()
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


# GIVEN — verified against SMSSpamCollection by frequency-ratio analysis.
# These words are in NLTK's English stopword list but appear significantly
# more often in spam than ham and must not be removed.
SPAM_KEEP_WORDS = {
    "won",    # 97x more in spam
    "our",    #  8x
    "from",   #  5x
    "or",     #  5x
    "now",    #  4x
    "your",   #  4x
    "only",   # ~4x
}


# STUDENT IMPLEMENTS
def remove_stopwords(tokens, language="english", extra_words=None,
                     keep_words=None):
    if not isinstance(tokens, list):
        return []

    stop_words = set(nltk.corpus.stopwords.words(language))

    if extra_words:
        stop_words |= set(extra_words)
    if keep_words:
        stop_words -= set(keep_words)

    return [t for t in tokens if t.lower() not in stop_words]
