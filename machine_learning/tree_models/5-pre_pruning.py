#!/usr/bin/env python3
"""
Task 5: Pre-Pruning
"""
from sklearn.model_selection import GridSearchCV

def prepruning(X, y, clf):
    params_grid = {
        'criteria': ('gini', 'entropy'),
        'max_depth': range(1, 5),
        'min_samples_leaf': range(1, 5),
        'min_samples_split': range(1, 5)
    }
    g_cv = GridSearchCV(clf, param_grid=params_grid)
    g_cv.fit(X=X, y=y)
    return g_cv.best_params_