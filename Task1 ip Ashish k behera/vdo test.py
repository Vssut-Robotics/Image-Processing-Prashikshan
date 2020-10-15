import cv2
import numpy

cap = cv2.VideoCapture('ashu.mp4')

while(True):
    ret, cam = cap.read()

    cv2.imshow('video',cam)

    if cv2.waitKey(1) == ord('q'):
        break
    

cv2.destroyAllWindows()
cap.release()
