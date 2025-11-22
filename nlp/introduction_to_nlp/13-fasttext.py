#!/usr/bin/env python3
"""
Task 13 — FastText training (gensim)
"""
import gensim


def train_fasttext(
    corpus_tokens,
    vector_size=100,
    window=5,
    min_count=1,
    sg=1,
    epochs=10,
    workers=1
):
    """
    Train a FastText model from a tokenized corpus.

    Args:
        corpus_tokens (list[list[str]]): tokenized documents
        vector_size (int): embedding dimension
        window (int): context window
        min_count (int): ignore words with lower freq
        sg (int): 1 = skip-gram (recommended), 0 = cbow
        epochs (int): number of training epochs
        workers (int): number of worker threads for training

    Returns:
        gensim.models.FastText: trained model
    """
    # gensim FastText can be given sentences directly
    model = gensim.models.FastText(
        sentences=corpus_tokens,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg,
        workers=workers,
        epochs=epochs
    )

    return model
