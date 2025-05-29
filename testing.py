import os
import cv2
import numpy as np
# image reading

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/download.jpg")

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows

# video reading

#vid = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/v24044gl0000d0gdqfnog65qsikeif1g.mov")
path = cv2.VideoCapture("C:/Users/lilha/Desktop/CommaPrep/v24044gl0000d0gdqfnog65qsikeif1g.mov")

ret = True

while ret:
    ret, frame = path.read()
    if ret:
        cv2.imshow('vid',frame)
        cv2.waitKey(10)
path.release()
cv2.destroyAllWindows

# webcam

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    x = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
#-------------blurring----------------------------------------------
    blur = cv2.blur(frame,(21,35))
    g = cv2.GaussianBlur(frame,(31,43),4)
    m = cv2.medianBlur(frame, 7)
#--------------threshhold---------------------------------------------
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # ret, thres = cv2.threshold(grey,130,235,cv2.THRESH_BINARY)

    ap = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,29,5)  
                            #21 is pixel size, 5 is subtracted so more pix turn white and 

#----------edge detection--------------------------------------------------
    e = cv2.Canny(grey,100,300)
    d = cv2.dilate(frame,np.ones((1,5),dtype= np.int8))

#-------------rectangles/text-----------------------------------------------
    re = cv2.rectangle(frame,(0,0),(200,200),(200,0,0),4)
    text = cv2.putText(d, "wassup",(200,200),5,3.15,(231,522,0),4)

#----------------countours------------------------------------------------------


    cv2.imshow('fra',text)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows

