#!/usr/bin/env python3
filter_tokens = __import__('4-filter_tokens').filter_tokens

"""
Ensure placeholders like <NUM>, <EMO>, <URL> are never removed
even if they are short or non-alphabetic.
"""
tokens = ['<NUM>', '<EMO>', '<URL>', 'ok', 'a', '!', '12']
filtered = filter_tokens(tokens)

print("Input tokens :", tokens)
print("Filtered     :", filtered)
# Expected: ['<NUM>', '<EMO>', '<URL>', 'ok']
