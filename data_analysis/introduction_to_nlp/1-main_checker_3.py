#!/usr/bin/env python3
clean_text = __import__('1-clean_text').clean_text

"""
Tests whether smart quotes, em-dashes, and repeated punctuation are normalized.
"""
if __name__ == "__main__":
    text = "You’ve won!!! — Amazing… right??"
    cleaned = clean_text(text)

    print("Input :", repr(text))
    print("Output:", repr(cleaned))
