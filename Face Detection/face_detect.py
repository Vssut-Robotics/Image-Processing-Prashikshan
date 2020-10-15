# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:57:30 2020

@author: LENOVO
"""

import cv2

#importing haarcascades_frontal_face_dataset

face_data = r"C:\Users\LENOVO\Desktop\VSSUT_BURLA_2\datasets\data\haarcascades\haarcascade_frontalface_default.xml"

#importing_image
face_img = cv2.imread(r"C:\Users\LENOVO\Desktop\image-2-u19-indian-cricket-team-87ff.jpg")
cv2.imshow("kohli",face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

classifier = cv2.CascadeClassifier(face_data) #training

#extracting the face co-ordinate points
faces = classifier.detectMultiScale(face_img)

for x,y,w,h in faces:
    cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,0,255),2)
    
cv2.imshow("india",face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


