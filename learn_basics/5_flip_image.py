import cv2
import numpy as np

#read
img = cv2.imread("images/park.png")

#verticle_flip
img_flip = cv2.flip(img,0) 

#horizontal_flip
img_flip2 = cv2.flip(img,1) 

cv2.imshow("window1",img_flip2)
cv2.waitKey(0)  #for delay


