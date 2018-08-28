# Filename : cv2ex18.py

import cv2
import numpy as np

img = cv2.imread('cho.png')

height, width = img.shape[:2]
res1 = cv2.resize(img,None, fx=0.7, fy=0.7, interpolation = cv2.INTER_AREA)
res2 = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('origin', img)
cv2.imshow('size down', res1)
cv2.imshow('size up', res2)

cv2.waitKey(0)
cv2.destroyAllWindows()



