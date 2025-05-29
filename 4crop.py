import os
import cv2

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/11222226.jpg")

cv2.imshow('bar',img) # the window
#cv2.waitKey(0) # how long it stays open

print(img.shape) # width + height of image
#(341, 512, 3)

crop_img = img[110:230, 250:450] 
#crop from this pizel to this pizel
cv2.imshow('img2',crop_img)
cv2.waitKey(0)