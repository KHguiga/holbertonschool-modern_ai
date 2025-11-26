#!/usr/bin/env python3
train_fasttext = __import__('13-fasttext').train_fasttext

corpus = [
    ["win", "money", "now"],
    ["free", "offer", "claim", "now"],
    ["limited", "time", "offer"]
]

model = train_fasttext(corpus, vector_size=40, window=3, epochs=40, workers=1)

# Word present in vocab
print("In-vocab 'offer' exists:", 'offer' in model.wv.key_to_index)
print("Vector (first 5 dims) for 'offer':", model.wv['offer'][:5])

# OOV word: not seen during training
oov_word = "winmoney"  # likely not in vocab
try:
    vec = model.wv[oov_word]
    print(f"Vector for OOV '{oov_word}' (first 5 dims):", vec[:5])
    print("Note: FastText returns a vector for OOV via subwords.", end="")
except KeyError:
    print(f"No vector available for '{oov_word}' (KeyError).", end="")
