#Filename : cv2ex29-1.py

import cv2
import numpy as np

img = cv2.imread('hand.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 120,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE
                                             ,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
cvxhull = cv2.convexHull(cnt)

cv2.drawContours(img, [cvxhull], 0, (0, 255, 0), 3)

cv2.imshow('Convex Hull', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

