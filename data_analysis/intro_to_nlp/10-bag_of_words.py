#!/usr/bin/env python3
"""
    Task 10 — Bag of Words
"""
import sklearn.feature_extraction.text


def bag_of_words(corpus_tokens, max_features=5000, ngram_range=(1, 2),
                 min_df=2, max_df=0.95, binary=False):
    """
    Build a Bag-of-Words feature matrix from a list of token lists.

    Args:
        corpus_tokens : list of token lists
        max_features  : maximum vocabulary size
        ngram_range   : (min_n, max_n) — (1,2) captures unigrams + bigrams
        min_df        : ignore terms appearing in fewer than min_df documents
        max_df        : ignore terms appearing in more than max_df of documents
        binary        : if True, presence/absence instead of counts

    Returns:
        X          : sparse feature matrix (n_samples, n_features)
        vectorizer : fitted CountVectorizer object
    """
    # CountVect works on str
    docs = [" ".join(doc) for doc in corpus_tokens]

    vectorizer = sklearn.feature_extraction.text.CountVectorizer(
        tokenizer=str.split,
        lowercase=False,       # cz pipeline already lowercased
        token_pattern=None,    # needed when tokenizer overridden
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=min_df,
        max_df=max_df,
        binary=binary,
    )

    X = vectorizer.fit_transform(docs)
    return X, vectorizer
