#import libraries
import cv2
import numpy as np

#read the image
img = cv2.imread("catimg.jpg")
#img = input("Filename: ")

#find edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9)

#cartoonization
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
cv2.imshow("Image", img)
cv2.imshow("edge", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
