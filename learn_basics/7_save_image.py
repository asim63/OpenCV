import cv2

img = cv2.imread("images/park.png")

img_crop = img[0:400, 0:500]

cv2.imwrite('images/saved_image.png',img_crop)

cv2.imshow("window",img_crop)
cv2.waitKey(0)