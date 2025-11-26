#!/usr/bin/env python3

generate_bow = __import__('10-bow').bag_of_words

corpus = [
    ["a", "b", "a"],
    ["b", "c"],
    ["a", "c", "d"]
]

df, vocab = generate_bow(corpus, binary=True)

# Write output to file instead of printing
with open('1-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write("DataFrame shape: " + str(df.shape) + "\n")
    f.write(str(df))
