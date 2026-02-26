#!/usr/bin/env python3
"""
Task 8 — WordCloud Generation
"""

import wordcloud
import matplotlib.pyplot as plt


def generate_wordcloud(corpus_tokens, max_words=200, label=None):
    """
    Generate and display a word cloud from a list of token lists.

    Args:
        corpus_tokens (list[list[str]]): Tokenized documents.
        max_words (int): Maximum number of words to include in the wordcloud.
        label (str or None): Optional label to display as title
                             (e.g., 'spam', 'ham').

    Returns:
        WordCloud object
    """

    # Flatten corpus from list of docsto one list of tokens
    all_tokens = [tok for doc in corpus_tokens for tok in doc]

    # Join into text since WordCloud expects string
    text = " ".join(all_tokens)

    # Create wordcloud
    wc = wordcloud.WordCloud(
        max_words=max_words,
        background_color="white",
        width=800,
        height=400,
        random_state=42
    ).generate(text)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")

    plt.title(f"WordCloud {label}" if label else "WordCloud")

    plt.tight_layout()
    plt.show()
