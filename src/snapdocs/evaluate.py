"""Đánh giá phương pháp phát hiện so với nhãn 4 góc chuẩn. (T08)"""
import numpy as np


def corner_error(pred: np.ndarray, truth: np.ndarray) -> float:
    """Sai số góc trung bình (pixel) giữa hai bộ 4 điểm cùng thứ tự."""
    pred = np.asarray(pred, dtype=np.float32).reshape(4, 2)
    truth = np.asarray(truth, dtype=np.float32).reshape(4, 2)
    return float(np.linalg.norm(pred - truth, axis=1).mean())
