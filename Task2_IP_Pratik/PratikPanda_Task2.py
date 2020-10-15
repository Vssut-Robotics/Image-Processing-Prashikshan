import numpy as np
import cv2 as cv


def a(img):
    print("Function A")
    image = cv.imread(img)
    info = image.shape
    print("Rows:", info[0], " Columns:", info[1], " Channels:", info[2])
    return info[0], info[1]


def b(img):
    print("\nFunction B")
    image = cv.imread(img)
    info = image.shape
    y = int(info[0] / 2)
    x = int(info[1] / 2)
    _blue = image[y, x, 0]
    _green = image[y, x, 1]
    _red = image[y, x, 2]
    print("Intensity at center(RGB):", _red, _green, _blue)


def c(img):
    print("\nFunction C")
    image = cv.imread(img)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 170, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0, 0, 0), 3)
    cnt = contours
    i=1
    for x in cnt:
        area = cv.contourArea(x)
        perimeter = cv.arcLength(x, True)
        print(f"Area of Contour {i}: is {area} and Perimeter is {perimeter}")
        i += 1
    cv.imshow('Contours', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def d(img):
    print("\nFunction D")
    image = cv.imread(img)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 170, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    max_area = 0
    for x in range(1, len(contours)):
        area = cv.contourArea(contours[x])
        if area > max_area:
            max_area = area
            num = x
    cv.drawContours(image, contours, num, (0, 0, 0), 3)
    area = cv.contourArea(contours[num])
    perimeter = cv.arcLength(contours[num], True)
    print("Area of Largest Shape:", area, "\nPerimeter of Largest Shape:", perimeter)
    cv.imshow('Largest Contour', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def e(img):
    image = cv.imread(img)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('Grayscale', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()


def f(img):
    image = cv.imread(img)
    red = image.copy()
    # set blue and green channels to 0
    red[:, :, 0] = 0
    red[:, :, 1] = 0

    cv.imshow('R-RGB', red)
    cv.waitKey(0)
    cv.destroyAllWindows()


print("\nImage 1")
a('Image1.jpg')
b('Image1.jpg')
c('Image1.jpg')
d('Image1.jpg')
e('Image1.jpg')
f('Image1.jpg')

print("\nImage 2")
a('Image2.png')
b('Image2.png')
c('Image2.png')
d('Image2.png')
e('Image2.png')
f('Image2.png')
