import numpy as np
import cv2

cap=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:\Anaconda\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")

while(True):
	ret,frame = cap.read()   ## ret -- checks weather reading was successful returns (true/false). then it reads and return the frame.
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(frame,scaleFactor=1.5,minNeighbors=5)

	for (x,y,w,h) in faces:
		print(x,y,w,h)
		roi = frame[y:y+h,x:x+h]  # roi is known as area of interest.
		cv2.imwrite("face.jpg",roi)
		## Draw a rectangle, First thing is to declare what color it is.
		color = (255,0,0)  ## BGR  Blue,green,Red
		stroke = 2 ## How thick the line is.
		width = x+w
		height = y+h
		cv2.rectangle(frame,(x,y),(width,height),color,stroke)   ## rectangle(frame,start,end)

	cv2.imshow("frame",frame)
	if (cv2.waitKey(20) & 0xFF==ord("q")):
		break

# cv2.imwrite("test.jpg",frame)

cap.release()
cv2.destroyAllWindows()


