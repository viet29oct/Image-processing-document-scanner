# Phi — luồng A (đề xuất)

**Nhánh:** `dev/phi`

## Phụ trách
- Phương pháp 1: Canny + Contour + approxPolyDP → `src/snapdocs/detect_canny.py` (T04)
- Perspective warp → `src/snapdocs/warp.py` (T05)
- Enhance sau scan (cân bằng histogram/CLAHE, threshold) → `src/snapdocs/enhance.py` (T10)
- Viết phần kỹ thuật của mình trong báo cáo (T14a: PP1, warp, enhance), gửi Huấn trước 29/12. **Không** làm chủ biên hay tổng hợp báo cáo (Huấn viết chính, Việt tổng hợp và duyệt)
- Khung repo/quy trình (T02, đã xong)
- **Có quyền merge PR** (cùng Việt), được tự merge PR của mình; merge PR của Huấn sau khi xem nhanh

## Cần đọc/học
- Slide Ch4: Canny (NMS, ngưỡng kép, hysteresis), slide 57–59 contour
- Tự học: `cv2.approxPolyDP`, `cv2.getPerspectiveTransform`, `cv2.warpPerspective`
- Slide Ch3: cân bằng histogram; CLAHE (ngoài slide)

## Cách làm
1. Làm `detect` trước với ảnh dễ, rồi thử từng nhóm điều kiện khó.
2. Sắp xếp 4 điểm theo thứ tự trên-trái, trên-phải, dưới-phải, dưới-trái (chung cho mọi phương pháp).
3. Viết test với ảnh tổng hợp (vẽ hình chữ nhật xoay, biết trước 4 góc).

## Phải giải thích được khi thi
Vì sao Canny rồi mới contour; ngưỡng Canny chọn thế nào; approxPolyDP epsilon là gì và ảnh hưởng ra sao; công thức biến đổi phối cảnh (ma trận 3×3, 4 cặp điểm).

## Định nghĩa xong
Xem mục 3 trong `docs/PROCESS.md`.
