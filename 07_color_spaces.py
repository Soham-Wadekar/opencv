import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Images/chair.jpg')
cv2.imshow('Original',img)

# plt.imshow(img)
# plt.show()

# Grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',img_gray)

# HSV
img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',img_HSV)

# LAB
img_LAB = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow('LAB',img_LAB)

# RGB
img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',img_RGB)

cv2.waitKey(0)