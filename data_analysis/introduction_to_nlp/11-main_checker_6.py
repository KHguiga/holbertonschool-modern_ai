#!/usr/bin/env python3

import pandas as pd

clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens
compute_tfidf = __import__('11-tf_idf').tf_idf

df_raw = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])
sample = df_raw.sample(50, random_state=1)

corpus = []
for msg in sample["message"]:
    toks = filter_tokens(remove_stopwords(tokenize_text(clean_text(msg))))
    corpus.append(toks)

df, vocab = compute_tfidf(corpus, max_features=150)

print("Vocabulary size:", len(vocab))
print("Shape:", df.shape)
print("First 20 vocab:", vocab[:20])
print(df.head(), end="")
