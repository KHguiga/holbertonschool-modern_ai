#!/usr/bin/env python3

import sklearn
import pandas as pd


def bag_of_words(corpus_tokens, max_features=5000, ngram_range=(1, 1),
                 min_df=2, max_df=0.9, binary=False):

    # Join tokens into whitespace-separated strings
    docs = [" ".join(doc) for doc in corpus_tokens]

    vect = sklearn.feature_extraction.text.CountVectorizer(
        tokenizer=lambda x: x.split(),
        preprocessor=lambda x: x,
        token_pattern=None,
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=min_df,
        max_df=max_df,
        binary=binary
    )

    X = vect.fit_transform(docs)
    vocab = vect.get_feature_names_out().tolist()
    df = pd.DataFrame.sparse.from_spmatrix(X, columns=vocab)
    return df, vocab
