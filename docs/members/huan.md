# Huấn — luồng B (đề xuất)

**Nhánh:** `dev/huan`

## Phụ trách
- Phương pháp 2: Otsu/Adaptive threshold + Morphology + Convex Hull → `src/snapdocs/detect_threshold.py` (T06)
- Cảnh báo chất lượng ảnh (mờ, quá xa, lệch) → `src/snapdocs/quality.py` (T09)
- **Viết báo cáo chính (T14b, 3/1):** dựng xương sống báo cáo, ghép phần kỹ thuật của Phi và Việt (nhận trước 29/12), thống nhất văn phong; tự viết phần PP2 và chất lượng ảnh (T14a). Dùng agent `report-writer`, chỉ trích số liệu từ `experiments/results/`
- Bàn giao bản nháp cho Việt duyệt trước 3/1

## Cần đọc/học
- Slide Ch2: threshold đơn giản, Adaptive, Otsu (slide 16–24)
- Tự học: morphology (`cv2.morphologyEx`, closing/opening), `cv2.convexHull`, `cv2.approxPolyDP`
- Phương sai Laplacian để đo độ mờ (`cv2.Laplacian(...).var()`)

## Cách làm
1. Ảnh xám → làm mờ nhẹ → Otsu hoặc Adaptive → closing để nối viền → contour lớn nhất → convex hull → xấp xỉ về 4 điểm.
2. Dùng chung hàm sắp xếp 4 điểm với phương pháp 1.
3. Ngưỡng cảnh báo chất lượng phải dựa trên số liệu từ bộ ảnh thật, không đoán.

## Phải giải thích được khi thi
Vì sao Otsu/Adaptive hợp với nền/ánh sáng nào; closing làm gì với viền bị đứt; convex hull khác contour thường ở điểm nào; ngưỡng cảnh báo lấy từ đâu.

## Định nghĩa xong
Xem mục 3 trong `docs/PROCESS.md`.
