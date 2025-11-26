#!/usr/bin/env python3
import pandas as pd
clean_text = __import__('1-clean_text').clean_text

"""
Tests whether smart quotes, em-dashes, and repeated punctuation are normalized.
"""
if __name__ == "__main__":
    df = pd.read_csv("SMSSpamCollection",
                     sep="\t", names=["label", "message"], header=None)

    sample = df.sample(100, random_state=42)
    for _, row in sample.iterrows():
        cleaned = clean_text(row["message"])
        print(f"Cleaned: {cleaned}")
