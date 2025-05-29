import os
import cv2 as cv

vid = cv.VideoCapture("C:/Users/lilha/Desktop/CommaPrep/v24044gl0000d0gdqfnog65qsikeif1g.mov")

ret = True




while ret:
    ret, frame = vid.read()
    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    _,x = cv.threshold(grey,127,255,cv.THRESH_BINARY) 

    xx,xxx = cv.findContours(x, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for count in xx:
        if cv.contourArea(count) <600:
            x1,y1,w,h = cv.boundingRect(count)
            cv.rectangle(frame,(x1,y1),(x1+w,y1+h),(255,0,0),3)


    if ret:
        cv.imshow('vid',frame)
        cv.waitKey(10)
vid.release()
cv.destroyAllWindows()




#img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/1.png")
#img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#ret, thresh = cv2.threshold(img2,127,255,cv2.THRESH_BINARY_INV)


#contours, hierarchy  = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE ) 

#for count in contours:
#   if cv2.contourArea(cnt)>200
#       x1,y1,w,h = cv.boundingRect(count)
#       cv.rectangle(frame,(x1,y1),(x1+w,y1+h),(255,0,0),3)
#

# grab image - make grey - make threshold - find all white blobs in black/white image - for loop to find and put rect over white part

