#!/usr/bin/env python3
"""
Task 5: Pre-Pruning
"""
from sklearn import model_selection

def prepruning(X, y, clf):
    params_grid = {
        'criterion': ('gini', 'entropy'),
        'max_depth':  range(2, 6),
        'min_samples_leaf':  range(2, 6),
        'min_samples_split':  range(2, 6)
    }
    g_cv = model_selection.GridSearchCV(clf, param_grid=params_grid)
    g_cv.fit(X=X, y=y)
    return g_cv.best_params_