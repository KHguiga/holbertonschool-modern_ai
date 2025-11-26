#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf

corpus = [
    ["win", "money", "now"],
    ["win", "prize", "now"],
    ["call", "now", "urgent"],
]

df, vocab = compute_tfidf(
    corpus,
    min_df=2,   # token must appear in ≥2 messages
    max_df=0.9  # not in >90% of messages
)

print("Vocabulary after pruning:", vocab)
print("Shape:", df.shape)
print(df, end="")
