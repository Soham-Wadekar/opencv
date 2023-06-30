import cv2

img = cv2.imread('Images/chair.jpg')
cv2.imshow('Original',img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',img_gray)

# Simple Thresholding
threshold, thresh = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
cv2.imshow('Simple Thresholding',thresh)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,3)
cv2.imshow('Adaptive Thresholding',adaptive_thresh)

cv2.waitKey(0)