import cv2
import numpy as np

# These are the XML classifiers.
# haarcascade_frontalface_default.xml is used for frontsal face detection.

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

# To start video capturing.
cam=cv2.VideoCapture(0);


while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,140,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
    cv2.imshow('Face',img)
    if cv2.waitKey(10)==ord('q') :  # Press 'q' to quit.
        break
cam.release()
cv2.destroyAllWindows()
 
