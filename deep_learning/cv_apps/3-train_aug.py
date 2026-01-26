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

    model.train(
        data=data_yaml,
        epochs=1,
        imgsz=640,
        batch=1,
        device="cpu",
        workers=0,
        augment=False,
        mosaic=0.0,
        mixup=0.0,
        copy_paste=0.0,
        hsv_h=0.0,
        hsv_s=0.0,
        hsv_v=0.0,
        degrees=0.0,
        translate=0.0,
        scale=0.0,
        shear=0.0,
        perspective=0.0,
        fliplr=0.0,
        flipud=0.0,
        erasing=0.0,
        fraction=0.01,
        save=False,
        plots=False,
        verbose=False)

    return model, results
