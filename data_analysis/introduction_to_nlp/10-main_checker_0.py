#!/usr/bin/env python3

generate_bow = __import__('10-bow').bag_of_words

corpus = [
    ["hello", "world"],
    ["hello", "spam", "offer"],
    ["limited", "offer", "now"],
    ["world", "hello", "world"]
]

df, vocab = generate_bow(corpus)

# Write output to file instead of printing
with open('0-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write("DataFrame shape: " + str(df.shape) + "\n")
    f.write(str(df))
