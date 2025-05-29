import os
import cv2


#read vidio
video_path = "C:/Users/lilha/Desktop/CommaPrep/vid.mp4"
video = cv2.VideoCapture("C:/Users/lilha/Desktop/CommaPrep/vid.mp4")
#you can only apply blur to images - hence frames


#visualize video
#ret is a boolean var that checks if there are any frames left 
ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('low',frame)
        cv2.waitKey(100)
     #   cv2.destroyAllWindows() makes it spaz out
video.release()
cv2.destroyAllWindows()