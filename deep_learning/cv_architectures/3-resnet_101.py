#!/usr/bin/env python3
"""
    Task 3
"""
from tensorflow import keras
bottleneck_block = __import__('2-bottleneck_block').bottleneck_block


def make_layer(x, blocks, filters, stride=1, name=None):
    """Create a layer with multiple bottleneck blocks"""
    # First block with potential downsampling
    x = bottleneck_block(x, filters, stride=stride, downsample=True,
                         name=f'{name}_block1')

    # Remaining blocks
    for i in range(1, blocks):
        x = bottleneck_block(x, filters, stride=1, downsample=False,
                             name=f'{name}_block{i+1}')

    return x


def build_resnet101(input_shape=(224, 224, 3), num_classes=1000):
    """Build ResNet-101 model using the two helper functions"""
    # Input layer
    inputs = keras.layers.Input(shape=input_shape)

    # Stem
    x = keras.layers.Conv2D(64, 7, strides=2, padding='same', use_bias=False,
                            name='conv1')(inputs)
    x = keras.layers.BatchNormalization(name='bn1')(x)
    x = keras.layers.ReLU(name='relu1')(x)
    x = keras.layers.MaxPool2D(3, strides=2, padding='same', name='maxpool')(x)

    # ResNet layers (3, 4, 23, 3 bottleneck blocks as in ResNet-101)
    x = make_layer(x, blocks=3, filters=64, stride=1, name='layer1')
    x = make_layer(x, blocks=4, filters=128, stride=2, name='layer2')
    x = make_layer(x, blocks=23, filters=256, stride=2, name='layer3')
    x = make_layer(x, blocks=3, filters=512, stride=2, name='layer4')

    # Head
    x = keras.layers.GlobalAveragePooling2D(name='avgpool')(x)
    outputs = keras.layers.Dense(num_classes, activation='softmax',
                                 name='fc')(x)

    # Create model
    model = keras.Model(inputs, outputs, name='resnet101')

    return model
