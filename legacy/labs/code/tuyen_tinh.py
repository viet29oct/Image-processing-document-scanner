from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


# Đọc ảnh từ thư mục source.
PROJECT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = PROJECT_DIR / "source" / "cho.jpg"

img = cv2.imread(str(IMAGE_PATH))
if img is None:
    raise FileNotFoundError(f"Không đọc được ảnh: {IMAGE_PATH}")


# Ánh xạ một mức sáng theo ba đoạn thẳng.
def pixelVal(pix, r1, s1, r2, s2):
    if pix <= r1:
        return (s1 / r1) * pix
    elif pix <= r2:
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2


# Tham số của phép biến đổi tuyến tính từng phần.
r1, s1 = 70, 0
r2, s2 = 140, 255

# Áp dụng hàm pixelVal cho từng giá trị màu trong ảnh.
pixelVal_vec = np.vectorize(pixelVal)
piecewise = pixelVal_vec(img, r1, s1, r2, s2)
piecewise = np.clip(piecewise, 0, 255).astype(np.uint8)


# Biến đổi lũy thừa: gamma > 1 làm ảnh tối hơn.
gamma = 2.2
power = 255 * (img / 255.0) ** gamma
power = power.astype(np.uint8)


# Thu nhỏ ảnh để ba ảnh vừa trong một cửa sổ.
panel_width = 330
panel_height = int(img.shape[0] * panel_width / img.shape[1])
images = [
    cv2.resize(img, (panel_width, panel_height)),
    cv2.resize(piecewise, (panel_width, panel_height)),
    cv2.resize(power, (panel_width, panel_height)),
]
labels = ["Ảnh gốc", "Tuyến tính từng phần", f"Lũy thừa (gamma={gamma})"]

# Thêm nhãn tiếng Việt trên dải nền tối.
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 20)
panels = []
for image, label in zip(images, labels):
    header = Image.new("RGB", (panel_width, 46), (36, 41, 47))
    draw = ImageDraw.Draw(header)
    bounds = draw.textbbox((0, 0), label, font=font)
    x = (panel_width - (bounds[2] - bounds[0])) // 2
    y = (46 - (bounds[3] - bounds[1])) // 2 - bounds[1]
    draw.text((x, y), label, font=font, fill="white")

    header = cv2.cvtColor(np.array(header), cv2.COLOR_RGB2BGR)
    panels.append(np.vstack((header, image)))

comparison = np.hstack(panels)
cv2.imshow("So sanh ket qua", comparison)
cv2.imwrite(str(PROJECT_DIR / "piecewise_vs_power.jpg"), comparison)

print("Saved comparison: piecewise_vs_power.jpg")
cv2.waitKey(0)
cv2.destroyAllWindows()
