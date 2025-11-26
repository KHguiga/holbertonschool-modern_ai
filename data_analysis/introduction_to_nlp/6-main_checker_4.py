#!/usr/bin/env python3

clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens
generate_ngrams = __import__('6-generate_ngrams').generate_ngrams

"""
Test 5: Full pipeline integration test with n-grams.
"""

msg = "WIN £1000 NOW!!! Visit www.freecash.com 😍🔥"

# Step 1: clean
cleaned = clean_text(msg)

# Step 2: tokenize
tokens = tokenize_text(cleaned)

# Step 3: remove stopwords
tokens = remove_stopwords(tokens)

# Step 4: filter
tokens = filter_tokens(tokens)

# Step 5: generate bigrams
bigrams = generate_ngrams(tokens, n=2)

print("RAW    :", msg)
print("BIGRAMS:", bigrams, end="")
