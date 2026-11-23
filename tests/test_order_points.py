import numpy as np

from snapdocs import order_points
from snapdocs.evaluate import corner_error


def test_order_points_shuffled():
    tl, tr, br, bl = (10, 20), (200, 30), (210, 300), (5, 290)
    shuffled = np.array([br, tl, bl, tr], dtype=np.float32)
    out = order_points(shuffled)
    assert np.allclose(out, np.array([tl, tr, br, bl], dtype=np.float32))


def test_corner_error_zero_and_shift():
    pts = np.array([[0, 0], [10, 0], [10, 10], [0, 10]], dtype=np.float32)
    assert corner_error(pts, pts) == 0.0
    assert abs(corner_error(pts + [3, 4], pts) - 5.0) < 1e-6
