# load camera with functions to save photo image and record video #

from cv2 import cv2

video = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
record_video = cv2.VideoWriter('Recorded_video.avi',fourcc,30,(640,480))

while video.isOpened():
    _,frame = video.read()
    cv2.imshow('video',frame)
    
    k=cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break

    if k & 0xFF == ord('s'):
        check,frame = video.read()
        cv2.imwrite(filename='saved_img.jpg',img=frame)
        print("Saving image...")
        cv2.waitKey(1650)
        print("Image saved.")

    if k & 0xFF == ord('r'):
        
        print("Recording video in progress, press ESC to end recording")
        
        while(True):
            _,frame = video.read()
            cv2.imshow('video',frame)
            record_video.write(frame)
            k=cv2.waitKey(1)

            if k & 0xFF == 27:
                print("Recording end.")
                print("Camera is still in use, press q to quit program.")
                break
    

video.release()