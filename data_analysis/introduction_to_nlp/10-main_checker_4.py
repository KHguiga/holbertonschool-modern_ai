#!/usr/bin/env python3

generate_bow = __import__('10-bow').bag_of_words
corpus = [
    ["spam", "offer", "now"],
    ["click", "offer", "win"],
    ["win", "prize", "now"],
]

df, vocab = generate_bow(corpus, max_features=3)

# Write output to file instead of printing
with open('4-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write("DataFrame shape: " + str(df.shape) + "\n")
    f.write(str(df))
