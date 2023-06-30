# Importing OpenCV package
import cv2

# Reading the image
img = cv2.imread('./Images/friends.jpg')

# Converting image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'Haarcascade_frontalface_default.xml')

# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(img_gray, 1.1, 3)
print(f"No. of faces detected: {len(faces_rect)}")

# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)