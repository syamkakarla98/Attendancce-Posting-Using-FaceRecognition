# FACE DETECTION OF AN IMAGE


import cv2
import numpy as np


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

img = cv2.imread('sarma.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceDetect.detectMultiScale(gray,1.3,5)
while True:
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Face',img)
    if cv2.waitKey(20)==ord('q') :
        break
cv2.destroyAllWindows()

