# Dữ liệu

- `raw/`: ảnh tự chụp, đã resize cạnh dài ≤ 1600 px. Tên: `<điều-kiện>_<số>.jpg`.
- `annotations/`: nhãn 4 góc, `<tên-ảnh>.json`, dạng `{"corners": [[x,y],[x,y],[x,y],[x,y]]}` theo thứ tự trên-trái, trên-phải, dưới-phải, dưới-trái.
- `original/` (không commit): ảnh gốc từ điện thoại.

Điều kiện: `nen-don-gian`, `nen-phuc-tap`, `thieu-sang`, `nghieng-manh`, `che-goc`. Mục tiêu 40–60 ảnh, mỗi điều kiện ≥ 8 ảnh.
Không chụp giấy tờ thật của người khác; dùng giấy mẫu hoặc che thông tin cá nhân.
