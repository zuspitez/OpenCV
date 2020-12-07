# load video with resize and rotation #

from cv2 import cv2

video = cv2.VideoCapture('video.mp4')

while video.isOpened():
    _,frame = video.read()
    resize_frame=cv2.resize(frame,(640,480))
    rotate=cv2.rotate(resize_frame,cv2.ROTATE_90_CLOCKWISE)
    
    cv2.imshow('video',rotate)

    k=cv2.waitKey(20)
    if k & 0xFF == ord('q'):
        break

video.release()