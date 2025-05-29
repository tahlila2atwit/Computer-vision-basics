import os 
import cv2 as cv
import numpy as np
from PIL import Image

# color detection - if something is a certain color- check each frame - and draw a box around it 
# Yellow in rgb is (255,255,0)

#mask work by blocking everything except the color

l_y = np.array([10,100,20])
u_y = np.array([20,255,200])

w = cv.VideoCapture(0)

while True:
    ret, frame = w.read()

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, l_y,u_y)
    mask_ = Image.fromarray(mask) #converting img from num to pilo

    box = mask_.getbbox()

    if box is not None:
        x1,y1,x2,y2 = box

        x =  cv.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),5)
        #y = cv.putText(frame,'Person',(x1,y1),4,1,(255,25,0),4)



    cv.imshow('cam',frame)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

w.release()
cv.destroyAllWindows()

#---------------------------------------------------------


lwr = np.array([0,100,100])
hgr = np.array([10,159,255])

vvv = cv.VideoCapture(0)

while True:
    ret, frame = vvv.read()

    g = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    inf = cv.inRange(g,lwr,hgr)
    inff = Image.fromarray(inf)
 
    boxx = inff.getbbox()

    if boxx is not None:
        x1,y1,x2,y2 = boxx

        r = cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)



    cv.imshow('vvv',frame)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break
vvv.release()
cv.destroyAllWindows()
