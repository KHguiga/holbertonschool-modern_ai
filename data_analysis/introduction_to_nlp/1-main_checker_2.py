clean_text = __import__('1-clean_text').clean_text

"""
Tests emoji replacement with keep_emoji=True and removal when False.
"""
if __name__ == "__main__":
    text = "Yay 😂🔥!"

    keep = clean_text(text, keep_emoji=True)
    remove = clean_text(text, keep_emoji=False)

    print("Input :", repr(text))
    print("With keep_emoji=True :", repr(keep))
    print("With keep_emoji=False:", repr(remove))
