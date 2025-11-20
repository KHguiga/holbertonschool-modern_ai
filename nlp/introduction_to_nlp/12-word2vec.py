#!/usr/bin/env python3
"""
Task 11 — Word2Vec
"""

from gensim.models import Word2Vec


def train_word2vec(corpus_tokens, vector_size=100, window=5,
                   min_count=1, sg=1, epochs=50, save_path=None):
    """
    Train a Word2Vec model from a tokenized corpus.

    Args:
        corpus_tokens (list[list[str]]): Tokenized corpus
        vector_size (int): Embedding dimensionality
        window (int): Context window size
        min_count (int): Minimum frequency threshold
        sg (int): Skip-gram=1, CBOW=0
        epochs (int): Number of iterations
        save_path (str or None): If provided, save model to this path

    Returns:
        gensim.models.Word2Vec
    """

    model = Word2Vec(
        sentences=corpus_tokens,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg,
        epochs=epochs
    )

    if save_path:
        model.save(save_path)

    return model
