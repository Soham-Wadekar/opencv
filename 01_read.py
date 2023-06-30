import cv2

# Reading Images
# ====================================#
# Unhash it while running
# Write cv.imread(path,0) for grayscale
img = cv2.imread('Images/chair.jpg')
cv2.imshow('Original',img)

cv2.waitKey(0)   # Waits for an infinite amount of time for a keyboard key to be pressed.
# ====================================#

# Reading Video
# ====================================#
# Unhash it while running
# capture = cv2.VideoCapture('Videos\stationery.mp4')     # For webcam, cv.CaptureVideo(0)

# while True:
#     isTrue, frame = capture.read()              # We read the video frame by frame
#     cv2.imshow('Video',frame)

#     if cv2.waitKey(20) & 0xFF==ord('d'):             # To not let the video play indefinitely, press D
#         break

# capture.release()
# cv2.destroyAllWindows()
# ====================================#