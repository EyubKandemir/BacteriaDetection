import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the input image")
ap.add_argument("-o","--output",required=True,help="path to the output image")
args = vars(ap.parse_args())

counter = {}

image_orig = cv2.imread('34142.jpg')
image_orig = image_orig[0:883, 0:1024]

height_orig,weight_orig = image_orig.shape[:2]

image_contours = image_orig.copy()

colors=['black']

image_to_process = image_orig.copy()

counter = 0

lower = np.array([75,25,25])
upper = np.array([95,45,45])

image_mask = cv2.inRange(image_to_process,lower,upper)
image_res = cv2.bitwise_and(image_to_process,image_to_process,mask=image_mask)

image_gray = cv2.cvtColor(image_res,cv2.COLOR_BGR2GRAY)
image_gray = cv2.GaussianBlur(image_gray,(5,5),0)

image_edged = cv2.Canny(image_gray,50,100)
image_edged = cv2.dilate(image_edged,None,iterations=1)
image_edged = cv2.erode(image_edged,None,iterations=1)

cnts = cv2.findContours(image_edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image_contours,cnts,-1,(0,255,0),1)

cv2.imwrite(args["output"],image_contours)


cv2.waitKey(0)
cv2.destroyAllWindows()
