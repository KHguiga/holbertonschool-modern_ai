#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf


def lowercase_tokenizer(text):
    return [t.lower() for t in text.split()]


corpus = [
    ["Win", "money"],
    ["money", "win"],
]

df, vocab = compute_tfidf(
    corpus,
    tokenizer_fn=lowercase_tokenizer,
    min_df=1,
    max_df=1.0
)
print("Vocabulary:", vocab)
print(df, end="")
