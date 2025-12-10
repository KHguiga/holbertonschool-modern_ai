#!/usr/bin/env python3
"""
    Task 1
"""
from tensorflow import keras


def compile_and_train_cnn(model, epochs, batch_size, x_train, y_train, x_val,
                          y_val, optimizer_name='adam', optimizer_params=None):
    """
    Docstring for compile_and_train_cnn
    :param model: Description
    :param epochs: Description
    :param batch_size: Description
    :param x_train: Description
    :param y_train: Description
    :param x_val: Description
    :param y_val: Description
    :param optimizer_name: Description
    :param optimizer_params: Description
    """
    if optimizer_params is None:
        optimizer_params = {}

    # Choose the optimizer and set its parameters
    if optimizer_name.lower() == 'adam':
        optimizer = keras.optimizers.Adam(**optimizer_params)
    elif optimizer_name.lower() == 'sgd':
        optimizer = keras.optimizers.SGD(**optimizer_params)
    elif optimizer_name.lower() == 'rmsprop':
        optimizer = keras.optimizers.RMSprop(**optimizer_params)
    else:
        raise ValueError(f"Unsupported optimizer: {optimizer_name}")

    # Compile the model
    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    # Train the model
    history = model.fit(
        x_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(x_val, y_val),
        verbose=2
    )
    return model, history
