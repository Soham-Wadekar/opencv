import cv2

img = cv2.imread('Images/chair.jpg')
cv2.imshow('Original',img)

# Averaging
avg_blur = cv2.blur(img,(7,7))
cv2.imshow('Average Blurring',avg_blur)

# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian Blurring',gaussian_blur)

# Median Blur
median_blur = cv2.medianBlur(img,3)
cv2.imshow('Median Blurring',median_blur)

# Bilateral Blurring
bilateral_blur = cv2.bilateralFilter(img, 9, 30, 15)
cv2.imshow('Bilateral Blurring',bilateral_blur)

cv2.waitKey(0)