#!/usr/bin/env python3
"""
Task 7 — word frequency
"""

import nltk
import matplotlib.pyplot as plt


def plot_top_n_frequencies(corpus_tokens, n=20):
    """
    Computes top-n most frequent words across the entire corpus
    and displays a bar chart.

    corpus_tokens: list of lists of tokens
                   e.g. [["hi","there"], ["hi","friend"]]

    n: number of top frequent words to show

    Returns:
        FreqDist object
    """
    # Flatten corpus into one list
    all_tokens = [tok for doc in corpus_tokens for tok in doc]

    # Compute frequencies
    fd = nltk.FreqDist(all_tokens)
    top = fd.most_common(n)

    # Plot
    words = [w for w, _ in top]
    counts = [c for _, c in top]

    plt.figure(figsize=(12, 5))
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.title(f"Top {n} Most Frequent Words")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    return fd
