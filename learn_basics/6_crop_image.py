import cv2


img = cv2.imread("images/park.png")

img_crop = img[100:300,200:500] # img[height,width]

cv2.imshow("window",img_crop)
cv2.waitKey(0)