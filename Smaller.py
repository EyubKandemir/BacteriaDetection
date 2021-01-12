import cv2
import numpy as np

im = cv2.imread("34142.jpg")
img = cv2.imread("34142.jpg", 0)
img = img[0:883, 0:1024]

kernal = np.ones((2,2), np.uint8)
#kernal = np.ones((5,5),np.float32)/25
img = cv2.dilate(img, kernal,iterations=2)

_,th1 = cv2.threshold(img,50,60,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,55,55,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO_INV)


contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours : ", str(len(contours)))

canny = cv2.Canny(th2,100,200)


cnt1 = contours[1]
#cv2.drawContours(im, [cnt1], -1, (0, 255, 0), 2)
print("Cnt 1 area : ", cv2.contourArea(cnt1))

lastContours=[]

for cnts in contours:
    if(cv2.contourArea(cnts)>40 and cv2.contourArea(cnts)<500 ):
        lastContours.append(cnts)

print(str(len(lastContours)))
cv2.drawContours(im, lastContours, -1, (0, 255, 0), 2)


#cv2.imshow("THRESH_BINARY_INV",th2)
#cv2.imshow("THRESH_TRUNC",th3)
#cv2.imshow("THRESH_TOZERO",th4)
#cv2.imshow("THRESH_TOZERO_INV",th5)


cv2.imshow("orji",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
