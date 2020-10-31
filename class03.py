# To generate a 250x500 black immage and draw few shapes and put text on it

import cv2
import numpy as np

img = np.zeros((250, 500, 3))

# b,g,r -> 0-255,0-255,0-255

img = cv2.line(img, (100, 125), (400, 125), (0, 0, 255), 5)

img = cv2.rectangle(img, (10, 100), (90, 150), (255,0,0), -1)

img = cv2.circle(img, (450,125), 40, (0,255,0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
string = "Text"
img = cv2.putText(img, string, (235,200), font, 0.5, (255,255,255), 1)

pts = np.array([[0,0],[250,125],[0,250],[500,250],[250,125],[500,0]], np.int32)
img = cv2.polylines(img, [pts], True, (0,255,255), 5)

cv2.imshow("Image", img)

cv2.imwrite("result/shape.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()