#!/usr/bin/env python3
"""
Task 3 Data Augmentation
Simple implementation using only Keras layers
"""
from tensorflow import keras


def build_data_augmentation():
    """
    Builds a simple data augmentation pipeline using only Keras layers
    """
    data_aug = keras.Sequential([
        # Random horizontal flip
        keras.layers.RandomFlip("horizontal"),
        # Random rotation (±15 degrees)
        keras.layers.RandomRotation(0.15),
        # Random zoom (±15%)
        keras.layers.RandomZoom(0.15),
        # Random Contrast (±10%)
        keras.layers.RandomContrast(0.1),
    ])
    return data_aug
