import cv2,os
import numpy as np
from PIL import Image
import pickle
import sqlite3

def getprofileId(id):
    conn=sqlite3.connect('FaceBase.db')
    cmd='select * from people where id='+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

def postattendence(id):
    att='Present'
    conn=sqlite3.connect('FaceBase.db')
    cmd='select * from attendence where id='+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd='update people set name='+str(name)+'where id='+str(id)
    conn.execute(cmd)
    conn.commit()
    conn.close()

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
path='Datasets'

rec = cv2.face.LBPHFaceRecognizer_create();
rec.read('recognizer\\trainer.yml')
id=0
font=cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getprofileId(id)
        postattendence(id)
        if profile != None:
            cv2.putText(img,'Hiii\nName    :'+str(profile[1]),(x,y+h+20),font,1,(0,0,255),2)
            cv2.putText(img,'AttendenceStatus :'+str(profile[2]),(x,y+h+80),font,1,(0,0,255),2)
    cv2.imshow('Face',img)
    if cv2.waitKey(20)==ord('q') :
        break
cam.release()
cv2.destroyAllWindows()
