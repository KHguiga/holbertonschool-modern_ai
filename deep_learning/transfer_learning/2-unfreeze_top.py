#!/usr/bin/env python3
"""
Task 2 Unfreezing Top Layers
"""


def unfreeze_top_layers(base_model, n_layers):
    """
    Docstring for unfreeze_top_layers

    :param base_model: A full Keras Model with a base model as its 2nd layer.
    :param n_layers: An Integer specifying how many of the last layers in
    the base model should be unfrozen (set as trainable).
    """
    # Freeze all but the last n_layers of the base_model
    for layer in base_model.layers[:-n_layers]:
        layer.trainable = False
    for layer in base_model.layers[-n_layers:]:
        layer.trainable = True
