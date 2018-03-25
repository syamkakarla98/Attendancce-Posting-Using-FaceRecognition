import cv2
import numpy as np
import sqlite3
cam=cv2.VideoCapture(0);
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
def insertorupdate(id,name,gender,section):
    conn=sqlite3.connect('FaceBase.db')
    cmd='select * from people where id='+str(id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd='update people set name='+str(name)+'where id='+str(id)
    else:
        cmd='insert into people(id,name,gender,section) values('+str(id)+','+str(name)+','+str(gender)+','+str(section)+')'
    conn.execute(cmd)
    conn.commit()
    conn.close()
id=input('\nEnter your ID :')
name=input('\nEnter your Name :')
gender=input('\nEnter your Gender :')
section=input('\nEnter your Section or Department:')
insertorupdate(id,name,gender,section)
sn=0                    # sample number
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sn=sn+1
        cv2.imwrite('Datasets/User'+'.'+str(id)+'.'+str(sn)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100)
    cv2.imshow('Face',img)
    cv2.waitKey(1)
    if sn>29 :
        break
cam.release()
cv2.destroyAllWindows()
