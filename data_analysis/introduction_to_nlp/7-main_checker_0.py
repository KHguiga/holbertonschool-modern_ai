#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import nltk

# import student's function (expects file 7-freq.py)
plot_top_n_frequencies = __import__('7-freq').plot_top_n_frequencies


# ----------------------------
# Test corpus
# ----------------------------
corpus = [
    ["hello", "world", "hello"],
    ["test", "world", "hello"],
]

N = 3  # top-n to plot


# ----------------------------
# Run student's plotting function and save result
# ----------------------------
plt.ion()   # interactive mode avoids blocking
plot_top_n_frequencies(corpus, n=N)
plt.savefig("student.png")
plt.close()


# ----------------------------
# Reference Implementation
# ----------------------------
def generate_reference_plot(corpus_tokens, n=20):
    # Flatten corpus
    all_tokens = [tok for doc in corpus_tokens for tok in doc]

    # Compute FreqDist
    fd = nltk.FreqDist(all_tokens)
    top = fd.most_common(n)

    # Extract words & counts
    words = [w for w, _ in top]
    counts = [c for _, c in top]

    # Plot
    plt.figure(figsize=(12, 5))
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.title(f"Top {n} Most Frequent Words")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


# ----------------------------
# Generate reference plot and save
# ----------------------------
generate_reference_plot(corpus, n=N)
plt.savefig("reference.png")
plt.close()


# ----------------------------
# Pixel-wise comparison
# ----------------------------
student_plot = mpimg.imread("student.png")
reference_plot = mpimg.imread("reference.png")

if np.array_equal(student_plot, reference_plot):
    print("The plot matches the reference.")
else:
    print("The plot does not match the reference.")
