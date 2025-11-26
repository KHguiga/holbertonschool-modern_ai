#!/usr/bin/env python3
filter_tokens = __import__('4-filter_tokens').filter_tokens

"""
Mixed case: short tokens, meaningful words, placeholders, non-alphabetic
"""
tokens = ['ok', 'i', '!', '<NUM>', 'be', 'go', 'money', '😊', '<EMO>']
filtered = filter_tokens(tokens)

print("Input tokens :", tokens)
print("Filtered     :", filtered)
# Expected: ['ok', '<NUM>', 'be', 'go', 'money', '<EMO>']
