# load a video #

from cv2 import cv2

video = cv2.VideoCapture('video.mp4')

while video.isOpened():
    _,frame = video.read()
    cv2.imshow('video',frame)

    k=cv2.waitKey(20)
    if k & 0xFF == ord('q'):
        break

video.release()