#!/usr/bin/env python3
from ultralytics import YOLO


def train_with_augmentation(
    data,
    model_path="yolov8n.pt",
    epochs=10,
    imgsz=640,
    batch=16,
    augmentation=True,
    yolo_aug_params=None,
    albumentations_transforms=None,
    save=False,
    plots=False,
    verbose=False,
):

    model = YOLO(model_path)

    # Base arguments
    train_kwargs = dict(
        data=data,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        save=save,
        plots=plots,
        verbose=verbose,
    )

    # Custom Albumentations
    if albumentations_transforms is not None:
        train_kwargs["augmentations"] = albumentations_transforms

    # Custom YOLO augment params
    elif yolo_aug_params is not None:
        train_kwargs.update(yolo_aug_params)

    # Disable augmentation
    elif not augmentation:
        train_kwargs.update(
            hsv_h=0.0,
            hsv_s=0.0,
            hsv_v=0.0,
            translate=0.0,
            scale=0.0,
            fliplr=0.0,
            mosaic=0.0,
            erasing=0.0,
            auto_augment=None,
        )

    # Train
    results = model.train(**train_kwargs)
    return model, results
