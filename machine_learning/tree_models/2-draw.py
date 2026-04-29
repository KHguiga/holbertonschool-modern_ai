#!/usr/bin/env python3
"""
Task 2: View the Decision Rules of a Trained Tree
"""
from sklearn import tree


def draw(clf, feature_names, class_names):
    r =tree.export_text(clf, feature_names=feature_names,
                        class_names=class_names)
    print(r)