import cv2
import numpy as np

im = cv2.imread("34142.jpg")
img = cv2.imread("34142.jpg", 0)
img = img[0:883, 0:1024]

kernal = np.ones((5,5), np.uint8)
img = cv2.dilate(img, kernal)

_, th2 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)

edge = cv2.Canny(th2, 180, 255)

contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of Contours : " + str(len(contours)))

# 1,11,22,29
cnt1 = contours[1]
cnt2 = contours[11]
cnt3 = contours[22]
cnt4 = contours[29]
cv2.drawContours(im, [cnt1, cnt2, cnt3, cnt4], -1, (0, 255, 0), 2)

M = cv2.moments(cnt1)
cx1 = int(M['m10']/M['m00'])
cy1 = int(M['m01']/M['m00'])
cv2.putText(im,'Bacteria-1',(cx1,cy1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),2)

M = cv2.moments(cnt2)
cx2 = int(M['m10']/M['m00'])
cy2 = int(M['m01']/M['m00'])
cv2.putText(im,'Bacteria-2',(cx2,cy2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),2)

M = cv2.moments(cnt3)
cx3 = int(M['m10']/M['m00'])
cy3 = int(M['m01']/M['m00'])
cv2.putText(im,'Bacteria-3',(cx3,cy3),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),2)

M = cv2.moments(cnt4)
cx4 = int(M['m10']/M['m00'])
cy4 = int(M['m01']/M['m00'])
cv2.putText(im,'Bacteria-4',(cx4,cy4),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),2)

cv2.circle(im,(cx1,cy1),1,(255,0,0),2)
cv2.circle(im,(cx2,cy2),1,(255,0,0),2)
cv2.circle(im,(cx3,cy3),1,(255,0,0),2)
cv2.circle(im,(cx4,cy4),1,(255,0,0),2)


cv2.imshow("th2", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
