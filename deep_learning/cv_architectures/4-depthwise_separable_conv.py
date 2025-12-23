#!/usr/bin/env python3
"""
    Task 4
"""
from tensorflow import keras


def depthwise_separable_conv(X, filters, stride=1):
    """
    Depthwise separable convolution block used in MobileNetV1

    Args:
        X: input tensor
        filters: number of output filters for pointwise conv
        stride: stride for depthwise convolution

    Returns:
        Output tensor
    """

    # Depthwise convolution
    X = keras.layers.DepthwiseConv2D(
        kernel_size=3,
        strides=stride,
        padding="same",
        use_bias=False
    )(X)
    X = keras.layers.BatchNormalization()(X)
    X = keras.layers.ReLU(6.0)(X)

    # Pointwise convolution
    X = keras.layers.Conv2D(
        filters,
        kernel_size=1,
        strides=1,
        padding="same",
        use_bias=False
    )(X)
    X = keras.layers.BatchNormalization()(X)
    X = keras.layers.ReLU(6.0)(X)

    return X
