import numpy as np
import cv2
import os

filename = "video.avi"
frames_per_second = 24.0
my_res = "720p"

cap=cv2.VideoCapture(0)

def change_res(cap,width,height):
	cap.set(3,width)
	cap.set(4,height)

STD_Dimension={
	"480p":(640,480),
	"720p":(1280,720),
	"1080p":(1920,720),
	"4k":(3840,2160)
}

def get_dimension(cap,res="1080p"):
	width,height = STD_Dimension["480p"]
	if res in STD_Dimension:
		width,height = STD_Dimension[res]
	change_res(cap,width,height)
	return width,height

Video_type={
	"avi":cv2.VideoWriter_fourcc(*"XVID"),
	"mp4":cv2.VideoWriter_fourcc(*"XVID")
}

def get_video_type(filename):
	filename,ext=os.path.splitext(filename)
	if ext in Video_type:
		return Video_type[ext]
	return Video_type["avi"]

video_type_cv2=get_video_type(filename)
dims=get_dimension(cap,res=my_res)

# out=cv2.VideoWriter(filename,video_type_cv2,my_res,frames_per_second,dims)

out=cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc(*"XVID"),25,dims)

while (True):
	ret,frame = cap.read()
	out.write(frame)
	cv2.imshow("frame",frame)
	if cv2.waitKey(20) & 0xFF== ord("q"):
		break

cap.release()
out.release()
cv2.destroyAllWindows()
