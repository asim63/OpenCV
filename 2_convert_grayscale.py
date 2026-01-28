import cv2
import numpy as np

#read
img = cv2.imread("images/park.png")

#convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)
#show
cv2.imshow("window",img_gray)
cv2.waitKey(0)  #for delay


