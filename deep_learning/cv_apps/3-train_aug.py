#!/usr/bin/env python3
"""
Task 3
"""
from ultralytics import YOLO


def train_with_augmentation(data_yaml, model="yolov8n.pt", aug=None,
                            custom_albu=None, epochs=10, imgsz=640, batch=16):
    """
    trains a YOLO model using data augmentation and allows custom
    Albumentations transforms to be applied during training.
    """
    model = YOLO(model)

    train_kwargs = {"data": data_yaml, "epochs": epochs,
                    "imgsz": imgsz, "batch": batch}

    if aug is not None:
        train_kwargs["augmentations"] = aug

    if custom_albu is not None:
        train_kwargs["augmentations"] = custom_albu

    results = model.train(**train_kwargs, save=False,
                          plots=False, verbose=False)

    return model, results
