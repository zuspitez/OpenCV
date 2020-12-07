# load camera and detect face(s) and indicate no. of face(s) detected with label #

from cv2 import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, video = cap.read() 
    grey_video = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey_video, scaleFactor=1.05, minNeighbors=5,minSize=(100,100))
    cv2.putText(video,"Live Camera is on.", (50,50), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    if len(faces) == 0:
        cv2.putText(video,"No face is detected.",(50,450),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

    else:
        cv2.putText(video,"Number of faces detected: " + str(faces.shape[0]),(50,450),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

        for (x,y,w,h) in faces:
            cv2.rectangle(video,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(video,"Face detected" ,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 255, 0),2)

    cv2.imshow('video',video)
    k=cv2.waitKey(1)

    if k & 0xFF == ord('s'):
        check,video = cap.read()
        cv2.imwrite(filename='saved_img.jpg',img=video)
        print("Saving image...")
        cv2.waitKey(1650)
        print("Image saved.")
   
    elif k & 0xFF == ord('a'):
        print('Button a is clicked.')

    elif k & 0xFF== ord('q'):
        print("Turning off camera...")
        print("Camera off.")
        break
cap.release()
cv2.destroyAllWindows