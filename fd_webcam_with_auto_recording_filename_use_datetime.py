from cv2 import cv2
import time
from datetime import datetime

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
video = cv2.VideoCapture(0)

while video.isOpened():
    _, frame = video.read() 
    grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey_frame, scaleFactor=1.05, minNeighbors=5,minSize=(100,100))
    cv2.putText(frame,"Live Camera is on.", (50,50), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    print("You are in main loop")

    if len(faces) == 0:
        cv2.putText(frame,"No face is detected.",(50,450),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

    else:
        cv2.putText(frame,"Number of faces detected: " + str(faces.shape[0]),(50,450),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(frame,"Face detected" ,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 255, 0),2)

    cv2.imshow('Live Camera Window',frame)
    k=cv2.waitKey(1)

    if k & 0xFF == ord('s'):
        ret,frame = video.read()
        cv2.imwrite('saved_img.jpg',frame)
        print("Saving image...")
        cv2.waitKey(1650)
        print("Image saved.")

    if len(faces) > 1:
    
        print("Recording video in progress")
        record_duration = 11
        start_time = int(time.time())
        filename_string = "Recorded_video_"+(datetime.now().strftime("%Y%m%d_%H%M_%S"))+".avi"
        record_video = cv2.VideoWriter(filename_string,fourcc,30,(640,480))

        while( int(time.time()- start_time)  < int(record_duration)):
            _,frame = video.read()
            cv2.putText(frame,"Recording mode.", (50,50), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2) 
            cv2.imshow('Live Camera Window',frame)
            record_video.write(frame)
            k=cv2.waitKey(1)
            timestamp = round((time.time()- start_time),2)
            print("You are in recording loop. Recorded %s seconds" %timestamp )
               
            if k & 0xFF == 27:
                print("Recording end.")
                print("Camera is still in use, press q to quit program.")
                break
    
    elif k & 0xFF== ord('q'):
        print("Turning off camera...")
        print("Camera off.")
        break

video.release()
cv2.destroyAllWindows