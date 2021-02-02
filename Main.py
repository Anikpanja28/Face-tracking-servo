import cv2
import numpy as np
import serial

port = serial.Serial('COM4',9600)
face_cas = cv2.CascadeClassifier('C:/Users/PAVILION/AppData/Local/Programs/Python/Python36/attendance/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
cap.set(3, 480)
cap.set(4, 320)
_, frame = cap.read()
rows, cols, _ = frame.shape
x_medium = int(cols / 2)
center = int(cols / 2)
position = 90 # degrees
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x,y,w,h) in faces:
        x_medium = int((x+x+w)/2)
        
        break
    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    if x_medium < center -30:
        position += 1
        
    elif x_medium > center +30:
        position -= 1
       
        
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        #roi_gray = gray[y:y + h, x:x + w]
        #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),10);
        #cv2.putText(img,str('Welcome!!!'),(x,y-10),font,1,(120,255,120),1)
    port.write(repr(position).encode('utf-8'))
    cv2.imshow('Detect', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 
