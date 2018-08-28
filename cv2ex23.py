# Filename : cv2ex23.py

import cv2
import numpy as np

img = cv2.imread('cho.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('orginal', img)
cv2.imshow('filter', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()








