#!/usr/bin/env python3
import pandas as pd

normalize_tokens = __import__('5-normalize_tokens').normalize_tokens
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens

"""
Test Task 5 on the real SMS Spam dataset.
Runs: clean → tokenize → stopwords → filter → normalize
"""

df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])

sample_msgs = df["message"].sample(20, random_state=60).tolist()

# Open file for writing
with open("lemmatized_output.txt", "w") as f:
    for i, msg in enumerate(sample_msgs):
        cleaned = clean_text(msg)
        tokens = tokenize_text(cleaned)
        no_stop = remove_stopwords(tokens)
        filtered = filter_tokens(no_stop)

        lemmatized = normalize_tokens(filtered, method="lemmatize")

        # Print to console (exactly as before)
        print("RAW :", msg)
        # Check if this is the last iteration
        if i == len(sample_msgs) - 1:
            print("LEMMATIZED :", lemmatized[:20], end="")
        else:
            print("LEMMATIZED :", lemmatized[:20])
        # Write the same output to file
        f.write(f"RAW : {msg}\n")
        if i == len(sample_msgs) - 1:
            f.write(f"LEMMATIZED : {lemmatized[:20]}")
        else:
            f.write(f"LEMMATIZED : {lemmatized[:20]}\n")
