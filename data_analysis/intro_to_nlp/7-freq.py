#!/usr/bin/env python3
"""
    Task 7 — Word Frequency Distribution
"""
import nltk
import matplotlib.pyplot as plt


def plot_top_n_frequencies(corpus_tokens, n=20):
    """
    Compute and display bar chart of top-n most frequent
    tokens across preprocessed corpus.

    Args:
        corpus_tokens: List of token lists — one per message.
        n: nbr of top words to display.

    Returns:
        nltk.FreqDist : frequency distribution of all corpus tokens .
    """
    # Flatten corpus into a single token list
    all_tokens = [tok for doc in corpus_tokens for tok in doc]

    fd = nltk.FreqDist(all_tokens)
    top = fd.most_common(n)

    words = [w for w, _ in top]
    counts = [c for _, c in top]

    plt.figure(figsize=(12, 5))
    plt.bar(words, counts)
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top {n} Most Frequent Words")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    return fd
