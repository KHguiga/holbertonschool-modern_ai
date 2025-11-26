#!/usr/bin/env python3
"""
pipeline_no_num.py
- clean_text: replace_num=False (numbers left as tokens)
- tokenizer: tweet
- normalization: lemmatize
- bag_of_words: default
"""
import pandas as pd

clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens
normalize_tokens = __import__('5-normalize_tokens').normalize_tokens
bag_of_words = __import__('10-bow').bag_of_words


def build_corpus(messages):
    corpus = []
    for m in messages:
        cleaned = clean_text(m, replace_num=False,
                             replace_url=True, keep_emoji=True)
        toks = tokenize_text(cleaned, method="tweet")
        toks = remove_stopwords(toks)
        toks = filter_tokens(toks)
        toks = normalize_tokens(toks, method="lemmatize")
        corpus.append(toks)
    return corpus


df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])
corpus = build_corpus(df["message"])
print("Documents:", len(corpus))
X_df, vocab = bag_of_words(corpus)
print("BoW shape:", X_df.shape)
print("Vocabulary sample:", vocab[-30:])
print(X_df.iloc[:5, -10:])  # show first 5 docs x first 10 features
