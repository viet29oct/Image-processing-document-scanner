import cv2 
import matplotlib.pyplot as plt

img_color = cv2.imread(r"D:\uni\Image Processing\source\frieren.jpg")

if img_color is None:
    print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
    exit()

# Chuyển đổi ảnh sang màu xám
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Chuyển màu xám sang âm bản
# Công thức: s = intensity(max) - r
# Anh 8-bit: intensity(max) = 2^8 - 1 = 255

intensity_max = 255
img_negative = intensity_max - img_gray


# cv2.imshow("Ảnh màu", img_color)
# cv2.imshow("Ảnh xám", img_gray)
# cv2.imshow("Ảnh âm bản", img_negative)

# cv2.waitKey(0)

# cv2.destroyAllWindows()


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img_color)
plt.title("Ảnh màu")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Ảnh đa cấp xám")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(img_negative, cmap="gray")
plt.title("Ảnh âm bản")
plt.axis("off")

plt.tight_layout()
plt.show()
