import cv2
import numpy as np

img = cv2.imread('Images/girl.jpg')
cv2.imshow('Original',img)

blank = np.zeros(img.shape[:2],dtype='uint8')  # Dimensions of the mask must be the same
# cv2.imshow('Blank',blank)

mask = cv2.circle(blank,(blank.shape[1]//2+45,blank.shape[0]//2),50,255,-1)
cv2.imshow('Mask',mask)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked Image',masked)

cv2.waitKey(0)