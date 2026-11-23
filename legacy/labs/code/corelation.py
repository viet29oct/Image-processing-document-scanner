from pathlib import Path

import cv2
import numpy as np

# Bài 1: tính 9 giá trị hợp lệ trong ví dụ của đề.
in_img = np.array(
    [[1, 0, 0, 1, 0],
     [0, 1, 1, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 0, 1, 0],
     [0, 1, 1, 0, 1]]
)

# Nhập kernel H ở đây; có thể thay các số trong ma trận.
kernel = np.array(
    [[1, 0, 0],
     [0, 1, 1],
     [1, 0, 1]],
    dtype=np.float32,
)


def correlation(img, kernel):
    # Lấy kích thước ảnh và kernel
    img_height, img_width = img.shape
    kernel_height, kernel_width = kernel.shape

    # khoảng cách từ tâm kernel đến mép của kernel
    half_height = kernel_height // 2
    half_width = kernel_width // 2

    # Tính khoảng cách từ tâm kernel đến mép
    out = np.zeros((img_height, img_width), dtype=np.float32)

    # Thuật toán: duyệt từng tâm ảnh -> nhân từng ô kernel -> cộng -> lưu tổng.
    for y in range(half_height, img_height - half_height):
        for x in range(half_width, img_width - half_width):
            total = 0
            for m in range(kernel_height):
                for n in range(kernel_width):
                    image_y = y + m - half_height
                    image_x = x + n - half_width
                    pixel = img[image_y, image_x]
                    weight = kernel[m, n]
                    total += pixel * weight
            out[y, x] = total

    return out


out_example = correlation(in_img, kernel)
print("Bai 1 - correlation 3x3:")
print(out_example[1:-1, 1:-1].astype(int))


# Bài 2: đọc ảnh, chuyển sang ảnh xám rồi tính tương quan.
project_dir = Path(__file__).resolve().parent.parent
image_path = project_dir / "source" / "cho.jpg"
img = cv2.imread(str(image_path))

if img is None:
    raise FileNotFoundError(f"Không đọc được ảnh: {image_path}")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
out_img = correlation(gray_img, kernel)

# Chuẩn hóa riêng để nhìn rõ kết quả trên màn hình.
out_display = cv2.normalize(out_img, None, 0, 255, cv2.NORM_MINMAX)
out_display = out_display.astype(np.uint8)

cv2.imshow("Original grayscale", gray_img)
cv2.imshow("Correlation result", out_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
