import cv2
import numpy as np

im = cv2.imread("34142.jpg")
img = cv2.imread("34142.jpg", 0)
img = img[0:883, 0:1024]
#172 pixel = 1 makrometer

kernal = np.ones((5,5), np.uint8)
img = cv2.dilate(img, kernal)

_, th2 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of Contours : " + str(len(contours)))
BacteriaContours = []

for c in contours:
    if(cv2.contourArea(c)> 36000 and cv2.contourArea(c)<63000):
        BacteriaContours.append(c)

del(BacteriaContours[1])

numberOfBacteria = int(len(BacteriaContours))
print("numberOfBacteria",numberOfBacteria)
cv2.drawContours(im, BacteriaContours, -1, (0, 255, 0), 2)

def area_circumferenceCalculator(hugeContours):
    sumOfArea = 0
    sumOfCircumference = 0
    for cnt in hugeContours:
        sumOfArea+=cv2.contourArea(cnt)
        sumOfCircumference+= cv2.arcLength(cnt, True)
    return sumOfArea/numberOfBacteria,sumOfCircumference/numberOfBacteria

def width_lengthCalculator(hugeContours):
    sumOfWidth = 0
    sumOfLength = 0
    for cnt in hugeContours:
        rect = cv2.minAreaRect(cnt)
        (x, y), (width, length), angle = rect
        if(width<length):
            x = length
            length = width
            width = x
        sumOfWidth+=width
        sumOfLength+=length
    return sumOfWidth/numberOfBacteria,sumOfLength/numberOfBacteria

averageOfArea, averageOfCircumference= area_circumferenceCalculator(BacteriaContours)
averageOfWidth, averageOfLength=width_lengthCalculator(BacteriaContours)

print("A) Average Bacteria Area is : ", averageOfArea)
print("B) Average Bacteria Width is : {} Average Bacteria Length is : {}".format(round(averageOfWidth,2),round(averageOfLength,2)))
print("C) Average Bacteria Circumference is : ",round(averageOfCircumference,2))

cv2.imshow("Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()