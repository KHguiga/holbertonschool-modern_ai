#!/usr/bin/env python3
import numpy as np
import cv2
import matplotlib.pyplot as plt


def visualize_seg(image, label_path, alpha=0.5, seed=42):
    """
    Visualize YOLO instance segmentation labels on an image.

    Args:
        image (np.ndarray): RGB image of shape (H, W, 3)
        label_path (str): Path to YOLO segmentation label file
        alpha (float): Transparency factor for mask overlay
        seed (int): Random seed for deterministic colors
    """
    H, W, _ = image.shape

    # Initialize outputs
    instance_mask = np.zeros((H, W), dtype=np.int32)
    overlay = image.copy()

    # Deterministic colors
    np.random.seed(seed)

    with open(label_path, "r") as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        parts = line.strip().split()
        coords = np.array(parts[1:], dtype=np.float32)

        # Convert normalized coords → pixel coords
        coords[0::2] *= W
        coords[1::2] *= H
        polygon = coords.reshape(-1, 2).astype(np.int32)

        # Unique color per instance
        color = np.random.randint(0, 255, size=3).tolist()

        # ----- Instance mask -----
        cv2.fillPoly(instance_mask, [polygon], idx + 1)

        # ----- Filled overlay mask -----
        mask = np.zeros((H, W), dtype=np.uint8)
        cv2.fillPoly(mask, [polygon], 255)

        for c in range(3):
            overlay[:, :, c] = np.where(
                mask == 255,
                overlay[:, :, c] * (1 - alpha) + alpha * color[c],
                overlay[:, :, c],
            )

        # ----- Polygon boundary -----
        cv2.polylines(
            overlay,
            [polygon],
            isClosed=True,
            color=color,
            thickness=2,
        )

        # ----- Instance index at centroid -----
        centroid_x = int(np.mean(polygon[:, 0]))
        centroid_y = int(np.mean(polygon[:, 1]))

        cv2.putText(
            overlay,
            str(idx + 1),
            (centroid_x, centroid_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

    # Matplotlib-compatible visualization (RGB)
    plt.figure(figsize=(6, 6))
    plt.imshow(overlay)
    plt.axis("off")
    plt.title("YOLO Instance Segmentation Visualization")
    plt.show()
