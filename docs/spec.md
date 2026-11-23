# Spec — Document Scanner

## Tên đề tài (đã chốt 23/11/2026)
Xây dựng ứng dụng quét và hiệu chỉnh phối cảnh ảnh giấy tờ với phát hiện biên tài liệu trong điều kiện chụp phức tạp.

## Mục tiêu
Từ ảnh chụp giấy tờ/văn bản, tìm 4 góc tài liệu và nắn phẳng (perspective warp). So sánh các phương pháp tìm 4 góc.

## Output cần đạt
1. Module `detect` cho phương pháp 1 (Canny+Contour+approxPolyDP) và 2 (Otsu/Adaptive+Morphology+Convex Hull). Hough là tuỳ chọn.
2. `warp`: nắn phẳng từ 4 góc; `enhance`: cân bằng histogram/CLAHE + threshold cho ảnh sau scan.
3. `quality`: cảnh báo ảnh mờ (phương sai Laplacian), quá xa (tỉ lệ diện tích), quá lệch (góc tứ giác).
4. Bộ ảnh tự chụp 40–60 ảnh, chia 5 nhóm điều kiện: nền đơn giản · nền phức tạp · thiếu sáng/sáng không đều · nghiêng mạnh · che góc.
5. Nhãn 4 góc chuẩn (đánh dấu tay) → bảng kết quả: tỉ lệ đúng, sai số góc (px) theo từng phương pháp × điều kiện.
6. GUI hai cửa sổ (trái: danh sách ảnh + nút chức năng; phải: kết quả) — theo mẫu GV gợi ý.
7. Báo cáo + slide + demo.

## Không làm
OCR (nhóm 10 đã làm) · deep learning · app điện thoại · nhận dạng nội dung giấy tờ.

## Đầu vào cần đọc
`docs/reference/yeu-cau-giang-vien.md` · slide Ch2 (lọc, threshold, Otsu/Adaptive), Ch3 (histogram), Ch4 (Canny, contour).

## Quyết định đã chốt
- Trùng đề với nhóm 12 ("Hệ thống quét tài liệu thông minh"): khác ở phương pháp (so sánh), dữ liệu (tự chụp theo điều kiện), mục đích (giấy tờ + cảnh báo chất lượng).
- Ngoài slide, phải tự học: approxPolyDP, Morphology, Convex Hull, perspective transform (Hough nếu làm).

## Cách kiểm chứng
- `pytest` qua cho `warp` và `detect` trên ảnh tổng hợp có góc biết trước.
- `experiments/run_compare.py` chạy được end-to-end và sinh bảng kết quả.
- Mỗi thành viên giải thích được phần mình (xem `docs/PROCESS.md`).

## Kết quả / bàn giao
_(điền cuối dự án)_
