#!/usr/bin/env python3

from tensorflow import keras
mobilenet_backbone = __import__('5-mobilenet_backbone'
                                ).mobilenet_backbone


def mobilenet(input_shape=(224, 224, 3), num_classes=1000):
    """
    Builds the full MobileNetV1 model

    Args:
        input_shape: shape of input images
        num_classes: number of output classes

    Returns:
        Keras Model
    """

    inputs = keras.layers.Input(shape=input_shape)

    # Backbone
    X = mobilenet_backbone(inputs)

    # Classification head
    X = keras.layers.GlobalAveragePooling2D()(X)
    outputs = keras.layers.Dense(num_classes, activation="softmax")(X)

    model = keras.Model(inputs, outputs, name="MobileNetV1")

    return model
