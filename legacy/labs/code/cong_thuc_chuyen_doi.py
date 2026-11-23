import cv2
import numpy as np

# 1. Đọc ảnh (OpenCV đọc mặc định theo thứ tự BGR)
image_bgr = cv2.imread(r"D:\uni\Image Processing\source\tach_anh.png")

# Chuyển đổi sang float32 để tránh tràn số khi tính toán cộng/nhân
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB).astype(np.float32)

# Tách 3 kênh màu R, G, B
R = image_rgb[:, :, 0]
G = image_rgb[:, :, 1]
B = image_rgb[:, :, 2]

# --- 1. Phương pháp Lightness ---
# grayscale = (min(R, G, B) + max(R, G, B)) / 2
min_rgb = np.min(image_rgb, axis=2)
max_rgb = np.max(image_rgb, axis=2)
gray_lightness = ((min_rgb + max_rgb) / 2.0).astype(np.uint8)

# --- 2. Phương pháp Average (Trung bình) ---
# grayscale = (R + G + B) / 3
gray_average = ((R + G + B) / 3.0).astype(np.uint8)

# --- 3. Phương pháp Luminosity ---
# grayscale = 0.3 * R + 0.59 * G + 0.11 * B
gray_luminosity = (0.3 * R + 0.59 * G + 0.11 * B).astype(np.uint8)

# Lưu kết quả ra file ảnh
cv2.imwrite("gray_lightness.jpg", gray_lightness)
cv2.imwrite("gray_average.jpg", gray_average)
cv2.imwrite("gray_luminosity.jpg", gray_luminosity) 