#!/usr/bin/env python3

generate_bow = __import__('10-bow').bag_of_words

corpus = [
    ["win", "money", "now"],
    ["win", "money"],
]

# FIX: explicitly set valid parameters for tiny corpus
df, vocab = generate_bow(
    corpus,
    ngram_range=(1, 2),
    min_df=1,     # token must appear in >= 1 document
    max_df=1.0    # allow tokens appearing in all documents
)

# Write output to file instead of printing
with open('2-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write("DataFrame shape: " + str(df.shape) + "\n")
    f.write(str(df))
