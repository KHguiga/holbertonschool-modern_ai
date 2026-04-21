#!/usr/bin/env python3
"""
    Task 11 — TF-IDF
"""
import sklearn.feature_extraction.text


def tf_idf(corpus_tokens, max_features=5000, ngram_range=(1, 2),
           min_df=2, max_df=0.95, norm='l2'):
    """
    Build a TF-IDF feature matrix from a list of token lists.

    Args:
        corpus_tokens : list of token lists
        max_features  : max vocab size
        ngram_range   : (min_n, max_n) — (1,2) captures unigrams + bigrams
        min_df        : remove terms appearing in < min_df docs
        max_df        : remove terms appearing in > max_df docs
        norm          : normalize row — 'l2' (default) or 'l1'

    Returns:
        X          : TF-IDF feature matrx (n_samples, n_features)
        vectorizer : fitted TfidfVectorizer object
    """
    docs = [" ".join(doc) for doc in corpus_tokens]

    vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(
        tokenizer=str.split,
        lowercase=False,
        token_pattern=None,
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=min_df,
        max_df=max_df,
        norm=norm,
    )

    X = vectorizer.fit_transform(docs)
    return X, vectorizer
