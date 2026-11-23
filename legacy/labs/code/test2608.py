import cv2
import numpy as np
import matplotlib.pyplot as plt
import pip
img = cv2.imread(r"D:\uni\Image Processing\source\frieren.jpg", cv2.IMREAD_COLOR_BGR)

plt.imshow(img)
plt.waitforbuttonpress()
plt.close('all')
