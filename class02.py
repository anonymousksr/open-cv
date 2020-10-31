# reading a Video (Using cap variable to capture and frame variable for frames) 
# and writeing Video (saving the Video in detination folder)
# Video location (relative path) -> "res/30_10fps.avi"
# destination to save images -> "result/*.avi"

# import OpenCV
import cv2

# captureing method is performed by cap variable

cap = cv2.VideoCapture('res/30_10fps.avi')

# cv2::VideoCapture(0) -> to read video from camera 
# [0 is camera address ... There can be more than 1]

# fcc is codec to write video

fcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('result/30_10fps.avi', fcc, 30.0, (400, 200))

# output is responsible to write video
# cv::VideoWrite(destination, codec, frame per second, size of video[w, h])


while True:
    # read the captured [by cap] video.
    # ret represents if frame is present or not
    ret, frame = cap.read()

    # as frame is similar to a single image we use cv::imshow method
    cv2.imshow("Frame", frame)

    # this will write a frame into video.
    out.write(frame)

    # we wait till a  esc key is pressed [27 -> value of esc key] to exit the loop.
    if cv2.waitKey(1) == 27:
        break

# release video source from cap and output source from out.
cap.release()
out.release()