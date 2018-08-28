# Filename : cv2ex24.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('timetable.jpg')

blur = cv2.blur(img, (5, 5))
gauss = cv2.GaussianBlur(img,(5,5), 0)
median = cv2.medianBlur(img, 9)
bila = cv2.bilateralFilter(img, 9, 75, 75)


cv2.imshow('Original', img)
cv2.imshow('blurred', blur)
cv2.imshow('Gaussian', gauss)
cv2.imshow('Median', median)
cv2.imshow('Bilateral', bila)
cv2.waitKey(0)
cv2.destroyAllWindows()








