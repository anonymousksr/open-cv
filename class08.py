import cv2
import numpy as np

img = cv2.imread("res/RGB.jpg", 1)

blur = cv2.GaussianBlur(img, (15,15), sigmaX=10, sigmaY=0)
median = cv2.medianBlur(img, 11)

cv2.imshow("Original Image", img)
cv2.imshow("GaussianBlur Image", blur)
cv2.imshow("medianBlur Image", median)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()