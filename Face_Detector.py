import cv2
import numpy as np

cam = cv2.VideoCapture(0)

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3,5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),3)

    cv2.imshow('Webcamku', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('a'):
        break
cam.release()
cv2.destroyAllWindows()