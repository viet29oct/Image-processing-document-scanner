# Việt — luồng C (đề xuất)

**Nhánh:** `dev/viet` (chủ repo)

## Phụ trách
- Chụp và quản lý dữ liệu (T03), công cụ đánh dấu 4 góc chuẩn (T07)
- Đánh giá và so sánh → `experiments/run_compare.py`, `src/snapdocs/evaluate.py` (T08)
- GUI hai cửa sổ → `app/` (T11)

## Cần đọc/học
- Tkinter cơ bản (hoặc OpenCV HighGUI nếu muốn nhẹ hơn)
- Cách tính IoU hoặc khoảng cách giữa 4 góc dự đoán và góc chuẩn
- `docs/reference/yeu-cau-giang-vien.md` (mẫu giao diện GV gợi ý)

## Cách làm
1. Chốt quy ước đặt tên và định dạng nhãn (xem `docs/PROCESS.md` mục 6) trước khi nhóm chụp nhiều.
2. Công cụ nhãn: mở ảnh, click 4 góc theo thứ tự, lưu JSON.
3. `run_compare.py` chạy mọi phương pháp trên mọi ảnh, xuất bảng theo điều kiện × phương pháp.
4. GUI: trái danh sách ảnh + nút phương pháp, phải ảnh kết quả; không cần cầu kỳ.

## Phải giải thích được khi thi
Chia điều kiện chụp thế nào và vì sao; "đúng" nghĩa là gì (ngưỡng sai số bao nhiêu px); kết quả tốt/xấu ở điều kiện nào.

## Định nghĩa xong
Xem mục 3 trong `docs/PROCESS.md`.
