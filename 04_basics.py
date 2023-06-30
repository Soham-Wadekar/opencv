import cv2

img = cv2.imread('Images/chair.jpg')
cv2.imshow("Original",img)

# Convert image to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscale",img_gray)

# Blur an image
blur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
# cv2.imshow("Blurred",blur)

# Edge Cascade
canny = cv2.Canny(blur, 125,175)
# cv2.imshow("Canny",canny)

# Dilate the image
dilated = cv2.dilate(canny,(7,7),iterations=3)
# cv2.imshow("Dilated",dilated)

# Erode the image
eroded = cv2.erode(dilated,(7,7),iterations=3)
# cv2.imshow("Eroded",eroded)

# Resize the image
resized = cv2.resize(img,(300,400),interpolation=cv2.INTER_LINEAR)
# cv2.imshow("Resized",resized)

# Cropping
cropped = img[50:200,100:400]
# cv2.imshow("Cropped",cropped)

cv2.waitKey(0)