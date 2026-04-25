#!/usr/bin/env python3
"""
    Task 8 — WordCloud
"""
import wordcloud
import matplotlib.pyplot as plt


def generate_wordcloud(corpus_tokens, max_words=200, label=None):
    """
    generate and display wordcloud from preprocessed token corpus.

    Args:
        corpus_tokens:List of token lists.
        max_words: max nbr of words to include.
        label: title suffix(e.g. 'SPAM','HAM', ...).

    Returns the fitted WordCloud object.
    """
    # Flatten corpus from list of token lists to one token list
    all_tokens = [tok for doc in corpus_tokens for tok in doc]

    # WordCloud expects a plain string
    text = " ".join(all_tokens)

    wc = wordcloud.WordCloud(
        max_words=max_words,
        background_color="white",
        width=800,
        height=400,
        random_state=42,
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"WordCloud {label}" if label else "WordCloud")
    plt.tight_layout()
    plt.show()

    return wc
