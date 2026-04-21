#!/usr/bin/env python3
"""
    Task 13 — FastText Embeddings
"""
import numpy as np
import gensim.models


def fasttext_embeddings(corpus_tokens, vector_size=50, window=5,
                        min_count=1, sg=0, epochs=10, workers=4):
    """
    Train FastText and return per-message embeddings.

    Args:
        corpus_tokens : list of token lists
        vector_size   : dimensionality of the word vectors
        window        : context window size
        min_count     : minimum token frequency (1 = keep all tokens)
        sg            : 0 = CBOW (default), 1 = Skip-gram
        epochs        : training passes over the corpus
        workers       : parallel training threads

    Returns:
        X     : np.ndarray of shape (n_messages, vector_size),
                computed as the mean of its token vectors.
                All tokens have vectors; no zero-vector messages.
        model : trained FastText model
    """
    model = gensim.models.FastText(
        sentences=corpus_tokens,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg,
        epochs=epochs,
        workers=workers,
    )

    X = np.zeros((len(corpus_tokens), vector_size))
    for i, tokens in enumerate(corpus_tokens):
        if tokens:
            X[i] = np.mean([model.wv[t] for t in tokens], axis=0)

    return X, model
