# Tasks

Phân công dưới đây là **đề xuất**, nhóm duyệt/đổi trong tuần đầu. Trạng thái: `todo` / `doing` / `done`.

Phân luồng: **A** = phương pháp 1 + warp + enhance · **B** = phương pháp 2 + cảnh báo chất lượng · **C** = dữ liệu + nhãn + đánh giá + GUI.

| ID | Việc | Người | Hạn | Checklist xong | Trạng thái |
|---|---|---|---|---|---|
| T01 | Chốt đề tài trong sheet đăng ký (tên + nội dung) | cả nhóm | 29/11 | Sheet đã cập nhật đúng tên đã chốt | todo |
| T02 | Dựng khung repo, quy trình, nhánh | Phi | 29/11 | Có cấu trúc, docs, nhánh `dev/*` | doing |
| T03 | Chụp và resize ảnh (≥ 40 ảnh, 5 điều kiện) | Việt (+ cả nhóm chụp) | 6/12 | Ảnh trong `data/raw/`, đặt tên đúng quy ước | todo |
| T04 | Phương pháp 1: Canny + Contour + approxPolyDP | Phi | 6/12 | `detect_canny.detect` + test + ảnh minh hoạ | todo |
| T05 | Perspective warp | Phi | 6/12 | `warp.warp` + test với góc biết trước | todo |
| T06 | Phương pháp 2: Otsu/Adaptive + Morphology + Hull | Huấn | 13/12 | `detect_threshold.detect` + test + ảnh minh hoạ | todo |
| T07 | Công cụ đánh dấu 4 góc chuẩn (click chuột → JSON) | Việt | 13/12 | Chạy được, đã gán nhãn toàn bộ ảnh | todo |
| T08 | Đánh giá: tỉ lệ đúng, sai số góc, bảng theo điều kiện | Việt | 20/12 | `experiments/run_compare.py` sinh bảng + biểu đồ | todo |
| T09 | Cảnh báo chất lượng ảnh (mờ, quá xa, lệch) | Huấn | 20/12 | `quality.check` + ngưỡng có cơ sở từ dữ liệu | todo |
| T10 | Enhance sau scan: cân bằng histogram/CLAHE, threshold | Phi | 20/12 | `enhance.enhance`, so sánh trước/sau | todo |
| T11 | GUI hai cửa sổ | Việt | 27/12 | Chọn ảnh, chọn phương pháp, xem kết quả | todo |
| T12 | (tuỳ chọn) Phương pháp 3: Hough Line | ai còn thời gian | 27/12 | Chỉ làm nếu T04–T11 xong | todo |
| T13 | **Dừng thêm tính năng** | cả nhóm | 27/12 | Không merge tính năng mới sau mốc này | todo |
| T14 | Viết báo cáo | Phi (chủ biên) + mỗi người viết phần mình | 3/1 | Có đủ mục, hình/bảng từ `experiments/` | todo |
| T15 | Slide + demo thử | cả nhóm | 8/1 | Chạy demo trọn vẹn 1 lần | todo |
| T16 | Tuần đệm: sửa lỗi, luyện hỏi đáp | cả nhóm | 10/1 | Mỗi người giải thích được phần mình | todo |

Thi/nộp: **12/01/2027** (hình thức chính xác: chưa rõ, cần hỏi GV).
