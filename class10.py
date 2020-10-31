import cv2


img = cv2.imread("res/sudoku.jpg", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5) 
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5) 
sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize = 5) 

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize = 5)



cv2.imshow("Image", img)
cv2.imshow("Sobel-X", sobelx)
cv2.imshow("Sobel-XY", sobelxy)
cv2.imshow("Sobel-Y", sobely)
cv2.imshow("Laplacian", laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()