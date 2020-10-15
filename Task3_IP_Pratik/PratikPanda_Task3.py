import cv2
import numpy as np


# Dummy Function
def nothing(x):
    # any operation
    pass


# Get Video From Cam
cap = cv2.VideoCapture(0)
# Create TrackBar
cv2.namedWindow("Track-bar")
cv2.createTrackbar("L-H", "Track-bar", 0, 255, nothing)
cv2.createTrackbar("L-S", "Track-bar", 0, 255, nothing)
cv2.createTrackbar("L-V", "Track-bar", 0, 255, nothing)
cv2.createTrackbar("U-H", "Track-bar", 255, 255, nothing)
cv2.createTrackbar("U-S", "Track-bar", 255, 255, nothing)
cv2.createTrackbar("U-V", "Track-bar", 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Get Reading From TrackBar
    l_h = cv2.getTrackbarPos("L-H", "Track-bar")
    l_s = cv2.getTrackbarPos("L-S", "Track-bar")
    l_v = cv2.getTrackbarPos("L-V", "Track-bar")
    u_h = cv2.getTrackbarPos("U-H", "Track-bar")
    u_s = cv2.getTrackbarPos("U-S", "Track-bar")
    u_v = cv2.getTrackbarPos("U-V", "Track-bar")

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    # Create Masks
    mask = cv2.inRange(hsv, lower, upper)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # Find The Contours in the Image
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Calculate The Area of Each Contour
        area = cv2.contourArea(cnt)

        # Use Approximation to minimize the Vertices of contour
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # Draw the contour on Original Image if Area > 400 to avoid noise
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 3)

    # We Show The Contours on the Original Image
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # If Esc Key is Pressed Program Terminates
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
