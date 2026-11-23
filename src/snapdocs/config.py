"""Thông số dùng chung (xem docs/CONVENTIONS.md mục 3). Sửa ở đây, ghi lý do vào docs/DECISIONS.md."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = REPO_ROOT / "data" / "raw"
DATA_ANNOTATIONS = REPO_ROOT / "data" / "annotations"
RESULTS_DIR = REPO_ROOT / "experiments" / "results"

CONDITIONS = ("nen-don-gian", "nen-phuc-tap", "thieu-sang", "nghieng-manh", "che-goc")

RANDOM_SEED = 42
MAX_STORED_LONG_SIDE = 1600   # px, ảnh lưu trong data/raw

WORK_LONG_SIDE = 800          # px, thu nhỏ trước khi detect rồi nhân toạ độ về ảnh gốc
BLUR_KSIZE = (5, 5)
CANNY_LOW, CANNY_HIGH = 50, 150
APPROX_EPS_RATIO = 0.02       # epsilon = ratio * chu vi contour
MIN_AREA_RATIO = 0.20         # contour tài liệu chiếm >= 20% diện tích ảnh
MORPH_KERNEL = (5, 5)         # ellipse
MORPH_CLOSE_ITER = 2
ADAPTIVE_BLOCK, ADAPTIVE_C = 35, 10

CORRECT_TOL_RATIO = 0.02      # đúng khi sai số góc TB <= 2% độ dài đường chéo ảnh
