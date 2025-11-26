#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf

corpus = [
    ["win", "money", "now"],
    ["call", "me", "later"],
    ["urgent", "offer", "click"],
    ["are", "you", "home"]
]

df, vocab = compute_tfidf(corpus, ngram_range=(1, 2), min_df=1, max_df=1.0)

print("Vocabulary size:", len(vocab))
print("Sample vocabulary:", vocab[:20])
print("Shape:", df.shape)
print(df, end="")
