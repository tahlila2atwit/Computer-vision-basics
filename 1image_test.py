import cv2

import os

img = cv2.imread('C:/Users/lilha/Downloads/IMG_6227.jpg')

cv2.imshow('Image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()


print(img.shape)
#-----------------------------------
#read iamge - how to read image from computer
#image_path = os.path.join('.','data','bird.jpg')
img=cv2.imread("C:/Users/lilha/Desktop/CommaPrep/1126.jpg")

#write iamge - write imagr from script to computer
cv2.imwrite("C:/Users/lilha/Desktop/CommaPrep/11222226.jpg",img)

#visualize image

cv2.imshow('Image lo',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
