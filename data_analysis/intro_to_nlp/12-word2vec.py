#!/usr/bin/env python3
"""
    Task 12 — Word2Vec Embeddings
"""
import numpy as np
import gensim.models


def word2vec_embeddings(corpus_tokens, vector_size=50, window=5,
                        min_count=2, sg=0, epochs=10, workers=4):
    """
    Train Word2Vec and return per-message embeddings.

    Args:
        corpus_tokens : list of token lists
        vector_size   : dimensionality of the word vectors
        window        : context window size
        min_count     : ignore tokens appearing fewer than min_count times
        sg            : 0 = CBOW (default), 1 = Skip-gram
        epochs        : training passes over the corpus
        workers       : parallel training threads

    Returns:
        X     : np.ndarray of shape (n_messages, vector_size),
                computed as the mean of its in-vocab token vectors.
                Messages with no in-vocab tokens get a zero vector.
        model : trained Word2Vec model
    """
    model = gensim.models.Word2Vec(
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
        vecs = [model.wv[t] for t in tokens if t in model.wv]
        if vecs:
            X[i] = np.mean(vecs, axis=0)

    return X, model
