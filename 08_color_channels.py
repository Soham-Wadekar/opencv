import cv2
import numpy as np

img = cv2.imread('Images/chair.jpg')
cv2.imshow('Original',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv2.split(img)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)

merged = cv2.merge([b,g,r])
cv2.imshow('Merged',merged)

blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('Blue Merged',blue)
cv2.imshow('Green Merged',green)
cv2.imshow('Red Merged',red)

cv2.waitKey(0)