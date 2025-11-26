#!/usr/bin/env python3
"""
Task 0 Frozen Feature Extractor
"""

from tensorflow import keras


def build_feature_extractor():
    """
    Docstring for build_feature_extractor
    """
    base_model = keras.applications.MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights="imagenet"
    )
    base_model.trainable = False  # Freeze all layers

    inputs = keras.Input(shape=(224, 224, 3))
    x = base_model(inputs, training=False)
    x = keras.layers.GlobalAveragePooling2D()(x)

    return keras.Model(inputs, x)
