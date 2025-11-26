#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf

corpus = [
    ["win", "money", "now"],
    ["free", "offer", "now"],
    ["urgent", "win", "call"],
    ["click", "claim", "now"],
]

df, vocab = compute_tfidf(corpus, max_features=5)

print("Vocabulary:", vocab)
print("Shape:", df.shape)
print(df, end="")
