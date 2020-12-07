# load camera with function to save a face image #

from cv2 import cv2

video = cv2.VideoCapture(0)

while video.isOpened():
    _,frame = video.read()
    cv2.imshow('video',frame)
    
    k=cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break 

    if k & 0xFF == ord('s'):
        check, frame = video.read()
        cv2.imwrite(filename='Saved_image.jpg', img=frame)
        print('Saving image')
        cv2.waitKey(1500)
        print('Image saved.')  

video.release()