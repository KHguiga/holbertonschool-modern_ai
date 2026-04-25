#!/usr/bin/env python3
"""
    Task 5 — Token Normalisation
"""
import re
import nltk

_PLACEHOLDER_RE = re.compile(r'^<[A-Za-z]+>$')


def get_pos(tag):
    """Map a Penn Treebank POS tag to a WordNet POS constant."""
    if tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    return nltk.corpus.wordnet.NOUN


def normalize_tokens(tokens, method="lemmatize"):
    """
    Task 5 — Token Normalisation
    Stemming vs Lemmatization
    """
    if method not in {"lemmatize", "stem"}:
        raise ValueError("method must be 'lemmatize' or 'stem'")

    if method == "stem":
        stemmer = nltk.stem.PorterStemmer()
        return [t if _PLACEHOLDER_RE.match(t)
                else stemmer.stem(t) for t in tokens]

    lemmatizer = nltk.stem.WordNetLemmatizer()
    tagged = nltk.pos_tag(tokens)
    return [
        t if _PLACEHOLDER_RE.match(t)
        else lemmatizer.lemmatize(word, get_pos(pos))
        for t, (word, pos) in zip(tokens, tagged)
    ]
