import cv2
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv2.circle(blank.copy(),(200,200),200,255,-1)
cv2.imshow("Rectangle",rectangle)
cv2.imshow("Circle",circle)

# Bitwise AND
bitwize_AND = cv2.bitwise_and(rectangle,circle)
cv2.imshow('AND',bitwize_AND)
 
# Bitwise OR
bitwize_OR = cv2.bitwise_or(rectangle,circle)
cv2.imshow('OR',bitwize_OR)
 
# Bitwise NOT
bitwize_NOT = cv2.bitwise_not(circle)
cv2.imshow('NOT',bitwize_NOT)
 
# Bitwise XOR
bitwize_XOR = cv2.bitwise_xor(rectangle,circle)
cv2.imshow('XOR',bitwize_XOR)
 
cv2.waitKey(0)