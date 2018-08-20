import numpy as np
import cv2

cap=cv2.VideoCapture(0)

def make_1080p():
	cap.set(3,1920)
	cap.set(4,1080)

def change_res(width,height):
	cap.set(3,height)
	cap.set(4,width)

# make_1080p()
# change_res(2000,2000)


def rescaling(frame,percent=75):
	width = (int(frame.shape[1]*percent/100))
	height = (int(frame.shape[0]*percent/100))
	dim=(width,height)
	return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

while (True):
	
	ret,frame = cap.read()
	frame=rescaling(frame,30)
	cv2.imshow("frame",frame)
	if cv2.waitKey(20) & 0xFF== ord("q"):
		break

cap.release()
cv2.destroyAllWindows()



