#!/usr/bin/env python3
"""
    Task 1
"""
import albumentations as A
import numpy as np


def basic_aug(image, bboxes, labels):
    """
    Docstring for basic_aug

    :param image: Description
    :param bboxes: Description
    :param labels: Description
    """
    transform = A.Compose(
        [
            A.HorizontalFlip(p=0.5),
            A.RandomBrightnessContrast(p=0.2),
            A.Affine(
                translate_percent=0.1,
                scale=0.9,
                rotate=[-30, 0],
                p=1
            )
        ],
        bbox_params=A.BboxParams(
            format="pascal_voc",
            label_fields=["labels"]
        ), seed=42
    )

    augmented = transform(image=image, bboxes=bboxes, labels=labels)

    return (
        augmented["image"],
        np.array(augmented["bboxes"]),
        augmented["labels"]
    )
