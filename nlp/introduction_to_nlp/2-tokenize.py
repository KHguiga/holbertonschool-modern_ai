#!/usr/bin/env python3
"""
    Task 2
"""
import nltk
nltk.download("punkt_tab", quiet=True)


def tokenize_text(text, method="tweet"):
    """
    Tokenize SMS text.

    Options:
      - 'tweet' : TweetTokenizer (handles emojis, repeated punctuation, slang)
      - 'word'  : nltk.word_tokenize (standard NLTK tokenizer)
      - 'split' : simple whitespace split

    Returns:
        List of tokens
    """
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
