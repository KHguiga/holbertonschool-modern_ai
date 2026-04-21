#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder

clean_text          = __import__('1-clean_text').clean_text
tokenize_text       = __import__('2-tokenize').tokenize_text
normalize_emoticons = __import__('2-tokenize').normalize_emoticons
remove_stopwords    = __import__('3-remove_stopwords').remove_stopwords
filter_tokens       = __import__('4-filter_tokens').filter_tokens
normalize_tokens    = __import__('5-normalize_tokens').normalize_tokens
tf_idf              = __import__('11-tf_idf').tf_idf
bag_of_words        = __import__('10-bag_of_words').bag_of_words

spam_keep_words = {"our", "from", "now", "your", "only"}
df = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
df['cleaned']         = df['message'].apply(clean_text)
df['tokens']          = df['cleaned'].apply(lambda x: tokenize_text(x, method='tweet'))
df['tokens']          = df['tokens'].apply(normalize_emoticons)
df['tokens_no_stop']  = df['tokens'].apply(lambda t: remove_stopwords(t, keep_words=spam_keep_words))
df['tokens_filtered'] = df['tokens_no_stop'].apply(filter_tokens)
df['tokens_lemma']    = df['tokens_filtered'].apply(normalize_tokens)

corpus = df['tokens_lemma'].tolist()
y  = LabelEncoder().fit_transform(df['label'])
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

def f1(clf, X):
    return cross_val_score(clf, X, y, cv=cv, scoring='f1').mean()

# 4a. LR regularization strength vs max_features
print("=== LR C VALUE vs MAX_FEATURES (TF-IDF, ngram=(1,2)) ===")
print(f"{'max_features':<15} {'C=0.1':>8} {'C=1':>8} {'C=5':>8} {'C=10':>8} {'C=50':>8}")
for mf in [1000, 2000, 3000, 5000]:
    scores = []
    for C in [0.1, 1, 5, 10, 50]:
        X, _ = tf_idf(corpus, max_features=mf, ngram_range=(1,2))
        scores.append(f1(LogisticRegression(C=C, max_iter=2000), X))
    print(f"{str(mf):<15} " + " ".join(f"{s:>8.4f}" for s in scores))

# 4b. LinearSVC vs max_features — increased max_iter and tolerance
print("\n=== LINEARSVC vs MAX_FEATURES (TF-IDF, ngram=(1,2)) ===")
for mf in [1000, 1500, 2000, 3000, 5000, None]:
    X, _ = tf_idf(corpus, max_features=mf, ngram_range=(1,2))
    # Increase max_iter to 10000 and relax tolerance slightly to guarantee convergence
    print(f"  max_features={str(mf):<6}  vocab={X.shape[1]}  f1={f1(LinearSVC(max_iter=10000, tol=1e-3), X):.4f}")

# 4c. BoW + LR vs max_features
print("\n=== BOW + LR vs MAX_FEATURES (ngram=(1,2)) ===")
for mf in [1000, 2000, 3000, 5000, None]:
    X, _ = bag_of_words(corpus, max_features=mf, ngram_range=(1,2))
    print(f"  max_features={str(mf):<6}  vocab={X.shape[1]}  f1={f1(LogisticRegression(max_iter=2000), X):.4f}")

# 4d. best overall combos — confirm the winner with the right parameters
print("\n=== FINAL CONFIRMATION: BEST COMBOS ===")
configs = [
    ("BoW  (1,2) mf=5000  + LR  C=1",   bag_of_words, dict(ngram_range=(1,2), max_features=5000),  LogisticRegression(C=1,  max_iter=2000)),
    ("BoW  (1,2) mf=5000  + SVC",        bag_of_words, dict(ngram_range=(1,2), max_features=5000),  LinearSVC(max_iter=10000, tol=1e-3)),
    ("TF   (1,2) mf=5000  + SVC",        tf_idf,       dict(ngram_range=(1,2), max_features=5000),  LinearSVC(max_iter=10000, tol=1e-3)),
    ("TF   (1,1) mf=5000  + SVC",        tf_idf,       dict(ngram_range=(1,1), max_features=5000),  LinearSVC(max_iter=10000, tol=1e-3)),
    ("TF   (1,2) mf=1000  + LR  C=1",   tf_idf,       dict(ngram_range=(1,2), max_features=1000),  LogisticRegression(C=1,  max_iter=2000)),
    ("TF   (1,2) mf=1000  + LR  C=0.1", tf_idf,       dict(ngram_range=(1,2), max_features=1000),  LogisticRegression(C=0.1,max_iter=2000)),
]
for name, fn, kwargs, clf in configs:
    X, _ = fn(corpus, **kwargs)
    print(f"  {name:<40}  f1={f1(clf, X):.4f}")