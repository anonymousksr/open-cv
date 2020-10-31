import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread("res/text.jpg")
img2 = cv2.imread("res/logo.jpg")

res = cv2.imread("res/text.jpg")

r, c, ch = img2.shape
roi = img1[57:r+57, 200:c+200]

print(img2.shape)
print(img2.dtype)

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, msk = cv2.threshold(img2gray, 245, 255, cv2.THRESH_BINARY_INV)

msk_inv = cv2.bitwise_not(msk)

img1_bg = cv2.bitwise_and(roi, roi, mask=msk_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=msk)

dst = cv2.add(img1_bg, img2_fg)
# (50,200,130) + (150,150,250) = (200,350,380) ===> (200,255,255)

res[57:r+57, 200:c+200] = dst



titles = ['img1', 'img2', 'roi', 'mask', 'img1_bg', 'img2_fg', 'dst', 'result']
images = [img1, img2, roi, msk, img1_bg, img2_fg, dst, res]

cv2.imshow("result", res)

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()