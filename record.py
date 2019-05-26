import numpy as np
import cv2
import os
cap = cv2.VideoCapture('b.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('toi_2.avi',fourcc, 30.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
