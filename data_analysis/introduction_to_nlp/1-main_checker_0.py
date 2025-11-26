clean_text = __import__('1-clean_text').clean_text

"""
Tests lowercasing, whitespace stripping, and HTML entity decoding.
"""
text = "   HeLLo &amp; WORLD!   "
cleaned = clean_text(text)

print(repr(cleaned))
