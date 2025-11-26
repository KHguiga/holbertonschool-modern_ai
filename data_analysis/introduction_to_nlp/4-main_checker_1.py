#!/usr/bin/env python3
filter_tokens = __import__('4-filter_tokens').filter_tokens

"""
Test that tokens without alphabetic characters are removed,
placeholders like <NUM>, <EMO>, <URL> should remain.
"""
tokens = ['123', '!!!', '$$$', '<NUM>', '<EMO>', '<URL>', 'hello', 'world']
filtered = filter_tokens(tokens)

print("Input tokens :", tokens)
print("Filtered     :", filtered)
# Expected: ['<NUM>', '<EMO>', '<URL>', 'hello', 'world']
