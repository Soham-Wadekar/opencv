# Detecting contours

import cv2
import numpy as np

img = cv2.imread('Images/chair.jpg')
cv2.imshow('Original',img)

blank = np.zeros(img.shape,dtype='uint8')
cv2.imshow('Blank',blank)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Method 1
# blur = cv2.GaussianBlur(img_gray,(3,3),cv2.BORDER_DEFAULT)

# canny = cv2.Canny(blur,125,175)
# cv2.imshow('Canny',canny)
# contours, hierarchies = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# print(f"{len(contours)} contours found")

# Method 2
ret, thresh = cv2.threshold(img_gray,125,255,cv2.THRESH_BINARY)
cv2.imshow('Thresh',thresh)

contours, hierarchies = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found")

cv2.drawContours(blank,contours,-1,(0,0,255),1)
cv2.imshow('Contours Drawn',blank)

cv2.waitKey(0)