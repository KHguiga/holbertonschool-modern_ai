#!/usr/bin/env python3
import pandas as pd

train_word2vec = __import__('12-word2vec').train_word2vec
clean_text = __import__('1-clean_text').clean_text
tokenize_text = __import__('2-tokenize').tokenize_text
remove_stopwords = __import__('3-remove_stopwords').remove_stopwords
filter_tokens = __import__('4-filter_tokens').filter_tokens
normalize_tokens = __import__('5-normalize_tokens').normalize_tokens

# Load dataset
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "message"])
sample = df.sample(50, random_state=0)


# Pipeline based on your functions ONLY
def preprocess_pipeline(msg):
    t = clean_text(msg)
    t = tokenize_text(t)
    t = remove_stopwords(t)
    t = filter_tokens(t)
    t = normalize_tokens(t)
    return t


# Apply to sample messages
corpus_tokens = [preprocess_pipeline(msg) for msg in sample['message']]

# Train Word2Vec
model = train_word2vec(
    corpus_tokens,
    vector_size=50,
    window=3,
    epochs=30
)

print("Vocabulary size:", len(model.wv))
print("Most similar to 'win':", model.wv.most_similar('win', topn=3), end="")
