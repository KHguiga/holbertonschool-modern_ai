#!/usr/bin/env python3
filter_tokens = __import__('4-filter_tokens').filter_tokens

"""
Test that tokens shorter than 2 characters are removed,
except placeholders like <NUM>, <EMO>, <URL>.
"""
tokens = ['a', 'i', 'ok', '<NUM>', 'be', 'go', 'u']
filtered = filter_tokens(tokens)

print("Input tokens :", tokens)
print("Filtered     :", filtered)
# Expected: ['ok', '<NUM>', 'be', 'go']
