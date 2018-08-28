#Filename : cv2ex28.py

import numpy as np
import cv2

img = cv2.imread('ci.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)s
ret,thresh = cv2.threshold(imgray,200,255,0)
image1, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE
                                              ,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,0,255), 2)

cv2.imshow('origin', img)
cv2.imshow('gray', imgray)
cv2.imshow('threshold', thresh)
cv2.imshow('contour', image1)

cv2.waitKey(0)
cv2.destroyAllWindows()

