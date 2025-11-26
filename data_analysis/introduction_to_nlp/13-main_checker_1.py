#!/usr/bin/env python3
train_fasttext = __import__('13-fasttext').train_fasttext

corpus = [
    ["spam", "spam", "offer", "spam"],
    ["ham", "hello", "ham", "meeting"],
    ["spam", "offer", "free", "click", "offer"],
]

model = train_fasttext(corpus, vector_size=30, window=2, epochs=40, workers=1)

print("Vocab (sample):", list(model.wv.key_to_index.keys())[:20])
print("Vector shape for 'spam':", model.wv['spam'].shape)
print("Most similar to 'spam':", model.wv.most_similar('spam', topn=5), end="")
