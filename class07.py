import cv2
import numpy as np

astro = cv2.imread("res/astro.jpg", 1)
sea = cv2.imread("res/sea.jpg", 1)
cv2.imshow("IMAGE", astro)
cv2.imshow("SEA", sea)

#hsv -> hue, sat, value
hsv = cv2.cvtColor(astro, cv2.COLOR_BGR2HSV)

low_green = np.array([50, 150, 180])
upper_green = np.array([200, 245, 255])

mask = cv2.inRange(hsv, low_green, upper_green)
mask_inv = cv2.bitwise_not(mask)
astro = cv2.bitwise_and(astro, astro, mask=mask_inv)
sea = cv2.bitwise_and(sea,sea,mask=mask)

result = cv2.add(astro, sea)

cv2.imshow("FORGROUND", astro)
cv2.imshow("MASK", mask)
cv2.imshow("MASK_INV", mask_inv)
cv2.imshow("BACKGROUND", sea)
cv2.imshow("RESULT", result)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()