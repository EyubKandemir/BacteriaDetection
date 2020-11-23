import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('34142.jpg',0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gaussian = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,(5))


titles = ['Median','Gaussian','image','2D Conv','blur']
images = [median, gaussian, img, dst, blur]

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()