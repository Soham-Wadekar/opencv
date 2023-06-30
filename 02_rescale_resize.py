import cv2

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

def changeRes(width,height):    # Only works for live videos (webcam,other cameras)
    capture.set(3,width)
    capture.set(4,height)       # Properties of the capture class - 3: width, 4:height

# img = cv2.imread('Images/chair.jpg')
# cv2.imshow('Chair',img)
# resized_image = rescaleFrame(img)
# cv2.imshow('Chair2',resized_image)

# Reading Video
# ====================================#
# Unhash it while running
capture = cv2.VideoCapture(0)     # For webcam, cv.CaptureVideo(0)

while True:
    isTrue, frame = capture.read()              # We read the video frame by frame
    frame_resized = rescaleFrame(frame)
    cv2.imshow('Video',frame)
    cv2.imshow('Video Resized',frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('d'):             # To not let the video play indefinitely, press D
        break

capture.release()
cv2.destroyAllWindows()