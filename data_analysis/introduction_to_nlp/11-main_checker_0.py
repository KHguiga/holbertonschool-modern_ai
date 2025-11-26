#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf

corpus = [
    ["win", "money", "now"],
    ["free", "offer", "claim", "now"],
]

df, vocab = compute_tfidf(corpus, min_df=1, max_df=1.0)

with open('0-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write("Shape: " + str(df.shape) + "\n")
    f.write(str(df))

#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf

corpus = [
    ["win", "money", "now"],
    ["call", "me", "later"],
    ["urgent", "offer", "click"],
    ["are", "you", "home"]
]

df, vocab = compute_tfidf(corpus, ngram_range=(1, 2), min_df=1, max_df=1.0)

with open('1-output', 'w') as f:
    f.write("Vocabulary size: " + str(len(vocab)) + "\n")
    f.write("Sample vocabulary: " + str(vocab[:20]) + "\n")
    f.write("Shape: " + str(df.shape) + "\n")
    f.write(str(df))


#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf

corpus = [
    ["win", "money", "now"],
    ["win", "prize", "now"],
    ["call", "now", "urgent"],
]

df, vocab = compute_tfidf(
    corpus,
    min_df=2,   # token must appear in ≥2 messages
    max_df=0.9  # not in >90% of messages
)

with open('2-output', 'w') as f:
    f.write("Vocabulary after pruning: " + str(vocab) + "\n")
    f.write("Shape: " + str(df.shape) + "\n")
    f.write(str(df))


#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf

corpus = [
    ["win", "money", "now"],
    ["free", "offer", "now"],
    ["urgent", "win", "call"],
    ["click", "claim", "now"],
]

df, vocab = compute_tfidf(corpus, max_features=5)

with open('3-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write("Shape: " + str(df.shape) + "\n")
    f.write(str(df))


#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf


def to_lowercase(text):
    return text.lower()


corpus = [
    ["WIN", "MONEY", "NOW"],
    ["Win", "Prize", "Now"]
]

df, vocab = compute_tfidf(
    corpus,
    min_df=1,      # appear in at least 1 document
    max_df=1.0,    # appear in at most all documents
    ngram_range=(1, 1)
)

with open('4-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write(str(df))


#!/usr/bin/env python3

compute_tfidf = __import__('11-tf_idf').tf_idf


def lowercase_tokenizer(text):
    return [t.lower() for t in text.split()]


corpus = [
    ["Win", "money"],
    ["money", "win"],
]

df, vocab = compute_tfidf(
    corpus,
    tokenizer_fn=lowercase_tokenizer,
    min_df=1,
    max_df=1.0
)

with open('5-output', 'w') as f:
    f.write("Vocabulary: " + str(vocab) + "\n")
    f.write(str(df))


#!/usr/bin/env python3

import pandas as pd

clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens
compute_tfidf = __import__('11-tf_idf').tf_idf

df_raw = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])
sample = df_raw.sample(50, random_state=1)

corpus = []
for msg in sample["message"]:
    toks = filter_tokens(remove_stopwords(tokenize_text(clean_text(msg))))
    corpus.append(toks)

df, vocab = compute_tfidf(corpus, max_features=150)

with open('6-output', 'w') as f:
    f.write("Vocabulary size: " + str(len(vocab)) + "\n")
    f.write("Shape: " + str(df.shape) + "\n")
    f.write("First 20 vocab: " + str(vocab[:20]) + "\n")
    f.write(str(df.head()))