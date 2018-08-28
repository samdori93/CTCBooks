#Filename : plot.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('logo.jpg')
img2 = cv2.imread('cho.png')
img3 = cv2.imread('ci.png')
img4 = cv2.imread('timetable.jpg')

plt.subplot(2,2,1), plt.imshow(img1), plt.title('Logo'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(img2), plt.title('cho'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(img3), plt.title('ci')
plt.subplot(2,2,4), plt.imshow(img4), plt.title('timetable')

plt.show()
