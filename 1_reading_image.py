import cv2
import numpy as np

#read
img = cv2.imread("images/park.png")

print(type(img))
print(img.shape) #has 3 channels R,G,B (0-255)*3
# print(img)

#to show the image
cv2.imshow("window",img)
cv2.waitKey(0)  #for delay


