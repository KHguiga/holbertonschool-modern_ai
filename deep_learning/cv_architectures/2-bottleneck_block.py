#!/usr/bin/env python3
"""
    Task 2 - corrected
"""
from tensorflow import keras


def bottleneck_block(x, filters, stride=1, downsample=False, name=None):
    """Bottleneck block for ResNet-50/101/152 (fixed projection path)"""
    identity = x

    # First 1x1 convolution
    x = keras.layers.Conv2D(filters, 1, strides=1, padding='same',
                            use_bias=False, name=f'{name}_conv1')(x)
    x = keras.layers.BatchNormalization(name=f'{name}_bn1')(x)
    x = keras.layers.ReLU(name=f'{name}_relu1')(x)

    # 3x3 convolution (may change spatial dims via stride)
    x = keras.layers.Conv2D(filters, 3, strides=stride, padding='same',
                            use_bias=False, name=f'{name}_conv2')(x)
    x = keras.layers.BatchNormalization(name=f'{name}_bn2')(x)
    x = keras.layers.ReLU(name=f'{name}_relu2')(x)

    # Second 1x1 convolution (expansion)
    x = keras.layers.Conv2D(filters * 4, 1, strides=1, padding='same',
                            use_bias=False, name=f'{name}_conv3')(x)
    x = keras.layers.BatchNormalization(name=f'{name}_bn3')(x)

    # Prepare shortcut (projection) if needed
    if downsample:
        shortcut = keras.layers.Conv2D(filters * 4, 1, strides=stride,
                                       padding='same', use_bias=False,
                                       name=f'{name}_downsample')(identity)
        # IMPORTANT: apply BN to the conv output, not to `identity`
        shortcut = keras.layers.BatchNormalization(name=f'{name}_bn_downsample'
                                                   )(shortcut)
    else:
        shortcut = identity

    # Add skip connection
    x = keras.layers.Add(name=f'{name}_add')([x, shortcut])
    x = keras.layers.ReLU(name=f'{name}_out')(x)

    return x
