#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import wordcloud

# Import student's function (expects file 8-wordcloud.py)
generate_wordcloud = __import__('8-wordcloud').generate_wordcloud

# ----------------------------
# Load dataset
# ----------------------------
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])

# ----------------------------
# Preprocessing functions
# ----------------------------
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens

# ----------------------------
# Build tokenized corpus
# ----------------------------


def preprocess_messages(messages):
    corpus_tokens = []
    for msg in messages:
        tokens = tokenize_text(clean_text(msg))
        tokens = remove_stopwords(tokens)
        tokens = filter_tokens(tokens)
        corpus_tokens.append(tokens)
    return corpus_tokens


corpus_all = preprocess_messages(df['message'])
corpus_spam = preprocess_messages(df[df['label'] == 'spam']['message'])
corpus_ham = preprocess_messages(df[df['label'] == 'ham']['message'])

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
    all_tokens = [tok for doc in corpus_tokens for tok in doc]
    text = " ".join(all_tokens)
    wc = wordcloud.WordCloud(
        width=800,
        height=400,
        max_words=200,
        background_color="white",
        random_state=42
    ).generate(text)
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
