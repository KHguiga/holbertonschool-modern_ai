#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import wordcloud

# Import student's function (expects file 8-wordcloud.py)
generate_wordcloud = __import__('8-wordcloud').generate_wordcloud

# ----------------------------
# Sample dataset
# ----------------------------
data = {
    "label": ["spam", "ham", "spam", "ham"],
    "message": [
        "Win money now",
        "Hello, how are you?",
        "Limited offer, click here",
        "Are we still meeting today?"
    ]
}
df = pd.DataFrame(data)

# ----------------------------
# Preprocessing functions
# ----------------------------
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
filter_tokens = __import__('4-filter_tokens').filter_tokens

# ----------------------------
# Build tokenized corpus
# ----------------------------
corpus_all = [filter_tokens(tokenize_text(
    clean_text(msg))) for msg in df['message']]
corpus_spam = [filter_tokens(tokenize_text(
    clean_text(msg))) for msg in df[df['label'] == 'spam']['message']]
corpus_ham = [filter_tokens(tokenize_text(
    clean_text(msg))) for msg in df[df['label'] == 'ham']['message']]

# ----------------------------
# Test 1: Whole corpus
# ----------------------------
plt.ion()
generate_wordcloud(corpus_all)
plt.savefig("student_all.png")
plt.close()

# ----------------------------
# Test 2: Spam only
# ----------------------------
plt.ion()
generate_wordcloud(corpus_spam, label='spam')
plt.savefig("student_spam.png")
plt.close()

# ----------------------------
# Test 3: Ham only
# ----------------------------
plt.ion()
generate_wordcloud(corpus_ham, label='ham')
plt.savefig("student_ham.png")
plt.close()

# ----------------------------
# Reference Implementation
# ----------------------------


def reference_wordcloud(corpus_tokens, label=None):
    # Flatten corpus
    all_tokens = [tok for doc in corpus_tokens for tok in doc]
    text = " ".join(all_tokens)
    wc = wordcloud.WordCloud(width=800,
                             height=400,
                             max_words=200,
                             background_color="white",
                             random_state=42).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")

    plt.title(f"WordCloud {label}" if label else "WordCloud")

    plt.tight_layout()
    plt.show()

# ----------------------------
# Generate reference plots
# ----------------------------


plt.ion()
reference_wordcloud(corpus_all)
plt.savefig("reference_all.png")
plt.close()

plt.ion()
reference_wordcloud(corpus_spam, label='spam')
plt.savefig("reference_spam.png")
plt.close()

plt.ion()
reference_wordcloud(corpus_ham, label='ham')
plt.savefig("reference_ham.png")
plt.close()

# ----------------------------
# Pixel-wise comparison
# ----------------------------
for s, r in [("student_all.png", "reference_all.png"),
             ("student_spam.png", "reference_spam.png"),
             ("student_ham.png", "reference_ham.png")]:
    student_plot = mpimg.imread(s)
    reference_plot = mpimg.imread(r)
    if np.array_equal(student_plot, reference_plot):
        print(f"{s} matches reference.")
    else:
        print(f"{s} does not match reference.")
