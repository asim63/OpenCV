import cv2
import numpy as np

img = np.ones((512,512,3))

flag = False
ix = -1
iy = -1

def draw(event,x,y,flags,params):
    # if (event == 0):
    #     print("Mouse moved")
    # if(event == 1):
    #     print("CLicked")
    # if(event == 4):
    #     print("Released")
    global flag, ix,iy
    
    if event == 1:
       flag = True
       ix = x
       iy = y
       
       
    elif event == 0:
        if flag == True:
            cv2.rectangle(img, pt1 = (ix,iy), pt2 = (x,y), color = (0,255,0),thickness = -1)
    elif event == 4:
        flag = False
        cv2.rectangle(img, pt1 = (ix,iy), pt2 = (x,y), color = (0,255,0),thickness = -1)

cv2.namedWindow(winname = "window")
cv2.setMouseCallback("window",draw)
while True:
    
    cv2.imshow("window",img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'): #the window will not be shown only if 'x' is pressed
        break  #the 0xFF keeps only the last 8 bits (waitkey(1) might return extra bits depending on OS/platform thats why)

cv2.destroyAllWindows()