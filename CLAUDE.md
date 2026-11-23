# CLAUDE.md — Document Scanner

Bài tập lớn môn Nhập môn xử lý ảnh (2 tín), nhóm 15. Thi/nộp: **12/01/2027**. GV không xem repo; được dùng AI thoải mái, nhưng mỗi thành viên phải tự giải thích được phần mình làm.

## Mục tiêu
Ứng dụng quét giấy tờ; trọng tâm so sánh các phương pháp phát hiện 4 góc tài liệu trong điều kiện chụp khó. Chi tiết: `docs/spec.md`.

## Cấu trúc
`src/snapdocs/` (code) · `app/` (GUI) · `data/` (ảnh + nhãn góc) · `experiments/` (so sánh) · `report/` · `docs/` · `legacy/labs/` (không sửa).

## Lệnh
- Cài: `pip install -r requirements.txt`
- Test: `python -m pytest tests -q`
- Chạy so sánh: `python experiments/run_compare.py` (khi đã có)

## Bất biến
- Chỉ dùng OpenCV/NumPy/Matplotlib/Tkinter (+ pytest). Không thêm dependency nặng (deep learning) nếu chưa bàn.
- Phương pháp 1–2 là bắt buộc; Hough là tuỳ chọn. Không làm OCR (nhóm khác đã làm).
- Mỗi phương pháp: một hàm `detect(image) -> 4 điểm | None` (xem `src/snapdocs/__init__.py`).
- Không commit ảnh gốc > 1600 px, không commit `.venv`, không commit bí mật/thông tin cá nhân (repo công khai).
- Mỗi người làm trên nhánh `dev/<tên>` và **phải push nhánh đó cuối mỗi buổi làm việc** (kể cả WIP); vào `main` qua PR, merge commit. Quy trình: `docs/PROCESS.md`.

## Đọc khi cần
`docs/CONVENTIONS.md` (môi trường, thông số, quy ước; hằng số ở `src/snapdocs/config.py`) · `docs/DECISIONS.md` · `docs/PROCESS.md` · `docs/TASKS.md` · `docs/members/<tên>.md` · `docs/reference/yeu-cau-giang-vien.md`
