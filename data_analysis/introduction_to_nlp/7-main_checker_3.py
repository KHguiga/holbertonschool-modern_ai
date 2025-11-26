#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import nltk

# Import required student functions
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
filter_tokens = __import__('4-filter_tokens').filter_tokens
plot_top_n_frequencies = __import__('7-freq').plot_top_n_frequencies


# ----------------------------
# Load dataset and build corpus
# ----------------------------
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])

sample = df.sample(40, random_state=0)

corpus_tokens = []
for msg in sample["message"]:
    cleaned = clean_text(msg)
    tokens = tokenize_text(cleaned)
    tokens = filter_tokens(tokens)
    corpus_tokens.append(tokens)

N = 10


# ----------------------------
# Run student's plot and save
# ----------------------------
plt.ion()
fd_student = plot_top_n_frequencies(corpus_tokens, n=N)
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
fd_reference = generate_reference_plot(corpus_tokens, n=N)
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


# ----------------------------
# Required printed output
# ----------------------------
print(fd_reference.most_common(5), end="")
