import cv2
img = cv2.imread(r"D:\uni\Image Processing\source\frieren.jpg", cv2.IMREAD_COLOR)
cv2.imshow('Image BGR', img)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Image RGB', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()