import os
import cv2
import numpy as np

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/Screenshot 2023-09-11 130453.png")


edge = cv2.Canny(img, 100, 200)

# two fucntitns that arent related to edge detection - but can make it easier

dil = cv2.dilate(edge, np.ones((3,7), dtype = np.int8)) #uses numpy ----makes lines thicker

#oppisute of dil
ero = cv2.erode(dil, np.ones((3,7), dtype = np.int8))

cv2.imshow('edge',edge)
cv2.imshow('img',dil)
cv2.imshow('ero',ero)

cv2.waitKey(0)

