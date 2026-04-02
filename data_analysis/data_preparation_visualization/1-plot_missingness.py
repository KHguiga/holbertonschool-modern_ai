#!/usr/bin/env python3
"""
Module for visualizing missing values in a DataFrame.
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Visualizes missing values in a DataFrame using a scatter plot.
    Args:
        df (pd.DataFrame): DataFrame to analyze.
    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    row_ind, col_ind = np.where(df.isnull())
    plt.scatter(
        row_ind,
        col_ind,
        marker='|',
        color='blue'
    )

    plt.title("Missingness Plot")
    plt.yticks(range(len(df.columns)), df.columns)
    plt.tight_layout()
    plt.show()
