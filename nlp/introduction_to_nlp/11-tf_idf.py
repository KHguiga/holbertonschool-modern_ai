#!/usr/bin/env python3
"""
Task 11 — TF-IDF Vectorization
"""
import sklearn
import pandas as pd


def tf_idf(
    corpus_tokens,
    max_features=5000,
    ngram_range=(1, 1),
    min_df=2,
    max_df=0.9,
    norm='l2',
    tokenizer_fn=None,
    preprocessor_fn=None
):
    """
    Compute TF-IDF matrix from a list of tokenized documents.

    Args:
        corpus_tokens (list[list[str]]): tokenized documents.
        max_features (int or None): maximum number of features to keep.
        ngram_range (tuple): n-gram range (e.g., (1,1), (1,2)).
        min_df (int or float): minimum document frequency.
        max_df (int or float): maximum document frequency.
        norm (str or None): normalization ('l1', 'l2', or None).
        tokenizer_fn (callable or None): optional tokenizer override.
        preprocessor_fn (callable or None): optional preprocessor override.

    Returns:
        df (DataFrame): TF-IDF feature matrix (sparse DataFrame).
        feature_names (list[str]): list of feature names.
    """

    # Join tokens because TfidfVectorizer works on strings
    docs = [" ".join(doc) for doc in corpus_tokens]

    # If no tokenizer is provided, split on whitespace
    tokenizer = tokenizer_fn if tokenizer_fn else (lambda x: x.split())

    # If no preprocessor, return text unchanged
    preprocessor = preprocessor_fn if preprocessor_fn else (lambda x: x)

    vect = sklearn.feature_extraction.text.TfidfVectorizer(
        tokenizer=tokenizer,
        preprocessor=preprocessor,
        token_pattern=None,       # required whenever tokenizer overrided
        ngram_range=ngram_range,
        max_features=max_features,
        min_df=min_df,
        max_df=max_df,
        norm=norm,
    )

    X = vect.fit_transform(docs)
    feature_names = vect.get_feature_names_out().tolist()

    df = pd.DataFrame.sparse.from_spmatrix(X, columns=feature_names)
    return df, feature_names
