# Filename : cv2ex13.py

import cv2
import numpy as np

img1 = cv2.imread('flippy.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('logo2.jpg', cv2.IMREAD_COLOR)
img3 = cv2.add(img1, img2)
img4 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('flippy.jpg', img1)
cv2.imshow('logo.jpg', img2)
cv2.imshow('addition', img3)
cv2.imshow('Weighed addition', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
