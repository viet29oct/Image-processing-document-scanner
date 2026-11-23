import cv2
import matplotlib.pyplot as plt

# 1. Đọc ảnh màu
img_color = cv2.imread(r"D:\uni\Image Processing\source\frieren.jpg")

if img_color is None:
    print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
    exit()

# 2. Chuyển ảnh màu sang ảnh đa cấp xám
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# 3. Adaptive Thresholding
img_adaptive = cv2.adaptiveThreshold(
    img_gray,                       # Ảnh xám đầu vào
    255,                            # Giá trị lớn nhất
    cv2.ADAPTIVE_THRESH_MEAN_C,     # Tính ngưỡng bằng giá trị trung bình
    cv2.THRESH_BINARY,              # Chuyển thành ảnh nhị phân
    11,                             # Kích thước vùng lân cận
    2                               # Hằng số C
)

# 4. Hiển thị ảnh xám và ảnh kết quả
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap="gray")
plt.title("Ảnh đa cấp xám")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_adaptive, cmap="gray")
plt.title("Adaptive Thresholding")
plt.axis("off")

plt.tight_layout()
plt.show()