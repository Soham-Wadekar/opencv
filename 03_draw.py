import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('Blank',blank)

# 1. Paint the entire image a certain color
# blank[:] = 0,255,0                      # BGR
# cv2.imshow('Green',blank)

# 2. Paint some part of the image a certain color
# blank[200:300,300:400] = 0,255,0
# cv2.imshow('Specific coloration',blank)

# 3. Draw a rectangle
# cv2.rectangle(blank, (100,100),(300,200),(0,0,255),thickness=2)
# cv2.rectangle(blank, (50,50),(200,400),(0,255,0),thickness=2)
# cv2.rectangle(blank, (400,400),(500,500),(0,255,255),thickness=cv2.FILLED)  #Fill the rectangle (or we can specify thickness=-1 to fill the shape)
# cv2.imshow("Rectangle",blank)

# 4. Draw a circle
# cv2.circle(blank,(250,250),100,(255,255,255),thickness=5)
# cv2.circle(blank,(400,400),30,(0,0,255),thickness=-1)
# cv2.imshow("Circle",blank)

# 5. Draw a line
# cv2.line(blank,(0,200),(500,400),(0,255,0),thickness=3)
# cv2.imshow("Line",blank)

# 6. Add text on an image
cv2.putText(blank,"Soham",(75,250),cv2.FONT_HERSHEY_PLAIN,5,(0,255,0),thickness=2)
cv2.imshow("Text",blank)

cv2.waitKey(0)