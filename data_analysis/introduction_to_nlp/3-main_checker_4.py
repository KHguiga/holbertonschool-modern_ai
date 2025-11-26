#!/usr/bin/env python3
import pandas as pd
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords

"""
Tests on real SMS spam dataset to ensure function scales and behaves correctly.
"""
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])

df = df[df['label'] == 'spam'].iloc[-21:-10]
for msg in df["message"]:
    cleaned = clean_text(msg)
    tokens = tokenize_text(cleaned)
    filtered = remove_stopwords(tokens, keep_words={"won"})
    print("RAW :", msg)
    # print("Cleaned :", cleaned)
    # print("Tokens  :", tokens)
    print("Removed StopWords :", filtered)
