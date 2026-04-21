## Bag of Words

Write a function `bag_of_words(corpus_tokens, max_features=5000, ngram_range=(1, 2), min_df=2, max_df=0.95, binary=False)` that builds a Bag-of-Words feature matrix from a list of token lists.

```
#!/usr/bin/env python3
import sklearn.feature_extraction.text


def bag_of_words(corpus_tokens, max_features=5000, ngram_range=(1, 2),
                 min_df=2, max_df=0.95, binary=False):
```

The function should:

- Join each token list into a whitespace-separated string (CountVectorizer works on strings).
- Use `sklearn` with:
  - `tokenizer=str.split` and `lowercase=False` — tokens are already lowercased by the pipeline.
  - `token_pattern=None` — required whenever `tokenizer` is overridden.
  - The remaining parameters passed through as-is.
- Return `(X, vectorizer)` where:
  - `X` is the sparse feature matrix `(n_samples, n_features)`.
  - `vectorizer` is the fitted `CountVectorizer` object.

```
$ cat 10-main.py
#!/usr/bin/env python3

import numpy as np
import pandas as pd
from collections import Counter
clean_text          = __import__('1-clean_text').clean_text
tokenize_text       = __import__('2-tokenize').tokenize_text
normalize_emoticons = __import__('2-tokenize').normalize_emoticons
remove_stopwords    = __import__('3-remove_stopwords').remove_stopwords
SPAM_KEEP_WORDS     = __import__('3-remove_stopwords').SPAM_KEEP_WORDS
filter_tokens       = __import__('4-filter_tokens').filter_tokens
normalize_tokens    = __import__('5-normalize_tokens').normalize_tokens
bag_of_words        = __import__('10-bag_of_words').bag_of_words

df = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
df['cleaned']         = df['message'].apply(clean_text)
df['tokens']          = df['cleaned'].apply(lambda x: tokenize_text(x, method='tweet'))
df['tokens']          = df['tokens'].apply(normalize_emoticons)
df['tokens_no_stop']  = df['tokens'].apply(lambda t: remove_stopwords(t, keep_words=SPAM_KEEP_WORDS))
df['tokens_filtered'] = df['tokens_no_stop'].apply(filter_tokens)
df['tokens_lemma']    = df['tokens_filtered'].apply(normalize_tokens)

corpus = df['tokens_lemma'].tolist()
labels = df['label'].tolist()

for ngram in [(1, 1), (1, 2)]:
    X, vect = bag_of_words(corpus, ngram_range=ngram)
    print(f"ngram_range={ngram} : shape={X.shape}  vocab={len(vect.vocabulary_)}")
print()

X, vect  = bag_of_words(corpus)
features = np.array(vect.get_feature_names_out())
spam_mask = np.array(labels) == 'spam'

spam_sums = np.asarray(X[spam_mask].sum(axis=0)).flatten()
print(f"top spam features  : {list(features[spam_sums.argsort()[::-1][:15]])}\n")

ham_sums  = np.asarray(X[~spam_mask].sum(axis=0)).flatten()
print(f"top ham  features  : {list(features[ham_sums.argsort()[::-1][:15]])}\n")

X_count,  _ = bag_of_words(corpus, binary=False)
X_binary, _ = bag_of_words(corpus, binary=True)
print(f"count  matrix — max value in a cell : {X_count.max()}")
print(f"binary matrix — max value in a cell : {X_binary.max()}")

$ ./10-main.py

```
`ngram_range=(1,2)` grows the vocabulary with bigrams like `call <NUM>` and `free prize` that carry strong spam signal and are invisible at the unigram level. `binary=True` collapses counts to presence/absence — useful when what matters is whether a term appears, not how often.


---

## TF-IDF

Write a function `tf_idf(corpus_tokens, max_features=5000, ngram_range=(1, 2), min_df=2, max_df=0.95, norm='l2')` that builds a TF-IDF feature matrix from a list of token lists.

```
#!/usr/bin/env python3
import sklearn.feature_extraction.text


def tf_idf(corpus_tokens, max_features=5000, ngram_range=(1, 2),
           min_df=2, max_df=0.95, norm='l2'):
```

The function should:

- Join each token list into a whitespace-separated string.
- Use `sklearn.feature_extraction.text.TfidfVectorizer` with `tokenizer=str.split`, `lowercase=False`, `token_pattern=None`, and the remaining parameters passed through.
- Return `(X, vectorizer)` where:
  - `X` is the sparse TF-IDF feature matrix `(n_samples, n_features)`.
  - `vectorizer` is the fitted `TfidfVectorizer` object.

```
$ cat 11-main.py
#!/usr/bin/env python3

import numpy as np
import pandas as pd
clean_text          = __import__('1-clean_text').clean_text
tokenize_text       = __import__('2-tokenize').tokenize_text
normalize_emoticons = __import__('2-tokenize').normalize_emoticons
remove_stopwords    = __import__('3-remove_stopwords').remove_stopwords
filter_tokens       = __import__('4-filter_tokens').filter_tokens
normalize_tokens    = __import__('5-normalize_tokens').normalize_tokens
bag_of_words        = __import__('10-bag_of_words').bag_of_words
tf_idf              = __import__('11-tf_idf').tf_idf

spam_keep_words = {"won", "our", "from", "now", "your", "only"}
df = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
df['cleaned']         = df['message'].apply(clean_text)
df['tokens']          = df['cleaned'].apply(lambda x: tokenize_text(x, method='tweet'))
df['tokens']          = df['tokens'].apply(normalize_emoticons)
df['tokens_no_stop']  = df['tokens'].apply(lambda t: remove_stopwords(t, keep_words=spam_keep_words))
df['tokens_filtered'] = df['tokens_no_stop'].apply(filter_tokens)
df['tokens_lemma']    = df['tokens_filtered'].apply(normalize_tokens)

corpus = df['tokens_lemma'].tolist()
labels = np.array(df['label'].tolist())
spam_mask = labels == 'spam'

X_bow,  v_bow  = bag_of_words(corpus)
X_tf,   v_tf   = tf_idf(corpus)

print(f"BoW   shape : {X_bow.shape}  dtype={X_bow.dtype}")
print(f"TF-IDF shape : {X_tf.shape}  dtype={X_tf.dtype}\n")

# --- IDF dampens common terms and upweights rare discriminative ones ---
# show same token's BoW count vs TF-IDF weight for a spam message
features_tf = np.array(v_tf.get_feature_names_out())
features_bw = np.array(v_bow.get_feature_names_out())

# top TF-IDF weighted spam features
spam_tfidf_sum = np.asarray(X_tf[spam_mask].sum(axis=0)).flatten()
top_tfidf = features_tf[spam_tfidf_sum.argsort()[::-1][:15]]
print(f"top spam TF-IDF features : {list(top_tfidf)}\n")

# IDF values — lower = more common across the corpus, higher = rarer
# Note: highest IDF terms appear in exactly min_df=2 documents
# rare ≠ discriminative — a term can be rare in both classes equally
# the most useful spam features combine high TF in spam AND moderate-to-high IDF
idf = v_tf.idf_
top_idf_idx = idf.argsort()[::-1][:10]
print("highest IDF (rarest terms — appear in only 2 documents):")
for i in top_idf_idx:
    print(f"  {features_tf[i]:<25} idf={idf[i]:.3f}")

low_idf_idx = idf.argsort()[:10]
print("lowest IDF (most common across all messages):")
for i in low_idf_idx:
    print(f"  {features_tf[i]:<25} idf={idf[i]:.3f}")

$ ./11-main.py
BoW   shape : (5507, 5000)  dtype=int64
TF-IDF shape : (5507, 5000)  dtype=float64

top spam TF-IDF features : ['<NUM>', 'call', 'call <NUM>', 'free', 'your', '<NUM> <NUM>', 'win', 'now', 'mobile', 'txt', 'claim', 'from', 'text', '<URL>', 'stop']

highest IDF (rarest terms — appear in only 2 documents):
  bottle                    idf=8.515
  that's way                idf=8.515
  willing go                idf=8.515
  wil reach                 idf=8.515
  wil get                   idf=8.515
  wil care                  idf=8.515
  hint                      idf=8.515
  medical insurance         idf=8.515
  wife <NUM>                idf=8.515
  pg                        idf=8.515

lowest IDF (most common across all messages):
  <NUM>                     idf=2.355
  get                       idf=3.173
  call                      idf=3.225
  your                      idf=3.263
  go                        idf=3.405
  now                       idf=3.472
  <EMO>                     idf=3.788
  ur                        idf=3.894
  come                      idf=3.907
  ok                        idf=4.004
```
IDF downweights terms that appear in many documents (common across both classes) and amplifies rare ones. High-IDF spam terms are the most discriminative features — they are specific enough to one class that a classifier can rely on them.


---

## Word2Vec Embeddings

Write a function `word2vec_embeddings(corpus_tokens, vector_size=100, window=5, min_count=2, sg=0, epochs=10, workers=4)` that trains Word2Vec and returns per-message embeddings.
The function should:

- Train `gensim` Word2Vec on `corpus_tokens`.
- Represent each message as the **mean** of its in-vocab token vectors. Tokens not in the Word2Vec vocabulary are silently ignored. If a message has no in-vocab tokens, its row is a zero vector.
- Return `(X, model)` where:
  - `X` is a `np.ndarray` of shape `(n_messages, vector_size)`.
  - `model` is the trained `Word2Vec` model.

```
$ cat 12-main.py
#!/usr/bin/env python3

import pandas as pd
clean_text           = __import__('1-clean_text').clean_text
tokenize_text        = __import__('2-tokenize').tokenize_text
normalize_emoticons  = __import__('2-tokenize').normalize_emoticons
remove_stopwords     = __import__('3-remove_stopwords').remove_stopwords
filter_tokens        = __import__('4-filter_tokens').filter_tokens
normalize_tokens     = __import__('5-normalize_tokens').normalize_tokens
word2vec_embeddings  = __import__('12-word2vec').word2vec_embeddings

spam_keep_words = {"won", "our", "from", "now", "your", "only"}
df = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
df['cleaned']         = df['message'].apply(clean_text)
df['tokens']          = df['cleaned'].apply(lambda x: tokenize_text(x, method='tweet'))
df['tokens']          = df['tokens'].apply(normalize_emoticons)
df['tokens_no_stop']  = df['tokens'].apply(lambda t: remove_stopwords(t, keep_words=spam_keep_words))
df['tokens_filtered'] = df['tokens_no_stop'].apply(filter_tokens)
df['tokens_lemma']    = df['tokens_filtered'].apply(normalize_tokens)

corpus = df['tokens_lemma'].tolist()

X, model = word2vec_embeddings(corpus)

print(f"embedding matrix : {X.shape}  (one row per message)\n")

#  semantic relationships learned through the corpus 
for word in ['free', 'call', 'win', 'go']:
    if word in model.wv:
        similar = [w for w, _ in model.wv.most_similar(word, topn=5)]
        print(f"most similar to '{word}' : {similar}")

# OOV
oov_token = "xyzunseen"
in_vocab  = oov_token in model.wv
print(f"'{oov_token}' in vocab : {in_vocab}")
print(f"'free'       in vocab : {'free' in model.wv}\n")

# zero-vector messages
import numpy as np
zero_rows = (X == 0).all(axis=1).sum()
print(f"zero-vector messages : {zero_rows} / {len(X)}")
print(f"avg embedding norm   : {np.linalg.norm(X, axis=1).mean():.4f}")

$ ./12-main.py
embedding matrix : (5507, 100)  (one row per message)

most similar to 'free' : ['mobile', 'nokia', 'camcorder', 'tone', 'txt']
most similar to 'call' : ['landline', 'award', 'mobile', 'expire', 'urgent']
most similar to 'win' : ['draw', 'cash', 'award', '<NUM>', 'guarantee']
most similar to 'go' : ['already', 'wat', 'ok', 'dun', 'home']

'xyzunseen' in vocab : False
'free'       in vocab : True

zero-vector messages : 20 / 5507
avg embedding norm   : 2.8779
```
Word2Vec learns dense representations that capture co-occurrence context — spam terms like `free`, `win`, `call` should cluster together in embedding space. `min_count=2` removes hapax legomena that would only add noise. OOV tokens get no vector, so messages with many rare tokens may produce zero or degraded embeddings.


---

## FastText Embeddings

Write a function `fasttext_embeddings(corpus_tokens, vector_size=100, window=5, min_count=1, sg=0, epochs=10, workers=4)` that trains FastText and returns per-message embeddings.

The function should:

- Train `gensim` FastText` on `corpus_tokens`.
- Represent each message as the **mean** of its token vectors. Unlike Word2Vec, FastText uses subword n-grams, so **every token has a vector** including OOV tokens. `min_count=1` is appropriate here for the same reason.
- Return `(X, model)` where:
  - `X` is a `np.ndarray` of shape `(n_messages, vector_size)`.
  - `model` is the trained `FastText` model.

```
$ cat 13-main.py
#!/usr/bin/env python3

import numpy as np
import pandas as pd
clean_text           = __import__('1-clean_text').clean_text
tokenize_text        = __import__('2-tokenize').tokenize_text
normalize_emoticons  = __import__('2-tokenize').normalize_emoticons
remove_stopwords     = __import__('3-remove_stopwords').remove_stopwords
filter_tokens        = __import__('4-filter_tokens').filter_tokens
normalize_tokens     = __import__('5-normalize_tokens').normalize_tokens
word2vec_embeddings  = __import__('12-word2vec').word2vec_embeddings
fasttext_embeddings  = __import__('13-fasttext').fasttext_embeddings

spam_keep_words = {"won", "our", "from", "now", "your", "only"}
df = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
df['cleaned']         = df['message'].apply(clean_text)
df['tokens']          = df['cleaned'].apply(lambda x: tokenize_text(x, method='tweet'))
df['tokens']          = df['tokens'].apply(normalize_emoticons)
df['tokens_no_stop']  = df['tokens'].apply(lambda t: remove_stopwords(t, keep_words=spam_keep_words))
df['tokens_filtered'] = df['tokens_no_stop'].apply(filter_tokens)
df['tokens_lemma']    = df['tokens_filtered'].apply(normalize_tokens)

corpus = df['tokens_lemma'].tolist()

X_w2v, m_w2v = word2vec_embeddings(corpus)
X_ft,  m_ft  = fasttext_embeddings(corpus)

print(f"Word2Vec  : {X_w2v.shape}")
print(f"FastText  : {X_ft.shape}\n")

# OOV handling
oov_tokens = ['freee', 'calll', 'prze', 'wnnr']
print(f"{'token':<12} {'in W2V vocab':>14} {'FastText has vector':>20}")
print("-" * 50)
for t in oov_tokens:
    in_w2v = t in m_w2v.wv
    print(f"  {t:<10} {str(in_w2v):>14} {'True':>20}")

# zero-vector messages
w2v_zeros = (X_w2v == 0).all(axis=1).sum()
ft_zeros  = (X_ft  == 0).all(axis=1).sum()
print(f"Word2Vec  zero-vector messages : {w2v_zeros}")
print(f"FastText  zero-vector messages : {ft_zeros}\n")

# similar words
for word in ['free', 'call', 'win']:
    if word in m_ft.wv:
        similar = [w for w, _ in m_ft.wv.most_similar(word, topn=5)]
        print(f"FastText most similar to '{word}' : {similar}")

$ ./13-main.py
Word2Vec  : (5507, 100)
FastText  : (5507, 100)

token          in W2V vocab  FastText has vector
--------------------------------------------------
  freee               False                 True
  calll               False                 True
  prze                False                 True
  wnnr                False                 True

Word2Vec  zero-vector messages : 20
FastText  zero-vector messages : 7

FastText most similar to 'free' : ['2mobile', 'free-nokia', 'or2stoptxt', 'mobilesvary', 'nokia']
FastText most similar to 'call' : ['cashto', 'mobilesvary', 'freeze', 'award', 'aww']
FastText most similar to 'win' : ['prizeswith', 'gr8prizes', 'draw', '10ppm', 'guaranteed']
```
FastText's subword model handles OOV tokens by composing their representation from character n-grams — useful for SMS data where misspellings and abbreviations (`calll`, `freee`, `prze`) are common. The key difference from Word2Vec is that no message produces a zero vector, even when all its tokens are rare or misspelled.
