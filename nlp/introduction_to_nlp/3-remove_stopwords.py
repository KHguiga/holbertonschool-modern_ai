#!/usr/bin/env python3
"""
    Task 3
"""
import nltk

# Ensure stopwords are downloaded (students should know this)
nltk.download('stopwords', quiet=True)


def remove_stopwords(tokens, language="english", extra_words=None,
                     keep_words=None):
    """
    Remove stopwords from a list of tokens.

    Args:
        tokens (list): List of tokens.
        language (str): Stopword language (default 'english').
        extra_words (set): Optional words to also remove.
        keep_words (set): Optional words to keep even if in stopwords.

    Returns:
        list: Tokens after stopword removal.
    """
    if not isinstance(tokens, list):
        return []

    stop_words = set(nltk.corpus.stopwords.words(language))

    # Add or remove specific words depending on dataset characteristics
    if extra_words:
        stop_words |= set(extra_words)
    if keep_words:
        stop_words -= set(keep_words)

    filtered = [t for t in tokens if t.lower() not in stop_words]
    return filtered
