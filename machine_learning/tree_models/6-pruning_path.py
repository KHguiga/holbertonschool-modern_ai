#!/usr/bin/env python3
"""
Task 6: Post-Pruning cost complexity
"""


def get_pruning_path(clf, X, y):
    """
    """
    path = clf.cost_complexity_pruning_path(X, y)
    return path.ccp_alphas, path.impurities