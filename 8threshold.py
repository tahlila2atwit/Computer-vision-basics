import os
import cv2

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/11222226.jpg")

# convert this image into a binary image 
# binay image is black/white 


grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thres = cv2.threshold(grey, 80,255, cv2.THRESH_BINARY)

#ret, thresh = cv2.threshold(grey,100,255, cv2.THRESH_BINARY_INV)

la = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)# will feel the threshold by itself

# lights kinda uneven, check each area- find average brighness sub 30 - and turn pixel brighter than a certain point white
#150-30 - threshold is now 120

#use this to get text out of a image if the lighting is weird

cv2.imshow('img',thres)

cv2.waitKey(0)
cv2.destroyAllWindows()

