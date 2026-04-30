#!/usr/bin/env python3
"""
Task 6: Post-Pruning cost complexity
"""


def get_pruning_path(clf, X, y):
    """
    """
    return clf.cost_complexity_pruning_path(X, y)