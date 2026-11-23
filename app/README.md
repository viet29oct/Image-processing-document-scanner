# app/

GUI hai cửa sổ (T11). Trái: danh sách ảnh + nút chọn phương pháp. Phải: ảnh kết quả (có thể thêm ảnh gốc và cảnh báo chất lượng). Mỗi thuật toán là một module trong `src/snapdocs/`, GUI chỉ gọi `detect`, `warp`, `enhance`, `quality`.
