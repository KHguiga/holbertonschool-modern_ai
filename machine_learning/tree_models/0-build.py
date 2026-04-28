#!/usr/bin/env python3
"""
Task 0: Building Decision Tree Classifier
"""
from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """
    """
    dc = tree.DecisionTreeClassifier(
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        random_state=random_state)

    return dc
