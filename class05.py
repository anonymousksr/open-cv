import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("res/logic_1.jpg")
img2 = cv2.imread("res/logic_2.jpg")



bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
not_img1 = cv2.bitwise_not(img1)
not_img2 = cv2.bitwise_not(img2)

# titles = ['img1', 'img2', 'bit_and', 'bit_or', 'bit_xor', 'not_img1', 'not_img2']
# images = [img1, img2, bit_and, bit_or, bit_xor, not_img1, not_img2]


# for i in range(7):
#     plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

cv2.imshow("AND", bit_and)
cv2.imwrite("result/AND.jpg", bit_and)
cv2.imshow("OR", bit_or)
cv2.imwrite("result/OR.jpg", bit_or)
cv2.imshow("XOR", bit_xor)
cv2.imwrite("result/XOR.jpg", bit_xor)
cv2.imshow("Img 01 NOT", not_img1)
cv2.imwrite("result/Img01NOT.jpg", not_img1)
cv2.imshow("Img 02 NOT", not_img2)
cv2.imwrite("result/Img02NOT.jpg", not_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()