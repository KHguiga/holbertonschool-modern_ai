#!/usr/bin/env python3
"""
    Task 1 — Text Cleaning
"""
import re
import emoji


_DATASET_PLACEHOLDER_MAP = {
    '<#>':       '<NUM>',
    '<decimal>': '<NUM>',
    '<time>':    '<TIME>',
    '<url>':     '<URL>',
    '<email>':   '<EMAIL>',
}


def normalize_unicode_punct(text):
    """Replace curly quotes, dashes, ellipses, etc. with ASCII equivalents."""
    replacements = {
        r"[''‚‛]":    "'",
        r"[""„‟]":    '"',
        r"[‐‑‒–—―−]": "-",
        r"…":          "...",
    }
    for pattern, repl in replacements.items():
        text = re.sub(pattern, repl, text)
    return text


def clean_text(text, replace_num=True,
               replace_url=True, emoji_action="replace"):
    """
    Args:
        text         : input string (already pre-cleaned)
        replace_num  : replace numbers with <NUM>
        replace_url  : replace URLs with <URL>
        emoji_action : "replace" → <EMO> | "remove" → drop | "keep" → untouched

    Pipeline:
        1. Lowercase + strip
        2. Remap dataset placeholders  (<#> → <NUM>, etc.)
        3. Unicode punctuation → ASCII
        4. URL replacement
        5. Number replacement
        6. Emoji handling
        7. Collapse repeated ! / ?
        8. Collapse whitespace
    """
    if text is None:
        return ""

    text = str(text).lower().strip()

    for src, dst in _DATASET_PLACEHOLDER_MAP.items():
        text = text.replace(src, dst)

    text = normalize_unicode_punct(text)

    if replace_url:
        text = re.sub(r'https?://\S+|www\.\S+', '<URL>', text)

    if replace_num:
        # pass 1 — phone-like strings (+447911123456, 0800-123-4567 …)
        text = re.sub(r'\+?\d[\d\s\-]{6,}\d', '<NUM>', text)
        # pass 2 — integers, decimals, currency-prefixed amounts
        # (?<!<) avoids matching the digit in emoticons like <3
        text = re.sub(r'(?:£|\$|€)\d+(?:[.,]\d+)*|(?<!<)\b\d+(?:[.,]\d+)*\b',
                      '<NUM>', text)

    if emoji_action == "replace":
        text = emoji.replace_emoji(text, replace="<EMO>")
    elif emoji_action == "remove":
        text = emoji.replace_emoji(text, replace=" ")

    text = re.sub(r'([!?])\1+', r'\1', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text
