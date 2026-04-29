#!/usr/bin/env python3
"""
Task 4: Evaluate Decision Tree Classifier
"""
from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    return metrics.classification_report(true_labels, predicted_labels, target_names=class_names)