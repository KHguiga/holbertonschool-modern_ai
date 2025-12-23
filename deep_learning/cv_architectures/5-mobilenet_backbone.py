#!/usr/bin/env python3
"""
    Task 5
"""
from tensorflow import keras
depthwise_separable_conv = __import__('4-depthwise_separable_conv'
                                      ).depthwise_separable_conv


def mobilenet_backbone(inputs):
    """
    MobileNetV1 backbone (feature extractor)

    Args:
        inputs: input tensor

    Returns:
        Output tensor of backbone
    """

    # Initial standard convolution
    X = keras.layers.Conv2D(
        32,
        kernel_size=3,
        strides=2,
        padding="same",
        use_bias=False
    )(inputs)
    X = keras.layers.BatchNormalization()(X)
    X = keras.layers.ReLU(6.0)(X)

    # Depthwise separable blocks
    X = depthwise_separable_conv(X, 64, stride=1)

    X = depthwise_separable_conv(X, 128, stride=2)
    X = depthwise_separable_conv(X, 128, stride=1)

    X = depthwise_separable_conv(X, 256, stride=2)
    X = depthwise_separable_conv(X, 256, stride=1)

    X = depthwise_separable_conv(X, 512, stride=2)

    # 5 repeated blocks with 512 filters
    for _ in range(5):
        X = depthwise_separable_conv(X, 512, stride=1)

    X = depthwise_separable_conv(X, 1024, stride=2)
    X = depthwise_separable_conv(X, 1024, stride=1)

    return X
