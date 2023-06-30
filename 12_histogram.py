import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Images/chair.jpg')
# cv2.imshow('Original',img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale',img_gray)

gray_hist = cv2.calcHist([img_gray],[0],None, [256],[0,256])

# plt.figure()
# plt.plot(gray_hist,'gray')
# plt.xlabel('Bins'),plt.ylabel('No. of Pixels')
# plt.title('Grayscale Histogram')
# plt.xlim(0,256)
# plt.show()

colors = ('b','g','r')
plt.figure()
plt.xlabel('Bins'),plt.ylabel('No. of Pixels')
plt.title('Color Histogram')
plt.xlim(0,256)
for i, col in enumerate(colors):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    
plt.show()

cv2.waitKey(0)