#!/usr/bin/env python3

train_word2vec = __import__('12-word2vec').train_word2vec

corpus = [
    ["spam", "spam", "offer", "spam"],
    ["ham", "hello", "ham", "meeting"],
]

model = train_word2vec(corpus, min_count=1, vector_size=20,
                       window=1, epochs=30)

print("Vocabulary:", list(model.wv.key_to_index.keys()))
print("Vector shape for 'spam':", model.wv['spam'].shape, end="")
