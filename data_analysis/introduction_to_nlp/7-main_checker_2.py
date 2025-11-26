#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import nltk

# Import student's function (expects file 7-freq.py)
plot_top_n_frequencies = __import__('7-freq').plot_top_n_frequencies


# ----------------------------
# Test corpus
# ----------------------------
corpus = [["spam", "ham", "spam", "offer", "spam", "ham"]]
N = 5


# ----------------------------
# Run student's plot and save
# ----------------------------
plt.ion()
fd_student = plot_top_n_frequencies(corpus, n=N)
plt.savefig("student.png")
plt.close()


# ----------------------------
# Reference Implementation
# ----------------------------
def generate_reference_plot(corpus_tokens, n=20):
    # Flatten tokens
    all_tokens = [tok for doc in corpus_tokens for tok in doc]

    # Frequency distribution
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

    return fd


# ----------------------------
# Generate reference plot and save
# ----------------------------
fd_reference = generate_reference_plot(corpus, n=N)
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
