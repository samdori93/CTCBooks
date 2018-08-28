# Filename : cv2ex2.py

import numpy as np
import cv2
img = cv2.imread('ci.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
k = cv2.waitKey(0)

if k == 27: 
    cv2.destroyAllWindows()
elif k == ord('s'): 
    cv2.imwrite('ci_gray.jpg', img)
    img2 = cv2.imread('ci_gray.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('image_gray', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
q
