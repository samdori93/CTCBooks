#Filename : border.py

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo.jpg')

constant= cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,0,0])
reflect = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT_101)
replicate = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REPLICATE)
wrap = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_WRAP)

images = [img, constant, reflect, reflect_101, replicate, wrap]
titles = ['ORIGINAL', 'CONSTANT', 'REFLECT', 'REFLECT_101', 'REPLICATE', 'WRAP']

for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

