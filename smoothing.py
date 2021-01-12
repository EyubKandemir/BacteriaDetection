import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread("34142.jpg")
img = cv2.imread("34142.jpg", 0)
img = img[0:883, 0:1024]

kernel = np.ones((5,5),np.float32)/25
kernel = np.ones((4,1), np.uint8)

dst = cv2.filter2D(img,-1,kernel)
dst2 = cv2.filter2D(img,-1,kernel)
dst2 = cv2.medianBlur(dst2,(5))
dst3 = cv2.medianBlur(dst2,(1))
blur = cv2.blur(img,(5,5))
gaussian = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,(5))


titles = ['Median','Gaussian','image','2D Conv','blur']
images = [median, gaussian, img, dst, blur] 

cv2.imshow("dst",dst)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)
#cv2.imshow("blur",blur)
#cv2.imshow("gaussian",gaussian)
#cv2.imshow("median",median)



cv2.waitKey(0)
cv2.destroyAllWindows()