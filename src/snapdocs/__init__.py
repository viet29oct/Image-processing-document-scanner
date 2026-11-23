"""SnapDocs — quét và nắn phẳng ảnh giấy tờ.

Quy ước chung cho mọi phương pháp phát hiện:
    detect(image: np.ndarray) -> np.ndarray | None
trả về mảng (4, 2) float32 theo thứ tự trên-trái, trên-phải, dưới-phải, dưới-trái,
hoặc None nếu không tìm được tài liệu.
"""
import numpy as np


def order_points(pts: np.ndarray) -> np.ndarray:
    """Sắp xếp 4 điểm: trên-trái, trên-phải, dưới-phải, dưới-trái."""
    pts = np.asarray(pts, dtype=np.float32).reshape(4, 2)
    s = pts.sum(axis=1)
    d = np.diff(pts, axis=1).ravel()  # y - x
    return np.array(
        [pts[np.argmin(s)], pts[np.argmin(d)], pts[np.argmax(s)], pts[np.argmax(d)]],
        dtype=np.float32,
    )
