# Filename : cv2ex10.py

import numpy as np
import cv2

img = np.zeros((400,400, 3), np.uint8)

img = cv2.ellipse(img, (200,200), (100,50), 0, 0, 180, 255, -1)
img = cv2.ellipse(img, (200,200), (100,50), 180, 0, 180, 255, 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

