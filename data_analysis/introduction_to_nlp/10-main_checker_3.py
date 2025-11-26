#!/usr/bin/env python3

generate_bow = __import__('10-bow').bag_of_words
corpus = [
    ["dog", "cat"],
    ["cat", "mouse"],
    ["dog", "dog"],
]

df, vocab = generate_bow(corpus, min_df=2, max_df=0.8)

# Write output to file instead of printing
with open('3-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write("DataFrame shape: " + str(df.shape) + "\n")
    f.write(str(df))
