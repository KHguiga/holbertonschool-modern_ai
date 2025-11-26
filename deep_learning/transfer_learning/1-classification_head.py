#!/usr/bin/env python3
"""
Task 1 Adding Classification Head
"""

from tensorflow import keras


def add_classification_head(base_model, num_classes):
    """
    Docstring for add_classification_head

    :param base_model: A Keras Model whose output is a pooled feature vector.
    :param num_classes: An integer representing the number of output classes.
    """
    x = base_model.output
    x = keras.layers.Dense(128, activation='relu')(x)
    outputs = keras.layers.Dense(num_classes, activation='softmax')(x)

    return keras.Model(inputs=base_model.input, outputs=outputs)
