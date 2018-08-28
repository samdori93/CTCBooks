#Filename : cv2ex29.py

import cv2
import numpy as np

img = cv2.imread('star.jpg')
img1 = img.copy()
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 120,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE
                                             ,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)

print(M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print('cx : ', cx)
print('cy : ', cy)

area = cv2.contourArea(cnt)
print(area, M['m00'])

perimeter = cv2.arcLength(cnt, False)
print(perimeter)
perimeter = cv2.arcLength(cnt, True)
print(perimeter)

epsilon = 0.06 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
cv2.drawContours(img1, [approx], 0, (0, 255, 0), 3)

cv2.imshow('Origin', img)
cv2.imshow('approx', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

