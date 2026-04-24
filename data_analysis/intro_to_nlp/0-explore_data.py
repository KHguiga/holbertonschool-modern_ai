#!/usr/bin/env python3
"""
    Task 0 — Basic Exploration
"""
import matplotlib.pyplot as plt
import seaborn as sns


def explore_data(df):
    """
    initial exploration of the SMSSpamCollection dataset.

    Args:
        df : pd.DataFrame with columns ['label', 'message']

    Plot 1. Bar chart — ham vs spam message counts
    Plot 2. Histogram — raw message length distribution
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # --- subplot 1: class counts ---
    counts = df['label'].value_counts()
    sns.barplot(x=counts.index, y=counts.values, ax=ax1)
    ax1.set_title("Ham vs Spam Counts")
    ax1.set_xlabel("label")
    ax1.set_ylabel("count")

    # --- subplot 2: raw message length histogram ---
    lengths = df['message'].str.len()
    sns.histplot(lengths, bins=50, kde=False, ax=ax2)
    ax2.set_title("Histogram of Raw Message Lengths")
    ax2.set_xlabel("length")
    ax2.set_ylabel("count")

    plt.tight_layout()
    plt.show()
