import cv2
import numpy as np

dave = cv2.imread("res/roadsigns.jpg", 1)
dave_gray = cv2.cvtColor(dave, cv2.COLOR_BGR2GRAY)

coin = cv2.imread("res/~uTurn.jpg", 0)
w, h = coin.shape[::-1]

res = cv2.matchTemplate(dave_gray, coin, cv2.TM_CCOEFF_NORMED)
accuracy = 0.40 # 30%
loc = np.where(res >= accuracy)
# print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(dave, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 5)

cv2.imshow("Result", dave)

cv2.waitKey(0)
cv2.destroyAllWindows()