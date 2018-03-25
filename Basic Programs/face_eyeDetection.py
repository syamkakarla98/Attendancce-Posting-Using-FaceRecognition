import cv2
import numpy as np

# These are the XML classifiers.
# haarcascade_frontalface_default.xml is used for frontsal face detection.

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

# haarcascade_eye.xml is used for eye detection in face.

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# To start video capturing.
cam=cv2.VideoCapture(0);


while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Face',img)
    if cv2.waitKey(10)==ord('q') :
        break
cam.release()
cv2.destroyAllWindows()
