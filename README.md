# SnapDocs — Image Processing (Nhập môn xử lý ảnh, nhóm 15, D18CNPM1)

**Đề tài:** Xây dựng ứng dụng quét và hiệu chỉnh phối cảnh ảnh giấy tờ với phát hiện biên tài liệu trong điều kiện chụp phức tạp.

Từ ảnh chụp giấy tờ/văn bản bằng điện thoại (nghiêng, nền phức tạp, thiếu sáng, che góc), tìm 4 góc tài liệu rồi nắn phẳng bằng biến đổi phối cảnh. Trọng tâm là **so sánh các phương pháp phát hiện 4 góc**:

1. Canny + Contour + approxPolyDP
2. Otsu/Adaptive threshold + Morphology + Convex Hull
3. *(mở rộng, nếu còn thời gian)* Hough Line + giao điểm

Đánh giá trên bộ ảnh tự chụp theo điều kiện: tỉ lệ tìm đúng 4 góc, sai số góc (px).

**Thi/nộp: 12/01/2027.** Dừng thêm tính năng: **27/12/2026**. Chi tiết lịch: [docs/SCHEDULE.md](docs/SCHEDULE.md).

## Mục lục

1. [Bắt đầu nhanh](#1-bắt-đầu-nhanh)
2. [Cấu trúc thư mục](#2-cấu-trúc-thư-mục)
3. [Quy trình chung](#3-quy-trình-chung)
4. [Môi trường, thông số, quy ước](#4-môi-trường-thông-số-quy-ước)
5. [Việc cần làm (checklist tổng)](#5-việc-cần-làm-checklist-tổng)
6. [Hướng dẫn và việc cụ thể của từng người](#6-hướng-dẫn-và-việc-cụ-thể-của-từng-người)
7. [Agent hỗ trợ (AI)](#7-agent-hỗ-trợ-ai)
8. [Yêu cầu của giảng viên và câu hỏi còn mở](#8-yêu-cầu-của-giảng-viên-và-câu-hỏi-còn-mở)
9. [Tài liệu chi tiết](#9-tài-liệu-chi-tiết)

---

## 1. Bắt đầu nhanh

```powershell
git clone https://github.com/viet29oct/SnapDocs.git
cd SnapDocs
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest tests -q
```

Chuyển sang nhánh của mình: `git checkout dev/huan` (hoặc `dev/phi`, `dev/viet`).

**Bắt đầu mỗi buổi làm việc (3 bước):**
1. Xem [docs/TASKS.md](docs/TASKS.md) và nhật ký tiến độ gần nhất (nếu có) để biết việc đã đổi gì.
2. Cập nhật nhánh của mình: `git fetch origin` rồi `git merge origin/main`.
3. Đối soát với [docs/spec.md](docs/spec.md) và [docs/CONVENTIONS.md](docs/CONVENTIONS.md) trước khi viết code.

## 2. Cấu trúc thư mục

| Thư mục | Nội dung |
|---|---|
| `src/snapdocs/` | Code chính, mỗi phương pháp một module (`detect_canny`, `detect_threshold`, `warp`, `enhance`, `quality`, `evaluate`, `config`) |
| `app/` | Giao diện (GUI hai cửa sổ: trái danh sách ảnh + nút chức năng, phải kết quả) |
| `data/raw/` | Ảnh tự chụp, đã resize cạnh dài ≤ 1600 px |
| `data/annotations/` | Toạ độ 4 góc chuẩn đánh dấu tay (JSON) |
| `experiments/` | Script chạy so sánh, `results/` (CSV + PNG), `failures/` (ảnh thất bại) |
| `report/` | Báo cáo, slide |
| `tests/` | Test (`python -m pytest tests -q`) |
| `docs/` | Quy trình, task, lịch, quy chuẩn, hướng dẫn từng người |
| `legacy/labs/` | Bài lab Ch2–Ch3 đã làm trước đó, chỉ để tham khảo, không sửa |
| `.claude/agents/` | Agent AI hỗ trợ |

## 3. Quy trình chung

Bản nhẹ cho môn 2 tín. Đầy đủ: [docs/PROCESS.md](docs/PROCESS.md).

**Nhánh và PR**
- `main` luôn chạy được; không commit thẳng, vào `main` bằng PR và ít nhất **1 người khác** xem nhanh (5–10 phút).
- Mỗi người một nhánh dài hạn: `dev/huan`, `dev/phi`, `dev/viet`. Việc nhỏ có thể tách `feat/<tên-việc>`.
- Commit: `<phạm vi>: <mô tả ngắn>` (ví dụ `detect: thêm Canny + Contour`), một commit một ý.
- Trước khi mở PR: `python -m pytest tests -q` qua, không lẫn ảnh nặng, `.venv`, thông tin cá nhân.

**Task**
- Việc nằm trong [docs/TASKS.md](docs/TASKS.md). Nhận việc: đổi trạng thái `doing` + ghi tên. Xong: tích hết checklist rồi `done`.
- Việc mới phát sinh: thêm dòng vào TASKS.md qua PR nhỏ, không tự thêm việc vào nhánh người khác.

**"Xong" cho một phương pháp**
- [ ] Có hàm `detect(image) -> 4 điểm | None` đúng chữ ký
- [ ] Có test trên ảnh tổng hợp
- [ ] Chạy được trên bộ ảnh thật, có ảnh minh hoạ thành công và thất bại

**Họp và mốc**
- Họp 15 phút mỗi tuần (hoặc nhắn nhóm): tuần trước xong gì, tuần này làm gì, vướng gì.
- **27/12/2026 dừng thêm tính năng**; sau đó chỉ sửa lỗi và viết báo cáo.

**Dùng AI:** được dùng thoải mái, nhưng tự chạy và tự đọc lại; không nộp thứ mình không giải thích được. Không dán mã sinh viên, email vào prompt hay repo (repo công khai).

## 4. Môi trường, thông số, quy ước

Đầy đủ: [docs/CONVENTIONS.md](docs/CONVENTIONS.md). Hằng số nằm ở [src/snapdocs/config.py](src/snapdocs/config.py) (sửa ở đó, ghi lý do vào [docs/DECISIONS.md](docs/DECISIONS.md)).

**Môi trường**

| Mục | Quy chuẩn |
|---|---|
| Hệ điều hành | Windows 10/11 |
| Python | 3.12 (đã chạy 3.12.10; 3.10–3.12 dự kiến chạy được, chưa kiểm chứng) |
| Môi trường ảo | `.venv/` ở gốc repo, không commit |
| Thư viện | OpenCV, NumPy, Matplotlib, Tkinter, pytest. Không deep learning, không OCR |
| Đã thử với | opencv-python 5.0.0, numpy 2.5.2, matplotlib 3.11.1, pytest 9.2.0 |
| File | UTF-8, kết thúc dòng LF |

**Quy ước ảnh và hình học**
- Ảnh BGR `uint8` (`cv2.imread`); chỉ đổi RGB khi hiển thị bằng Matplotlib.
- Điểm là `(x, y)` `float32`; bộ 4 góc shape `(4, 2)`, thứ tự **trên-trái, trên-phải, dưới-phải, dưới-trái** (`order_points`).
- `detect` trả toạ độ theo **ảnh gốc**, trả `None` nếu không tìm được (tính là thất bại khi đánh giá).

**Thông số khởi điểm** (giá trị khởi điểm, chưa kiểm chứng trên dữ liệu thật)

| Tham số | Giá trị |
|---|---|
| `WORK_LONG_SIDE` | 800 px (thu nhỏ trước khi detect) |
| `BLUR_KSIZE` | (5, 5) |
| `CANNY_LOW/HIGH` | 50 / 150 |
| `APPROX_EPS_RATIO` | 0.02 × chu vi contour |
| `MIN_AREA_RATIO` | 0.20 (contour ≥ 20% diện tích ảnh) |
| `MORPH_KERNEL` | ellipse 5×5, closing 2 lần |
| `ADAPTIVE_BLOCK / C` | 35 / 10 |
| `CORRECT_TOL_RATIO` | 0.02 (đúng khi sai số góc TB ≤ 2% đường chéo ảnh) |
| `RANDOM_SEED` | 42 |

Ngưỡng cảnh báo chất lượng (mờ, quá xa, lệch) **chưa đặt**: lấy từ phân bố trên ảnh thật rồi ghi vào DECISIONS.md.

**Dữ liệu**
- 5 điều kiện: `nen-don-gian`, `nen-phuc-tap`, `thieu-sang`, `nghieng-manh`, `che-goc`; mỗi điều kiện ≥ 8 ảnh, tổng 40–60.
- Tên file: `<dieu-kien>_<NNN>.jpg` (ví dụ `thieu-sang_004.jpg`). Ảnh gốc để `data/original/` (đã ignore).
- Nhãn: `data/annotations/<ten-anh>.json` dạng `{"corners": [[x,y],[x,y],[x,y],[x,y]]}`.
- Không chụp giấy tờ thật của người khác; dùng giấy mẫu hoặc che thông tin.

**Đánh giá:** CSV cột `image, condition, method, found, error_px, correct`; mọi số trong báo cáo phải sinh từ `experiments/run_compare.py`.

**Code:** PEP 8, dòng ≤ 100, tên tiếng Anh `snake_case`, comment tiếng Việt, `pathlib` (không đường dẫn tuyệt đối), `src/` không `print`/`imshow`.

## 5. Việc cần làm (checklist tổng)

Phân công là **đề xuất**, nhóm duyệt/đổi trong tuần đầu. Bảng đầy đủ (người, hạn, trạng thái): [docs/TASKS.md](docs/TASKS.md).

**Việc chung**
- [ ] T01 — Cập nhật sheet đăng ký của lớp theo tên đề tài đã chốt (hạn 29/11)
- [x] T02 — Dựng khung repo, quy trình, quy chuẩn, nhánh (Phi, xong)
- [ ] T12 — *(tuỳ chọn)* Phương pháp 3: Hough Line, chỉ làm nếu T04–T11 xong (hạn 27/12)
- [ ] T13 — Dừng thêm tính năng (27/12)
- [ ] T15 — Slide + demo thử (hạn 8/1)
- [ ] T16 — Tuần đệm: sửa lỗi, luyện hỏi đáp (hạn 10/1)

**Vai trò và công việc chính** (chi tiết ở mục 6)

| Người | Công việc chính (code) | Vai trò báo cáo |
|---|---|---|
| **Phi** | T04 Canny + Contour, T05 warp, T10 enhance | Viết phần kỹ thuật của mình (T14a), gửi Huấn |
| **Huấn** | T06 Otsu/Adaptive + Morphology + Hull, T09 cảnh báo chất lượng | **Viết báo cáo chính** (T14b) |
| **Việt** | T03 dữ liệu, T07 công cụ nhãn, T08 đánh giá, T11 GUI | **Tổng hợp và duyệt báo cáo** (T14c), làm slide (T15) |

**Quy trình báo cáo:** mỗi người viết phần kỹ thuật của mình (29/12) → Huấn ghép và viết báo cáo chính (3/1) → Việt tổng hợp, kiểm số liệu, duyệt và chốt bản nộp (6/1) → Việt làm slide, cả nhóm demo thử (8/1).

**Mốc theo tuần:** 29/11 chốt đề tài + khung · 6/12 PP1 + warp + ảnh chụp xong · 13/12 PP2 + công cụ nhãn · 20/12 đánh giá + cảnh báo chất lượng + enhance · 27/12 GUI + dừng tính năng · 3/1 báo cáo · 10/1 đệm.

## 6. Hướng dẫn và việc cụ thể của từng người

Mỗi người có file riêng ở [docs/members/](docs/members/): [phi.md](docs/members/phi.md), [huan.md](docs/members/huan.md), [viet.md](docs/members/viet.md). Tóm tắt:

### Phi — luồng A (nhánh `dev/phi`)
Phương pháp 1, nắn phẳng, tăng cường ảnh. Không làm tổng hợp báo cáo; chỉ viết phần kỹ thuật của mình.
- [ ] **T04 (6/12)** `src/snapdocs/detect_canny.py`: Canny → contour → approxPolyDP → 4 góc; test + ảnh minh hoạ
- [ ] **T05 (6/12)** `src/snapdocs/warp.py`: nắn phẳng bằng `getPerspectiveTransform` + `warpPerspective`; test với góc biết trước
- [ ] **T10 (20/12)** `src/snapdocs/enhance.py`: cân bằng histogram, CLAHE, Otsu, Adaptive; so sánh trước/sau
- [ ] **T14a (29/12)** Viết phần kỹ thuật PP1, warp, enhance (đúng với code, số liệu từ `experiments/`), gửi Huấn
- Đọc/học: slide Ch4 (Canny, contour), Ch3 (histogram); tự học approxPolyDP, perspective, CLAHE
- Phải giải thích được: vì sao Canny rồi mới contour; chọn ngưỡng Canny thế nào; epsilon của approxPolyDP; ma trận phối cảnh 3×3 từ 4 cặp điểm

### Huấn — luồng B (nhánh `dev/huan`)
Phương pháp 2, cảnh báo chất lượng ảnh, **viết báo cáo chính**.
- [ ] **T06 (13/12)** `src/snapdocs/detect_threshold.py`: làm xám → làm mờ → Otsu/Adaptive → closing → contour lớn nhất → convex hull → 4 điểm; test + ảnh minh hoạ
- [ ] **T09 (20/12)** `src/snapdocs/quality.py`: cảnh báo mờ (phương sai Laplacian), quá xa (tỉ lệ diện tích), quá lệch (góc tứ giác); ngưỡng lấy từ số liệu thật
- [ ] **T14a (29/12)** Viết phần kỹ thuật PP2 + chất lượng ảnh
- [ ] **T14b (3/1)** **Báo cáo chính**: xương sống, ghép phần của Phi và Việt, văn phong thống nhất; bản nháp đủ mục
- Đọc/học: slide Ch2 (threshold, Adaptive, Otsu); tự học morphology, `convexHull`, `Laplacian().var()`
- Phải giải thích được: Otsu/Adaptive hợp điều kiện nào; closing làm gì với viền đứt; convex hull khác contour thường ở đâu; ngưỡng cảnh báo lấy từ đâu

### Việt — luồng C (nhánh `dev/viet`, chủ repo)
Dữ liệu, nhãn, đánh giá, giao diện, **tổng hợp và duyệt báo cáo**.
- [ ] **T03 (6/12)** Chụp và resize ≥ 40 ảnh theo 5 điều kiện (cả nhóm cùng chụp), đặt tên đúng quy ước
- [ ] **T07 (13/12)** Công cụ đánh dấu 4 góc (click chuột → JSON); gán nhãn toàn bộ ảnh
- [ ] **T08 (20/12)** `experiments/run_compare.py` + `src/snapdocs/evaluate.py`: bảng tỉ lệ đúng và sai số góc theo (điều kiện × phương pháp), biểu đồ
- [ ] **T11 (27/12)** `app/`: GUI hai cửa sổ (chọn ảnh, chọn phương pháp, xem kết quả)
- [ ] **T14a (29/12)** Viết phần dữ liệu, đánh giá, GUI
- [ ] **T14c (6/1)** **Tổng hợp và duyệt báo cáo**: kiểm mọi số với `experiments/results/`, đối chiếu spec và code, chốt bản nộp
- [ ] **T15 (8/1)** Làm slide từ báo cáo; cả nhóm demo thử
- Đọc/học: Tkinter cơ bản; cách tính sai số giữa 4 góc dự đoán và chuẩn
- Phải giải thích được: chia điều kiện chụp thế nào, vì sao; "đúng" nghĩa là gì (ngưỡng bao nhiêu); kết quả tốt/xấu ở điều kiện nào

## 7. Agent hỗ trợ (AI)

Nằm ở [.claude/agents/](.claude/agents/):

| Agent | Dùng khi |
|---|---|
| `cv-implementer` | Viết/sửa module OpenCV theo đúng chữ ký (Phi, Huấn) |
| `experiment-runner` | Chạy so sánh, xuất bảng và biểu đồ (Việt) |
| `report-writer` | Soạn báo cáo từ số liệu thật (Huấn viết chính; Phi, Việt viết phần mình; Việt dùng để kiểm số liệu khi duyệt) |
| `light-reviewer` | Review nhanh PR trước khi vào `main` (cả nhóm) |

## 8. Yêu cầu của giảng viên và câu hỏi còn mở

Tóm tắt từ buổi hướng dẫn 23/11/2026: [docs/reference/yeu-cau-giang-vien.md](docs/reference/yeu-cau-giang-vien.md).

**Đã rõ:** không bắt buộc ứng dụng hoàn chỉnh (nêu rõ cách làm và demo được là ổn; làm app thì được đánh giá cao); giao diện gợi ý hai cửa sổ; tên đề tài không được giống nhóm khác (khác phương pháp, dữ liệu hoặc mục đích); dữ liệu tự chụp hoặc Kaggle.

**Chưa rõ, cần hỏi GV:** hình thức thi 12/01 (báo cáo/demo/vấn đáp), hạn nộp, số trang và mẫu báo cáo, thang điểm, có nộp code không, có chấm riêng từng người không, quy định ghi rõ việc dùng AI, tên đề tài đã đủ khác nhóm 12 chưa.

## 9. Tài liệu chi tiết

| File | Nội dung |
|---|---|
| [docs/spec.md](docs/spec.md) | Đặc tả đề tài: mục tiêu, output, không làm, cách kiểm chứng |
| [docs/PROCESS.md](docs/PROCESS.md) | Quy trình chung đầy đủ |
| [docs/CONVENTIONS.md](docs/CONVENTIONS.md) | Môi trường, thông số, quy ước |
| [docs/TASKS.md](docs/TASKS.md) | Bảng task T01–T16 |
| [docs/SCHEDULE.md](docs/SCHEDULE.md) | Lịch lùi từ 12/01/2027 |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Nhật ký quyết định |
| [docs/members/](docs/members/) | Hướng dẫn từng người |
| [docs/reference/](docs/reference/) | Yêu cầu GV, transcript buổi hướng dẫn |
