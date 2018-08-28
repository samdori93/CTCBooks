# Filename : cv2ex26.py

import cv2
import numpy as np
from matplotlib import pyplot as plt


orig = cv2.imread('ci_binary2.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT, kernel)
opening = cv2.morphologyEx(orig, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(orig, cv2.MORPH_CLOSE, kernel)


images =[orig, gradient, opening, closing]
titles =['origin', 'gradient', 'opening','closing' ]

for i in range(4):
    plt.subplot(4,1,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
