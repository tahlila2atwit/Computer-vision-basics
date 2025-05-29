import os
import cv2

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/11222226.jpg")

cv2.imshow("color",img)
#cv2.waitKey(0)

# 3 color spaces - blue green red to red green blue

swimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#convert from one colorspace to another
cv2.imshow("bruh",swimg)
#cv2.waitKey(0)

# swithc to greyscale
grimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#convert from one colorspace to another
cv2.imshow("gruh",grimg)
#cv2.waitKey(0)

# swithc to HSV
himg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # used to detect color
#convert from one colorspace to another
cv2.imshow("hruh",himg)
cv2.waitKey(0)


# way more arguments of RGB2---