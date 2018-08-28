# Filename : cv2ex9.py

import numpy as np
import cv2

img = np.zeros((512,512, 3), np.uint8)

img = cv2.circle(img, (256,256), 50, (0,0,255), -1)
img = cv2.circle(img, (256,256), 100, (0,0,255), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

