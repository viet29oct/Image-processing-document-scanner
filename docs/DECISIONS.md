# Nhật ký quyết định

Mỗi quyết định 3–4 dòng, thêm vào cuối. Mẫu: **ngày — quyết định** · lý do · hệ quả.

**2026-11-23 — Chốt đề tài: ứng dụng quét giấy tờ, trọng tâm so sánh phương pháp phát hiện 4 góc** · khác nhóm 12 ở phương pháp/dữ liệu/mục đích; nhóm 10 làm OCR nên bỏ OCR · tên đề tài ghi trong `docs/spec.md`.

**2026-11-23 — Thứ tự 4 góc: trên-trái, trên-phải, dưới-phải, dưới-trái; toạ độ (x, y) float32** · để mọi phương pháp, nhãn và đánh giá dùng chung · cài trong `order_points`.

**2026-11-23 — Thông số khởi điểm và tiêu chí "đúng" (sai số góc ≤ 2% đường chéo)** · giá trị khởi điểm, chưa kiểm chứng trên dữ liệu · xem `docs/CONVENTIONS.md` mục 3; chỉnh sau khi có bộ ảnh và ghi lý do tại đây.
