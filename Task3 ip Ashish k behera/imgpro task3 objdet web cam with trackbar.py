import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0);

cv2.namedWindow('Tracking')
##creating new window to adjust  upper and lower ranges of hsv values
cv2.createTrackbar('LH','Tracking', 0, 255,nothing)##track for lower hew(window name,window location,start value,end value,callnback function)
cv2.createTrackbar('LS','Tracking', 0, 255,nothing)##lowersaturation
cv2.createTrackbar('LV','Tracking', 0, 255,nothing)##lowervalue
cv2.createTrackbar('UH','Tracking', 255, 255,nothing)##upperhew
cv2.createTrackbar('US','Tracking', 255, 255,nothing)##uppersaturation
cv2.createTrackbar('UV','Tracking', 255, 255,nothing)##uppervalue


while True:
    ##frame = cv2.imread('')
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)
    ##getting values from track bar
    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
    
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')
    ##thresholding hsv img in range of blue color
    l_b = np.array([l_h,l_s,l_v])##lower range ##this will be done more precisingly using track bar
    u_b = np.array([u_h,u_s,u_v])##upper range([hew,saturation,value])
    ##thresholding hsv img to only get blue color
    
    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask= mask )##sourse1,sourse2,masking value of lower and upper blue(here)
    
    cv2.imshow('frame',frame)

    cv2.imshow('mask',mask)

    cv2.imshow('res',res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
    
