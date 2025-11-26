#!/usr/bin/env python3
train_fasttext = __import__('13-fasttext').train_fasttext

corpus = [
    ["win", "money", "now"],
    ["free", "offer", "claim", "now"],
    ["call", "me", "now"],
    ["click", "link", "offer"]
]

cbow = train_fasttext(corpus, sg=0, vector_size=30, epochs=30, workers=1)
sg = train_fasttext(corpus, sg=1, vector_size=30, epochs=30, workers=1)

print("CBOW vector (first 5) for 'offer':", cbow.wv['offer'][:5])
print("SG  vector (first 5) for 'offer':", sg.wv['offer'][:5])
print("CBOW most-similar to 'offer':", cbow.wv.most_similar('offer', topn=3))
print("SG  most-similar to 'offer':",
      sg.wv.most_similar('offer', topn=3), end="")
