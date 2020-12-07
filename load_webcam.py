# load camera #

from cv2 import cv2

video = cv2.VideoCapture(0)

while video.isOpened():
    _,frame = video.read()
    cv2.imshow('video',frame)
    
    k=cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break 

video.release()