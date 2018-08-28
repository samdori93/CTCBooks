# Filename : cv2ex27.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ci_gray.jpg')

sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
laplacian = cv2.Laplacian(img,cv2.CV_8U)
canny = cv2.Canny(img,30,70)

images = [sobelx, sobely, laplacian, canny]
titles = ['Sobel X', 'Sobel Y','Laplacian', 'Canny']

for i in range(4):
    plt.subplot(4,1,i+1),plt.imshow(images[i]),plt.title([titles[i]])
    plt.xticks([]),plt.yticks([])

plt.show()
