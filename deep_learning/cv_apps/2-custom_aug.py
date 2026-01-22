#!/usr/bin/env python3
"""
    Task 2
"""
from ultralytics import YOLO
import albumentations as A
import numpy as np


def custom_aug(image, bboxes, labels):
    """
    Apply YOLO-exclusive Albumentations augmentations.

    Args:
        image (np.ndarray): Input image
        bboxes (List[List[int]]): Bounding boxes in Pascal VOC format
        labels (List[int]): Class labels corresponding to each bounding box

    Returns:
        Tuple: Augmented image, bounding boxes, and labels
    """
    transform = A.Compose(
        [
            # Add motion blur randomly
            A.MotionBlur(blur_limit=5, p=0.9),

            # Add Gaussian noise
            # A.GaussNoise(var_limit=(10.0, 50.0), p=0.9),

            # Optional: elastic or optical distortions
            A.OneOf([
                A.ElasticTransform(alpha=1, sigma=50, p=0.2),
                A.OpticalDistortion(distort_limit=0.05, p=0.2)
            ], p=0.9),
        ],
        bbox_params=A.BboxParams(format='pascal_voc', label_fields=['labels']),
        seed=42
    )

    augmented = transform(image=image, bboxes=bboxes, labels=labels)

    aug_image = augmented['image']
    aug_bboxes = np.array(augmented['bboxes'])
    aug_labels = augmented['labels']

    return aug_image, aug_bboxes, aug_labels
