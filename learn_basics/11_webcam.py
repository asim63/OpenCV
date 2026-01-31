import cv2
import numpy as np

cap = cv2.VideoCapture(0) #put path of video in place of 0 if you want to get video as output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi",fourcc,30.0,(640,480))
while True:
    
    ret , frame = cap.read()
    out.write(frame)
    #new_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0xff == ord('x'):
        break
    
out.release()    
cv2.destroyAllWindows()