#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf


def to_lowercase(text):
    return text.lower()


corpus = [
    ["WIN", "MONEY", "NOW"],
    ["Win", "Prize", "Now"]
]

df, vocab = compute_tfidf(
    corpus,
    min_df=1,      # appear in at least 1 document
    max_df=1.0,    # appear in at most all documents
    ngram_range=(1, 1)
)
print("Vocabulary:", vocab)
print(df, end="")
