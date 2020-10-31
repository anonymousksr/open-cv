import cv2
import numpy as np

img = cv2.imread("res/opencv-logo.png", 1)
cv2.imshow("ORIGINAL", img)
w, h, ch = img.shape
black = np.zeros((w, h, ch))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 1)
corners = np.int0(corners)
count = 0 

for corner in corners:
    x, y = corner.ravel()
    print(f"({x},{y})")
    count += 1
    cv2.circle(img, (x, y), 5, (0, 255, 255), -1)
    cv2.circle(black, (x, y), 5, (0, 255, 255), -1)

print(count)
cv2.imshow("IMAGE", img)
cv2.imshow("BLACK", black)

cv2.waitKey(0)
cv2.destroyAllWindows()