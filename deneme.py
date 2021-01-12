import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread("34142.jpg",0)
""""
img_filt = cv2.medianBlur(img,1)
img_th = cv2.adaptiveThreshold(img_filt,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
contours,hierarchy = cv2.findContours(img_th,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
"""
_,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO_INV)

kernal = np.ones((1,2),np.uint8)
dilation = cv2.dilate(th2,kernal,iterations=1)
erosion =cv2.erode(dilation,kernal,iterations=1)
opening = cv2.morphologyEx(th2,cv2.MORPH_OPEN,kernal,)

titles=["contour","Original","erosion","dilation","Bınary Inv.","opening","Binary","Trunc","To_zero","To_zero_Inv" ]
images = [img,erosion,dilation,th2,opening,th1,th3,th4,th5]

for i in range(8):
    plt.subplot(3,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

print(th2)

""""
cv2.imshow("th2",th2)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#plt.show()
cv2.imshow("dilation",dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()