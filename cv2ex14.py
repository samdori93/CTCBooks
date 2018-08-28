# Filename : cv2ex14.py

import cv2
import numpy as np

img1 = cv2.imread('logo.jpg')
img2 = cv2.imread('cho.png')

rows,cols,channels = img1.shape
roi = img2[0:rows, 0:cols ]

img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_fg = cv2.bitwise_and(img1,img1,mask = mask_inv)
img2_bg = cv2.bitwise_and(roi,roi,mask = mask)

dst = cv2.add(img1_fg,img2_bg)
img2[0:rows, 0:cols ] = dst

cv2.imshow('res',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

