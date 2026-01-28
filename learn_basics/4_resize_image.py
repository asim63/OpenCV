import cv2
import numpy as np

#read
img = cv2.imread("images/park.png")

print(img.shape)

img_resize = cv2.resize(img,(400,400))
print(img_resize.shape)

img_resize2 = cv2.resize(img,(800,800))
print(img_resize2.shape)

#you dont know the size of image but want to reduce the size by 50%
img_half = cv2.resize(img,(img.shape[1]//2, img.shape[0]//2))
print(img_half.shape)

cv2.imshow("window2",img_half)
cv2.waitKey(0)  #for delay


