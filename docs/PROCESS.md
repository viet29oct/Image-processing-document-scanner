# Quy trình chung

Bản nhẹ cho môn 2 tín. Mục đích: ai cũng biết mình làm gì, làm xong thế nào, và trả lời được khi thầy cô hỏi.

## 1. Nhánh và PR
- `main`: luôn chạy được. Không commit thẳng.
- Mỗi người một nhánh dài hạn: `dev/huan`, `dev/phi`, `dev/viet`. Việc nhỏ có thể tách `feat/<tên-việc>` từ nhánh của mình.
- Vào `main` bằng PR, ít nhất **1 người khác** xem qua (xem nhanh 5–10 phút, không cần review nghiêm).
- Merge kiểu squash; commit message ngắn, tiếng Việt hoặc Anh đều được: `detect: thêm phương pháp Canny+Contour`.
- Trước khi mở PR: `python -m pytest tests -q` qua, không còn file rác (ảnh nặng, `.venv`).

## 2. Task và checklist
- Việc nằm trong [TASKS.md](TASKS.md): ID, người làm, hạn, checklist hoàn thành, trạng thái (`todo` / `doing` / `done`).
- Nhận việc: đổi trạng thái thành `doing` và ghi tên. Xong: tích hết checklist rồi `done`.
- Việc mới phát sinh: thêm dòng vào TASKS.md qua PR nhỏ, không tự thêm việc vào nhánh người khác.

## 3. Định nghĩa "xong" cho một phương pháp
- [ ] Có hàm `detect(image) -> 4 điểm | None` đúng chữ ký.
- [ ] Có test trên ảnh tổng hợp.
- [ ] Đã chạy được trên bộ ảnh thật, có ảnh minh hoạ thành công và thất bại.

## 4. Cuộc họp và liên lạc
- Họp ngắn 15 phút mỗi tuần (hoặc nhắn nhóm): tuần trước xong gì, tuần này làm gì, vướng gì.
- Mốc cứng: **27/12/2026 dừng thêm tính năng**, sau đó chỉ sửa lỗi và viết báo cáo.

## 5. Dùng AI
- Được dùng thoải mái để viết code, giải thích, soạn báo cáo. Agent mẫu nằm ở `.claude/agents/`.
- Quy tắc: **tự chạy và tự đọc lại** những gì AI viết; không nộp thứ mình không giải thích được. GV từng hỏi sâu "lấy đặc trưng thế nào", "vì sao dùng cách này".
- Không dán thông tin cá nhân (mã sinh viên, email) vào prompt hay commit vào repo (repo công khai).

## 6. Dữ liệu
- Chụp bằng điện thoại, resize cạnh dài ≤ 1600 px trước khi commit vào `data/raw/`. Ảnh gốc để ở `data/original/` (đã bị ignore).
- Đặt tên: `<điều-kiện>_<số>.jpg`, ví dụ `nen-phuc-tap_012.jpg`. Điều kiện: `nen-don-gian`, `nen-phuc-tap`, `thieu-sang`, `nghieng-manh`, `che-goc`.
- Nhãn góc: `data/annotations/<tên-ảnh>.json` (4 điểm theo thứ tự trên-trái, trên-phải, dưới-phải, dưới-trái).
- Không chụp giấy tờ thật của người khác; dùng giấy tờ mẫu hoặc che thông tin.

## 7. Cuối dự án
- Điền "Kết quả / bàn giao" trong `docs/spec.md`.
- Mỗi người tự kiểm tra: chạy lại được từ repo sạch theo README, và giải thích được phần của mình.
