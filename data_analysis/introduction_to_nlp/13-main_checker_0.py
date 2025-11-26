#!/usr/bin/env python3
train_fasttext = __import__('13-fasttext').train_fasttext

corpus = [
    ["win", "money", "now"],
    ["hello", "how", "are", "you"],
    ["limited", "offer", "click", "here"]
]

model = train_fasttext(corpus, vector_size=50, window=2, epochs=30, workers=1)

print("Vocab size:", len(model.wv.key_to_index))
print("Vector size (for 'win'):", model.wv['win'].shape)
print("Most similar to 'win':", model.wv.most_similar('win', topn=3), end="")
