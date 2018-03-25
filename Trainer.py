import os
import numpy as np
import cv2

from PIL import Image

# Some how the method cv2.createLBPHFaceRecognizer() is not working.

recognizer = cv2.face.LBPHFaceRecognizer_create();
path='Datasets'

def getImagewithId(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        Id=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(Id)
        Ids.append(Id)
        cv2.imshow('Training',faceNp)
        cv2.waitKey(10)
    return np.array(Ids),faces


Ids,faces=getImagewithId(path)

recognizer.train(faces,Ids)
recognizer.save('recognizer/trainer.yml')
cv2.destroyAllWindows()
