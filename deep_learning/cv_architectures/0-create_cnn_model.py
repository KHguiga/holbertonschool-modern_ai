#!/usr/bin/env python3
"""
    Task 0
"""
from tensorflow import keras


def create_cnn_model(input_shape, filters, kernel_sizes,
                     activations, pooling_type='max'):
    """
    Docstring for create_cnn_model
    :param input_shape: Description
    :param filters: Description
    :param kernel_sizes: Description
    :param activations: Description
    :param pooling_type: Description
    """
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=input_shape))

    for f, s, a in zip(filters, kernel_sizes, activations):
        model.add(keras.layers.Conv2D(f, s, activation=a))
        if pooling_type == 'max':
            model.add(keras.layers.MaxPooling2D((2, 2)))
        elif pooling_type == 'avg':
            model.add(keras.layers.AveragePooling2D((2, 2)))
        else:
            raise ValueError(f"Unsupported pooling type: {pooling_type}")

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(10, activation='softmax'))

    return model
