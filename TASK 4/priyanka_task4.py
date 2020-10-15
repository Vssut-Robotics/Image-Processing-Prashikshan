import cv2 as cv
import numpy as np
from math import acos
from math import pi
from math import sqrt
def imag(x):
    img= cv.imread(x)
    gray1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,thresh=cv.threshold(gray1,200,300,0)
    contours,hierarchy=cv.findContours(thresh,1,2)
    cnt= contours[0]
    M=cv.moments(cnt)
    cx= int(M['m10']/M['m00'])
    cy= int(M['m01']/M['m00'])
    lr=np.array([0,0,220])
    ur=np.array([10,10,255])
    mask=cv.inRange(img,lr,ur)
    ret,thresh1=cv.threshold(mask,200,300,0)
    contours1,hierarchy=cv.findContours(thresh1,1,2)
    cnt1=contours1[0]
    M1=cv.moments(cnt1)
    cx1= int(M1['m10']/M1['m00'])
    cy1= int(M1['m01']/M1['m00']) 
    lg=np.array([0,220,0])
    ug=np.array([10,255,10])
    mask1=cv.inRange(img,lg,ug)
    ret,thresh2=cv.threshold(mask1,200,300,0)
    contours2,hierarchy=cv.findContours(thresh2,1,2)
    cnt2=contours2[0]
    M2=cv.moments(cnt2)
    cx2= int(M2['m10']/M2['m00'])
    cy2= int(M2['m01']/M2['m00'])
    v1=[(cx1-cx),(cy1-cy)]
    v2=[(cx2-cx),(cy2-cy)]
    cosy=((v1[0]*v2[0])+(v1[1]*v2[1]))/(sqrt(v1[0]**2 + v1[1]**2)*sqrt(v2[0]**2 + v2[1]**2))
    rad=acos(cosy)
    y=(rad*180/pi)
    print("the angle in"+" " + x +" "+"is" +" "+ str(round(y,2))+"degree")
    cv.waitKey(0)
    cv.destroyAllWindows()

imag("image_1.png")
imag("image_2.png")
imag("image_3.png")
    

    
