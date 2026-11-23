# Quy chuẩn: môi trường, thông số, quy ước

Mục đích: ba người chạy cùng một kết quả trên máy khác nhau, và số liệu so sánh giữa các phương pháp là công bằng. Giá trị đánh dấu **(khởi điểm)** được phép chỉnh, nhưng phải ghi lý do vào [DECISIONS.md](DECISIONS.md) và sửa ở `src/snapdocs/config.py`, không sửa rải rác trong code.

## 1. Môi trường

| Mục | Quy chuẩn |
|---|---|
| Hệ điều hành | Windows 10/11 (macOS/Linux chạy được nhưng chưa kiểm tra) |
| Python | **3.12** (đã chạy trên 3.12.10). 3.10–3.12 dự kiến chạy được, chưa kiểm chứng |
| Môi trường ảo | `.venv/` ở gốc repo, không commit |
| Cài đặt | `python -m venv .venv` → `.venv\Scripts\activate` → `pip install -r requirements.txt` |
| Thư viện được phép | OpenCV (`opencv-python`), NumPy, Matplotlib, Tkinter (có sẵn trong Python), pytest |
| Đã thử với | opencv-python 5.0.0, numpy 2.5.2, matplotlib 3.11.1, pytest 9.2.0 |
| Không dùng | Deep learning, OCR, thư viện nặng khác. Muốn thêm thư viện: ghi vào DECISIONS.md và `requirements.txt` trong cùng một PR |
| Chạy test | `python -m pytest tests -q` từ gốc repo |
| Định dạng file | UTF-8, kết thúc dòng LF (có `.gitattributes`, `.editorconfig`) |

Gặp khác biệt giữa các phiên bản OpenCV: ghi lại (phiên bản + hành vi) vào DECISIONS.md.

## 2. Quy ước ảnh và hình học

- Đọc ảnh bằng `cv2.imread` → mảng **BGR, `uint8`**, shape `(H, W, 3)`. Chỉ đổi sang RGB ngay trước khi hiển thị bằng Matplotlib. Ảnh xám: `(H, W)`, `uint8`.
- Điểm là **(x, y)** (x theo cột, y theo hàng), kiểu `float32`. Bộ 4 góc: shape `(4, 2)`, thứ tự **trên-trái, trên-phải, dưới-phải, dưới-trái** (dùng `order_points`).
- `detect(image) -> (4, 2) float32 | None`. Toạ độ trả về **theo ảnh đầu vào gốc**, không theo ảnh đã thu nhỏ.
- Ảnh phải được xoay đúng chiều khi đọc (`cv2.imread` mặc định áp EXIF); không tự xoay thêm.
- Ảnh trong `data/raw/`: cạnh dài ≤ **1600 px**, JPEG chất lượng ≥ 90.

## 3. Thông số khởi điểm (đặt trong `src/snapdocs/config.py`)

Tất cả phương pháp phải dùng chung cùng điều kiện đầu vào để so sánh công bằng.

| Tham số | Giá trị (khởi điểm) | Ghi chú |
|---|---|---|
| `WORK_LONG_SIDE` | 800 px | Thu nhỏ cạnh dài về 800 trước khi detect, rồi nhân toạ độ về lại ảnh gốc |
| `BLUR_KSIZE` | (5, 5) | Gaussian trước Canny/threshold |
| `CANNY_LOW/HIGH` | 50 / 150 | Phương pháp 1; có thể thử ngưỡng tự động theo trung vị, ghi vào báo cáo |
| `APPROX_EPS_RATIO` | 0.02 | `epsilon = 0.02 × chu vi contour` cho `approxPolyDP` |
| `MIN_AREA_RATIO` | 0.20 | Contour tài liệu phải chiếm ≥ 20% diện tích ảnh |
| `MORPH_KERNEL` | ellipse 5×5, 2 lần closing | Phương pháp 2 |
| `ADAPTIVE_BLOCK / C` | 35 / 10 | Adaptive threshold (block lẻ) |
| `CORRECT_TOL_RATIO` | 0.02 | Một kết quả "đúng" khi sai số góc trung bình ≤ 2% độ dài đường chéo ảnh |
| `RANDOM_SEED` | 42 | Mọi chỗ có ngẫu nhiên |

Ngưỡng cảnh báo chất lượng (mờ, quá xa, lệch) **không đặt trước**: lấy từ phân bố trên bộ ảnh thật rồi ghi vào DECISIONS.md.

## 4. Chụp dữ liệu

- Điện thoại, giấy A4 hoặc giấy mẫu, **không chụp giấy tờ thật của người khác**.
- 5 điều kiện: `nen-don-gian`, `nen-phuc-tap`, `thieu-sang`, `nghieng-manh`, `che-goc`; mỗi điều kiện ≥ 8 ảnh, tổng 40–60.
- Tên file: `<dieu-kien>_<NNN>.jpg` (3 chữ số, ví dụ `thieu-sang_004.jpg`). Không dấu, không dấu cách.
- Nhãn: `data/annotations/<ten-anh-khong-duoi>.json`, dạng `{"corners": [[x,y],[x,y],[x,y],[x,y]]}`, toạ độ theo ảnh đã resize trong `data/raw/`, đúng thứ tự mục 2.
- Ảnh gốc từ điện thoại để ở `data/original/` (đã ignore).

## 5. Đánh giá

- Một ảnh chưa có nhãn thì bỏ khỏi thống kê và nêu số ảnh bị bỏ.
- `detect` trả `None` được tính là **thất bại** (không bỏ khỏi mẫu).
- Báo cáo mỗi (phương pháp × điều kiện): số ảnh, tỉ lệ đúng, sai số góc trung bình (px, chỉ tính trên ảnh có kết quả).
- Kết quả ghi vào `experiments/results/` dạng CSV có các cột: `image, condition, method, found, error_px, correct`.
- Mọi số trong báo cáo phải sinh từ `experiments/run_compare.py`, không nhập tay.

## 6. Code

- PEP 8, độ dài dòng ≤ 100. Type hint cho hàm công khai.
- Tên hàm/biến/file: tiếng Anh, `snake_case`. Docstring và comment: tiếng Việt, ngắn.
- Đường dẫn: dùng `pathlib` tính từ gốc repo; không viết đường dẫn tuyệt đối (ngoại lệ: `legacy/`).
- `src/` không `print`, không `cv2.imshow`; hiển thị chỉ ở `app/` và `experiments/`.
- Mỗi module có test; test dùng ảnh tổng hợp có góc biết trước, không phụ thuộc ảnh chụp.

## 7. Git và tài liệu

- Commit: `<phạm vi>: <mô tả ngắn>`, ví dụ `detect: thêm Canny + Contour`; một commit một ý.
- Nhánh: xem [PROCESS.md](PROCESS.md). Không commit ảnh > 1600 px, `.venv`, file zip/video.
- Repo công khai: không đưa mã sinh viên, email, số điện thoại, ảnh giấy tờ thật.
- Tài liệu và báo cáo: tiếng Việt, giữ thuật ngữ kỹ thuật tiếng Anh; trích dẫn APA 7 (trừ khi khoa yêu cầu khác).
