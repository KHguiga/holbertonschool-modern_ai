#!/usr/bin/env python3
"""
Task 11 — Word2Vec
"""

import gensim


def train_word2vec(corpus_tokens, vector_size=100, window=5,
                   min_count=1, sg=1, epochs=50):
    """
    Train a Word2Vec model from a tokenized corpus.

    Args:
        corpus_tokens (list[list[str]]): Tokenized corpus
        vector_size (int): Embedding dimensionality
        window (int): Context window size
        min_count (int): Minimum frequency threshold
        sg (int): Skip-gram=1, CBOW=0
        epochs (int): Number of iterations

    Returns:
        gensim.models.Word2Vec
    """

    model = gensim.models.Word2Vec(
        sentences=corpus_tokens,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg,
        epochs=epochs
    )

    return model
