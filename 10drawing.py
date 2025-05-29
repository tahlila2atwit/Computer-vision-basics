import os
import cv2

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/Screenshot 2024-06-30 180225.png")

#line
line = cv2.line(img, (100,150), (300,450),(15,124,21),10)
print(img.shape)
#takes img and the start/end point of the line, color, thickness

#rectangle
rect = cv2.rectangle(img,(1,1),(500,500),(0,23,32),20)
#circle

circ = cv2.circle(img, (34,100), 25, (100,11,100),5)



#text

txt = cv2.putText(img, "wassup", (120,120), 20, 3.14, (120,200,0), 3)
cv2.imshow('txt',txt)

cv2.waitKey(0)
cv2.destroyAllWindows()