"""Cảnh báo chất lượng ảnh chụp: mờ, quá xa, quá lệch. (T09)"""
import numpy as np


def check(image: np.ndarray, corners: np.ndarray | None) -> list[str]:
    """Trả về danh sách cảnh báo (rỗng nếu ảnh ổn). Ngưỡng phải dựa trên số liệu thật."""
    raise NotImplementedError("T09: chưa làm")
