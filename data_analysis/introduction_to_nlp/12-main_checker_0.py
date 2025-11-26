#!/usr/bin/env python3

train_word2vec = __import__('12-word2vec').train_word2vec

corpus = [
    ["win", "money", "now"],
    ["hello", "how", "are", "you"],
    ["limited", "offer", "click", "here"]
]

model = train_word2vec(corpus, vector_size=50, window=2, epochs=20)

# Inspect vector for a word
print("Vector for 'win':", model.wv['win'][:5])  # first 5 dims
print("Most similar to 'win':", model.wv.most_similar('win', topn=3), end="")
