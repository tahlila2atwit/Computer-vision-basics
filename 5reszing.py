import os
import cv2

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/11222226.jpg")
#regular image size (341, 512, 3)
resized_image = cv2.resize(img,(300,1000))

print(img.shape)#(341, 512, 3)
print(resized_image.shape) #(256, 166, 3)

cv2.imshow('img',resized_image)
cv2.waitKey(0)