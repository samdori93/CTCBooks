# Filename : cv2ex25.py

import cv2
import numpy as np
from matplotlib import pyplot as plt


orig = cv2.imread('ci_binary.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

erosion = cv2.erode(orig, kernel, iterations = 1)
dilation = cv2.dilate(orig, kernel, iterations = 1)

images =[orig, erosion,  dilation]
titles =['origin', 'Erosion','Dilation']

for i in range(3):
    plt.subplot(3,1,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
