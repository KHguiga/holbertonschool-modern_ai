#!/usr/bin/env python3
import pandas as pd

# Import the student's functions
filter_tokens = __import__('4-filter_tokens').filter_tokens
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords

"""
Filtering with stopword removal on the SMSSpamCollection dataset.
"""

# Load dataset
df = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])

df = df[df['label'] == 'spam'].iloc[-21:-10]
sample_msgs = df['message'].tolist()

for i, msg in enumerate(sample_msgs):
    # Step 1: Clean
    cleaned = clean_text(msg)
    # Step 2: Tokenize (TweetTokenizer)
    tokens = tokenize_text(cleaned)
    # Step 3: Remove stopwords
    tokens_no_stop = remove_stopwords(tokens)
    # Step 4: Filter low-information tokens
    filtered = filter_tokens(tokens_no_stop)
    print("RAW :", msg)
    if i == len(sample_msgs) - 1:
        print("FILTERED  :", filtered, end="")
    else:
        print("FILTERED  :", filtered)
