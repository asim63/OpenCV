import cv2
import numpy as np

img = cv2.imread("images/park.png")
temp_img = img.copy()
flag = False
ix = -1
iy = -1

def crop(event,x,y,flags,params):
    global flag, ix, iy, img, temp_img
    
    # print(event)
    if event == 1:
        flag = True
        ix = x
        iy = y
        temp_img = img.copy()
        
    elif event == 0:
        if flag:
            img = temp_img.copy() # in order to restore the original image (live rectangle)
            cv2.rectangle(img,pt1 = (ix,iy), pt2 = (x,y), color = (0,255,0), thickness = 1)
    
    elif event == 4:
        flag = False
        img = temp_img.copy()
        cv2.rectangle(img,pt1 = (ix,iy), pt2 = (x,y), color = (0,255,0),thickness = 1)
        x1, x2 = sorted([ix,x])
        y1, y2 = sorted([iy,y])
        cropped_image = img[y1+1:y2, x1+1:x2] # img[top:bottom, left:right]
        if cropped_image.size > 0:
            cv2.imwrite("images/cropped_image.png",cropped_image) 
            print("Saved:",cropped_image.shape)
        
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)
while True:
    cv2.imshow("window",img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()