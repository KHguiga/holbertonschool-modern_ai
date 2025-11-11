#!/usr/bin/env python3
import re
import html
import unicodedata
"""
    Task 1
"""


def normalize_unicode_punct(text):
    """Replace curly quotes, dashes, ellipses, etc. with ASCII equivalents."""
    replacements = {
        r"[‘’‚‛]": "'",      # single quotes
        r"[“”„‟]": '"',      # double quotes
        r"[‐-‒–—―]": "-",    # hyphens and dashes
        r"…": "...",         # ellipsis
    }
    for pattern, repl in replacements.items():
        text = re.sub(pattern, repl, text)
    return text


def replace_emoji(text, replace="<EMO>"):
    """Replace all emoji characters in text with the given placeholder."""
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002700-\U000027BF"  # dingbats
        "\U0001F900-\U0001F9FF"  # supplemental symbols & pictographs
        "\U00002600-\U000026FF"  # misc symbols
        "\U00002B00-\U00002BFF"  # arrows etc.
        "]", flags=re.UNICODE
    )
    return emoji_pattern.sub(replace, text)


def clean_text(text, replace_num=True, replace_url=True, keep_emoji=True):
    """
    Clean raw SMS text.
    - Lowercase, strip whitespace.
    - Replace URLs and numbers with placeholders.
    - Normalize unicode characters.
    - Replace emojis with <EMO> if keep_emoji=True.
    """
    if text is None:
        return ""
    # Basic normalization
    text = str(text).lower().strip()
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text)

    # Normalize Unicode punctuation to ASCII
    text = normalize_unicode_punct(text)

    # Replace URLs and numbers
    if replace_url:
        text = re.sub(r'https?://\S+|www\.\S+', '<URL>', text)
    if replace_num:
        text = re.sub(r'\b\d+\b', '<NUM>', text)

    # Replace emojis with <EMO> placeholder
    if keep_emoji:
        text = replace_emoji(text, replace="<EMO>")
    else:
        text = replace_emoji(text, replace="")

    # Collapse repeated punctuation (e.g., !!! → !)
    text = re.sub(r'([!?])\1+', r'\1', text)

    return text
