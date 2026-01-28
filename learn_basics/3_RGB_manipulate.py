import cv2
import numpy as np

#read
img = cv2.imread("images/park.png")


img2 = img.copy()
img2[:,:,0]=0  # removes blue component; image becomes yellowish
imgBlue = img[:,:,0] #select blue
imgGreen = img[:,:,1] #select Green
imgRed = img[:,:,2] #select red

img_final = np.hstack((imgBlue,imgGreen,imgRed))
#show
cv2.imshow("window",img2)

cv2.imshow("window2",img_final)
cv2.waitKey(0)  #for delay


