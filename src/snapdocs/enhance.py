"""Tăng cường ảnh sau scan: cân bằng histogram/CLAHE, threshold. (T10)"""
import numpy as np


def enhance(image: np.ndarray, mode: str = "adaptive") -> np.ndarray:
    """mode: 'equalize' | 'clahe' | 'otsu' | 'adaptive'."""
    raise NotImplementedError("T10: chưa làm")
