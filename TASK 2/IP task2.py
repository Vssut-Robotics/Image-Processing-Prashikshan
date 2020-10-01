import cv2 as cv
import numpy as np
img1= cv.imread("Image1.jpg")
img2= cv.imread("Image2.png")
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret,thresh1=cv.threshold(gray1,200,300,0)
ret,thresh2=cv.threshold(gray2,200,300,0)
contours1,hierarchy=cv.findContours(thresh1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours2,hierarchy=cv.findContours(thresh2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt1=contours1[0]
cnt2=contours2[0]
M1=cv.moments(cnt1)
M2=cv.moments(cnt2)
cx1=int(M1['m10']/M1['m00'])
cy1=int(M1['m01']/M1['m00'])
cx2=int(M2['m10']/M2['m00'])
cy2=int(M2['m01']/M2['m00'])
area1=[]
area2=[]
def funcA():
    print("NO. OF ROWS,COLUMNS AND CHANNELS :")
    print("image 1")
    print(img1.shape)
    print("image 2")
    print(img2.shape)


def funcB():
    print("THE VALUE OF INTENSITY IN RED,GREEN AND BLUE ORDER AT THE CENTRE:")
    print("image 1")
    px=img1[cx1,cy1,(2,1,0)]
    print(px)
    print("image 2")
    qx=img2[cx2,cy2,(2,1,0)]
    print(qx)
    

def funcC():
    cv.drawContours(img1,contours1,-1,(0,255,0),3)
    cv.drawContours(img2,contours2,-1,(0,255,0),3)
    cv.imshow("image1",img1)
    cv.imshow("image2",img2)
    print("Image 1:") 
    for i in range(len(contours1)):
       print("Area of contour"+str(i+1)+"=",cv.contourArea(contours1[i]))
       print("Perimeter of contour"+str(i+1)+"=",cv.arcLength(contours1[i],True))
    print("Image 2:") 
    for i in range(len(contours2)): 
       print("Area of contour"+str(i+1)+"=",cv.contourArea(contours2[i]))
       print("Perimeter of contour"+str(i+1)+"=",cv.arcLength(contours2[i],True))
    
def funcD():
    ig1= cv.imread("Image1.jpg")
    ig2= cv.imread("Image2.png")
    for i in range(1,len(contours1)):
       x=cv.contourArea(contours1[i])
       area1.append(x)
    print("image 1:")
    print("maximum area =",max(area1))
    m=int(area1.index(max(area1)))
    print("it's perimeter=",cv.arcLength(contours1[m+1],True))
    cv.drawContours(ig1,contours1,m+1,(0,255,0),3)
    cv.imshow("imag1",ig1)
    for i in range(1,len(contours2)): 
       u=cv.contourArea(contours2[i])
       area2.append(u)
    print("image 2:")
    print("maximum area 2 =",max(area2))
    n=int(area2.index(max(area2)))
    print("it's perimeter =",cv.arcLength(contours2[n+1],True))
    cv.drawContours(ig2,contours2,n+1,(0,255,0),3)
    cv.imshow("imag2",ig2)
def funcE():
    cv.imshow("picture1",gray1)
    cv.imshow("picture2",gray2)

def funcF():
    r1=img1.copy()
    r2=img2.copy()
    r1[:,:,0]=0
    r1[:,:,1]=0
    r2[:,:,0]=0
    r2[:,:,1]=0
    cv.imshow("photo1",r1)
    cv.imshow("photo2",r2)

    
funcA()
funcB()
funcC()
funcD()
funcE()
funcF()
cv.waitKey(0)
cv.destroyAllWindows()


 
