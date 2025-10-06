#!/usr/bin/env python3
"""
    Task 0
"""
import matplotlib.pyplot as plt
import seaborn as sns


def explore_data(df):
    """
    df: pd.DataFrame with columns ['label', 'message']
    - plots count ham vs spam (bar chart)
    - plots histogram of raw message lengths
    - returns None
    """
    # Create a figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    # First subplot: Ham vs Spam counts
    counts = df['label'].value_counts()
    sns.barplot(x=counts.index, y=counts.values, ax=ax1)
    ax1.set_title("Ham vs Spam Counts")
    ax1.set_xlabel("label")
    ax1.set_ylabel("count")
    # Second subplot: Histogram of message lengths
    lengths = df['message'].str.len()
    sns.histplot(lengths, bins=50, kde=False, ax=ax2)
    ax2.set_title("Histogram of Raw Message Lengths")
    ax2.set_xlabel("length")
    ax2.set_ylabel("count")
    plt.tight_layout()
    plt.show()
