import os
import cv2

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/1.png")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img2,127,255,cv2.THRESH_BINARY_INV)

#contours

contours, hierarchy  = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE ) 
# find all the white shapes on black


for cnt in contours:
    if cv2.contourArea(cnt) > 200:
#ignoring tiny chunks

        #cv2.drawContours(img,cnt,-1,(0,255,0),1) 

        x1, y1, w, h = cv2.boundingRect(cnt)
 # give me a rectangle that perfectly fits around this shape x1 left side, y1 top side, w width of box, h height of box

        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(213,0,0),1)
#draw a rectangle on this points

cv2.imshow("gruh",img)
cv2.waitKey(0)