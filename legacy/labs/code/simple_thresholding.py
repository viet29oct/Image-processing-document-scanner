import cv2
import matplotlib.pyplot as plt

# Đọc ảnh màu
img_color = cv2.imread(r"D:\uni\Image Processing\source\frieren.jpg")

if img_color is None:
    print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
    exit()

# Chuyển ảnh màu sang ảnh đa cấp xám
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Chọn 5 giá trị ngưỡng
thresholds = [50, 100, 150, 200, 250]

# Tạo 5 ảnh nhị phân bằng Simple Thresholding
binary_images = []

for T in thresholds:
    _, img_binary = cv2.threshold(
        img_gray,
        T,
        255,
        cv2.THRESH_BINARY
    )

    binary_images.append(img_binary)

# Hiển thị 5 ảnh output
plt.figure(figsize=(15, 6))

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(binary_images[i], cmap="gray")
    plt.title("T = " + str(thresholds[i]))
    plt.axis("off")

plt.tight_layout()
plt.show()