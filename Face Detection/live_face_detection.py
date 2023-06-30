import cv2

capture = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'Haarcascade_frontalface_default.xml')
while True:
    isTrue, frame = capture.read()              
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(frame_gray, 1.1, 9)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame,"Person",(x,y-3),cv2.QT_FONT_NORMAL,0.8,(0,0,255),thickness=1)

    cv2.imshow('Video',frame)   
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()