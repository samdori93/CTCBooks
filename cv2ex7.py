# Filename : cv2ex7.py

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

img = cv2.line(img,(0,0), (511,511), (255,255,255), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


