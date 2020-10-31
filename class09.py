import cv2
import numpy as np

img = cv2.imread("res/sudoku.jpg", 0)

thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 1)
# 00000000 -> uint8
kernel = np.ones((2,2), np.uint8)

erosion = cv2.erode(thresh, kernel, iterations=1)
dilation = cv2.dilate(thresh, kernel, iterations=1)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)

gradient = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel, iterations=1)
tophat = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, kernel, iterations=1)
blackhat = cv2.morphologyEx(thresh, cv2.MORPH_BLACKHAT, kernel, iterations=1)

cv2.imshow("image", img)
cv2.imshow("adaptiveThreshold", thresh)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gradient", gradient)
cv2.imshow("tophat", tophat)
cv2.imshow("blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()