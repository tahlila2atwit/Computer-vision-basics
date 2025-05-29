import os
import cv2


# four funcitons to apply a blur

# blur()
# gaussainblur()
# medianblur()
# bilatarealFilter()

# you will be replacing every single pixel with the average of the pixels around it

img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/Screenshot 2023-09-11 130453.png")

b_size = 9 # how strong is teh blur # must be a odd number
blur = cv2.blur(img,(9,9))

gauss = cv2.GaussianBlur(img, (9,9), 3) # img, tuple size - img,height - and how much blut

medi = cv2.medianBlur(img, 9) #img, odd number


# how to remove the noise from a image
img = cv2.imread("C:/Users/lilha/Desktop/CommaPrep/download.jpg")
# you use the blur to blend the noise with the background - nothing new
#median blur is best

cv2.imshow('img', gauss)
cv2.waitKey(0)