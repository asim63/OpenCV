import cv2
import numpy as np

img = np.ones((512,512,3)) #creating a black image(intensity = 0; black)


#RECTANGLE  
cv2.rectangle(img,pt1=(100,100),pt2=(400,400),color = (0,0,0),thickness= 3) #note in color its B-G-R so the rectangle will be red
#thickness = -1, will fill


#CIRCLE
cv2.circle(img,center = (250,250),radius = 150,color = (0,255,0),thickness = -1)

#LINE
cv2.line(img,pt1 = (250,100), pt2 = (400,250), color=(250,0,0), thickness= 3 )
cv2.line(img,pt1 = (250,400), pt2 = (400,250), color=(250,0,0), thickness= 3 )
cv2.line(img,pt1 = (250,400), pt2 = (100,250), color=(250,0,0), thickness= 3 )
cv2.line(img,pt1 = (100,250), pt2 = (250,100), color=(250,0,0), thickness= 3 )

#TEXT
cv2.putText(img,org=(135,270),fontScale=2, color=(255,0,255),thickness = 2, lineType=cv2.LINE_AA, text ="BEN 10", fontFace=cv2.FONT_HERSHEY_SIMPLEX)


cv2.imshow("window",img)

cv2.waitKey(0)


