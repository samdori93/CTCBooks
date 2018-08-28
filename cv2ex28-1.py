#Filename : cv2ex28-1.py

import numpy as np
import cv2

img = np.zeros((300,400, 3), np.uint8)

img1 = cv2.rectangle(img,(50,100),(350,200),(255,255,255),-1)
img2 = img1.copy()
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

image1, contours1, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE
                                              ,cv2.CHAIN_APPROX_NONE)
image2, contours2, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE
                                              ,cv2.CHAIN_APPROX_SIMPLE)

print('APPROX_NONE :   ', contours1[0].shape)
print('APPROX_SIMPLE : ', contours2[0].shape)

for i in contours1[0]:
    cv2.circle(img1, (i[0][0], i[0][1]), 3, (0, 0, 255), -1)

for i in contours2[0]:
    cv2.circle(img2, (i[0][0], i[0][1]), 3, (0, 0, 255), -1)

cv2.imshow('APPROX_NONE', img1)
cv2.imshow('APPROX_SIMPLE', img2)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
