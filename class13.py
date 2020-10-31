import cv2
import numpy as np 

cap = cv2.VideoCapture("res/cam_feed.avi")
# MOG
# motion_dector = cv2.createBackgroundSubtractorMOG2()

_, f1 = cap.read()
_, f2 = cap.read()
_, f3 = cap.read()
_, f4 = cap.read()
_, f5 = cap.read()

while cap.isOpened():
# while True:
#     res, frame = cap.read()
#     motion = motion_dector.apply(frame)
    frame = cv2.absdiff(f1, f5)
    cv2.imshow("Original", f1)
    cv2.imshow("Motion", frame)

    f1 = f2
    f2 = f3
    f3 = f4
    f4 = f5
    _, f5 = cap.read()
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()