import cv2
import numpy as np

img = cv2.imread('Images/broccoli house.jpg')  
cv2.imshow('Original',img)

# Translation
def translate(img, x, y):
    '''
    -x --> Left
    -y --> Up
    x --> Right
    y --> Down
    '''
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img, transMatrix, dimensions)

translated = translate(img,40,60)
# cv2.imshow("Translated",translated)

# Rotation
def rotate(img,angle,rotation_point=None):
    height, width = img.shape[:2]

    if rotation_point==None:
        rotation_point=(width//2,height//2)

    rotMatrix = cv2.getRotationMatrix2D(rotation_point,angle,scale=1.0)
    dimensions = width,height
    return cv2.warpAffine(img,rotMatrix,dimensions)

rotated = rotate(img,30)
# cv2.imshow('Rotated',rotated)

# Resizing
resized = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
'''
cv2.INTER_CUBIC/cv2.INTER_LINEAR for enlarging
cv2.INTER_AREA for shrinking
'''
# cv2.imshow('Resized',resized)

# Flipping
flip = cv2.flip(img, 0)
'''
flipCode takes 3 values: 0, 1 ,-1
0 --> Flips vertically
1 --> Flips horizontally
-1 --> Flips both vertically and horizontally
'''
cv2.imshow("Flipped",flip)

cv2.waitKey(0)