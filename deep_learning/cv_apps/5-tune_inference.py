#!/usr/bin/env python3
"""
Task 5
"""
from ultralytics import YOLO


def inference_tuning(data_yaml, model="yolov8n.pt", imgsz=640,
                     conf_list=[0.25, 0.4, 0.5], iou_list=[0.45, 0.5, 0.6]):
    """
    This function evaluates different (conf, iou) combinations
    on the validation set and reports their performance.

    Args:
        data_yaml: dataset YAML path (must include validation set).
        model: trained model path or model name.
        imgsz: image size for inference.
        conf_list: list of confidence thresholds to try.
        iou_list: list of IoU thresholds to try.

    Returns:
        list of dicts with inference parameters and val scores.
    """
    yolo_model = YOLO(model, verbose=False)

    results = []

    for conf in conf_list:
        for iou in iou_list:

            val_kwargs = {
                "data": data_yaml,
                "imgsz": imgsz,
                "conf": conf,
                "iou": iou
            }

            metrics = yolo_model.val(**val_kwargs, verbose=False,
                                     batch=2, plots=False, workers=0)

            # Safely extract mAP metrics
            map50 = None
            map50_95 = None
            try:
                box = getattr(metrics, "box", None)
                if box:
                    map50 = getattr(box, "map50", None)
                    map50_95 = getattr(box, "map", None)
            except Exception:
                pass

            results.append({
                "conf": conf,
                "iou": iou,
                "map50": map50,
                "map50_95": map50_95
            })

    return results
