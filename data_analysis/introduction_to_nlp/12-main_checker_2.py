#!/usr/bin/env python3

train_word2vec = __import__('12-word2vec').train_word2vec

corpus = [
    ["win", "money", "now"],
    ["free", "offer", "claim", "now"],
]

# CBOW
cbow_model = train_word2vec(corpus, sg=0)
print("CBOW vector for 'free':", cbow_model.wv['free'][:5])

# Skip-gram
sg_model = train_word2vec(corpus, sg=1)
print("Skip-gram vector for 'free':", sg_model.wv['free'][:5], end="")
