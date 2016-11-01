import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    topSize = len(frame)/2
    lowerSize = len(frame[len(frame)/2])/2
    print frame[topSize][lowerSize]
    cv2.circle(frame,(lowerSize, topSize), 10, (0, 255, 0), -5)
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    '''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #newgray = np.array(gray, dtype='uint8')
    '''

'''
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.circle(frame,(x + (w / 2), y + ( 4 * (h / 5))), 10, (0, 255, 0), -5)
        #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
           # cv2.line(roi_color,(ex + (ew/2), ey),(ex +(ew / 2), ey + eh),(0, 0, 255))
           # cv2.line(roi_color,(ex, ey + (eh / 2)), (ex + ew, ey + (eh / 2)), (0, 0, 255))
           # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

'''

cv2.destroyAllWindows()
