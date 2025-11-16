#!/usr/bin/env python3
"""
Task 5 — Lemma vs Stem
"""

import nltk


nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('wordnet', quiet=True)


def get_pos(tag):
    """Map POS tag to WordNet POS for accurate lemmatization."""
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
    Normalize tokens:
      - method="lemmatize": context-aware lemmatization
      - method="stem": Porter stemming
    """
    if method not in {"lemmatize", "stem"}:
        raise ValueError("method must be 'lemmatize' or 'stem'")

    if method == "stem":
        stemmer = nltk.stem.PorterStemmer()
        return [stemmer.stem(t) for t in tokens]

    lemmatizer = nltk.stem.WordNetLemmatizer()
    # Use POS tagging for more accurate lemmatization
    tagged = nltk.pos_tag(tokens)
    return [lemmatizer.lemmatize(word, get_pos(pos)) for word, pos in tagged]
