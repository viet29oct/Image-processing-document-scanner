# SnapDocs — Image Processing (Nhập môn xử lý ảnh, nhóm 15, D18CNPM1)

**Đề tài:** Xây dựng ứng dụng quét và hiệu chỉnh phối cảnh ảnh giấy tờ với phát hiện biên tài liệu trong điều kiện chụp phức tạp.

Bài toán: từ ảnh chụp giấy tờ/văn bản bằng điện thoại (bị nghiêng, nền phức tạp, thiếu sáng, che góc), tìm 4 góc tài liệu rồi nắn phẳng bằng biến đổi phối cảnh. Trọng tâm là **so sánh các phương pháp phát hiện 4 góc**:

1. Canny + Contour + approxPolyDP
2. Otsu/Adaptive threshold + Morphology + Convex Hull
3. (mở rộng, nếu còn thời gian) Hough Line + giao điểm

Đánh giá trên bộ ảnh tự chụp theo điều kiện: tỉ lệ tìm đúng 4 góc, sai số góc (pixel).

## Bắt đầu nhanh

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `src/snapdocs/` | Code chính (mỗi phương pháp một module) |
| `app/` | Giao diện (GUI hai cửa sổ: ảnh vào / kết quả) |
| `data/raw/` | Ảnh tự chụp (đã resize ≤ 1600 px) |
| `data/annotations/` | Toạ độ 4 góc chuẩn đánh dấu tay |
| `experiments/` | Script chạy so sánh, bảng và biểu đồ kết quả |
| `report/` | Báo cáo, slide |
| `docs/` | Quy trình, task, lịch, hướng dẫn từng thành viên |
| `legacy/labs/` | Bài lab đã làm trước đó (Ch2–Ch3), chỉ để tham khảo |

## Đọc tiếp

- Quy trình chung: [docs/PROCESS.md](docs/PROCESS.md)
- Việc cần làm: [docs/TASKS.md](docs/TASKS.md)
- Đặc tả đề tài: [docs/spec.md](docs/spec.md)
- Lịch: [docs/SCHEDULE.md](docs/SCHEDULE.md)
- Hướng dẫn từng người: [docs/members/](docs/members/)
