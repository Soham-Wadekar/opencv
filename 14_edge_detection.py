import cv2
import numpy as np

img = cv2.imread('Images/chair.jpg')
cv2.imshow('Original',img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',img_gray)

# Laplacian Method
lap = cv2.Laplacian(img_gray,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian',lap)

# Sobel Method
sobelx = cv2.Sobel(img_gray,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img_gray,cv2.CV_64F,0,1)

sobel = cv2.bitwise_or(sobelx,sobely)

# Canny
canny = cv2.Canny(img_gray,150,175)
cv2.imshow('Canny',canny)

cv2.imshow('Sobel X',sobelx)
cv2.imshow('Sobel Y',sobely)
cv2.imshow('Sobel',sobel)

cv2.waitKey(0)