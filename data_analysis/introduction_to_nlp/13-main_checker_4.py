#!/usr/bin/env python3
import pandas as pd

train_fasttext = __import__('13-fasttext').train_fasttext

# Preprocessing functions provided in the repo
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens
normalize_tokens = __import__('5-normalize_tokens').normalize_tokens

# Load SMS dataset (path must exist)
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])
sample = df.sample(200, random_state=0)  # use 200 for decent training speed


def preprocess(msg):
    t = clean_text(msg)
    t = tokenize_text(t)
    t = remove_stopwords(t)
    t = filter_tokens(t)
    t = normalize_tokens(t)
    return t


corpus = [preprocess(m) for m in sample['message']]

model = train_fasttext(corpus, vector_size=100, window=5,
                       min_count=2, epochs=50, workers=1)

print("Corpus docs:", len(corpus))
print("Vocab size:", len(model.wv.key_to_index))
print("Some words in vocab sample:", list(model.wv.key_to_index.keys())[:40])
# show similarities for a spam-like token if present
token = 'win'
if token in model.wv.key_to_index:
    print("Most similar to 'win':",
          model.wv.most_similar(token, topn=5), end="")
else:
    print(f"'{token}' not in vocab (min_count filtering).", end="")
