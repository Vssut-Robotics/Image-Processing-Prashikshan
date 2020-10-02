import cv2      ##importing computer vision lib
import numpy    ##importing numpy

def Function_A():
    
    x = cv2.imread('image1.jpg')      ##Reading images
    y = cv2.imread('image2.jpg.png')
    print('rows,columns and channels of two images respectively are:')
    print(x.shape)                    ##Finging co-ordinates
    print(y.shape)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Function_B():                         
    
    x = cv2.imread('image1.jpg')      ##Reading images
    y = cv2.imread('image2.jpg.png')
      ##centre co-ordinates calculated by finding no. of rows and columns
      ##using img.shape function
      ##we can access the central co-ordinates by rows/2 ,cols/2
    centre_x = x[473 ,640]            ##Picking central intencities 
    centre_y = y[322 ,488]
    print('central intencity of two images respectively in the BGR order are:')
    print(centre_x)
    print(centre_y)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Function_C():

    import cv2
    import numpy

    x = cv2.imread('image1.jpg') 
    y = cv2.imread('image2.jpg.png')

    gray1 = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(y,cv2.COLOR_BGR2GRAY)

    ret ,th1 = cv2.threshold(gray1,200,255,cv2.THRESH_BINARY)##Thresholding of img 1
    ret ,th2 = cv2.threshold(gray2,200,255,cv2.THRESH_BINARY)##and img 2

    contours1, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)##Finding contours of
    contours2, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)##image1 and 2
    cv2.drawContours(x, contours1, -1, (0,255,0), 3)##Drawing all contours
    cv2.drawContours(y, contours2, -1, (0,255,0), 3)

##Looping for finding areas and perimeters of each contour of two images
    a = 1
    for i in contours1 : 
        area = cv2.contourArea(i)
        perimeter = cv2.arcLength(i, True)
        print('First image shape',a,'area =',area)##Printing areas of contours of image 1 
        print('First image shape',a,'Perimeter =',perimeter)##Prints perimeters of contours of image 1
        a  += 1
    
    b = 1    
    for i in contours2 : 
        area = cv2.contourArea(i)
        perimeter = cv2.arcLength(i, True)
        print('Second image shape',b,'area =',area)##Printing areas of contours of image 2
        print('second image shape',b,'Perimeter =',perimeter)##Prints perimeters of contours of image 2
        b  += 1


    cv2.imshow('All_contours1', x)  ##Showing all contours
    cv2.imshow('All contours2', y)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Function_D():

    import cv2
    import numpy

    x = cv2.imread('image1.jpg')        ##Reading
    y = cv2.imread('image2.jpg.png')

    gray1 = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY) ##Gray conversion
    gray2 = cv2.cvtColor(y,cv2.COLOR_BGR2GRAY)

    ret ,th1 = cv2.threshold(gray1,200,255,cv2.THRESH_BINARY) ##Thresholding
    ret ,th2 = cv2.threshold(gray2,200,255,cv2.THRESH_BINARY)

    contours1, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) ##Contour finding
    contours2, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

##length = len(contours)

    Max_area1 = 0
    for i in range(1,len(contours1)) :      ##Looping to fing largest shape in image 1 excluding boundary 
        area = cv2.contourArea(contours1[i])##of image 1
        if area > Max_area1:
            Max_area1 = area
            Max = i
    Max_perimeter1 = cv2.arcLength(contours1[Max], True)        
    print("Area of largest shpe in image1 is =",Max_area1) ##Printing max area and perimeters of largest shape
    print("Perimeter of largest shape in image1 is =",Max_perimeter1)
   
    Max_area2 = 0
    for i in range(1,len(contours2)) :       ##Looping to fing largest shape in image 1 excluding boundary 
        area = cv2.contourArea(contours2[i]) ##of image 2
        if area > Max_area2:
            Max_area2 = area
            Max = i
    Max_perimeter2 = cv2.arcLength(contours2[Max], True)        
    print("Area of largest shpe in image2 is =",Max_area2)  ##Printing max area and perimeters of largest shape
    print("Perimeter of largest shape in image2 is =",Max_perimeter2)    

    cv2.drawContours(x, contours1, Max, (0,255,0), 3) ##Drawing contours
    cv2.drawContours(y, contours2, Max, (0,255,0), 3)

    cv2.imshow('Max_contour1', x)
    cv2.imshow('Max_contour2', y)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Function_E():

    x = cv2.imread('image1.jpg')      ##Reading images
    y = cv2.imread('image2.jpg.png')

    gray1 = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY) ##Converrting to grayscale
    gray2 = cv2.cvtColor(y,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('gray1',gray1)
    cv2.imshow('gray2',gray2)
    print('Gray images')
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Function_F():
    
    x = cv2.imread('image1.jpg')       ##Reading images
    y = cv2.imread('image2.jpg.png')

    x[:,:,0] = 0    ##setting green and blue channels zero
    x[:,:,1] = 0
    y[:,:,0] = 0
    y[:,:,1] = 0
    cv2.imshow('red_1',x)
    cv2.imshow('red_2',y)
    print("Red images")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

print('Initiating FUNCTION calling :')
print("\nFunction_A")
Function_A()
print("\nFunction_B")
Function_B()
print("\nFunction_C")
Function_C()
print("\nFunction_D")
Function_D()
print("\nFunction_E")
Function_E()
print("\nFunction_F")
Function_F()
