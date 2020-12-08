# STEP 1 #
# Face(s) collection / Gather data for training & modelling #
# user can save up to 50 face images via live camera by pressing the <S> key #

from cv2 import cv2

face_detector=cv2.CascadeClassifier(r"C:\Users\Student\Desktop\SGTS006_SGTS039\Face_Recognition\haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

face_id = input("Please enter the name of the face ID: ")
sample_number = 0

while camera.isOpened():
    _, video = camera.read() 
    grey_video = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    faces=face_detector.detectMultiScale(grey_video, scaleFactor=1.05, minNeighbors=5,minSize=(100,100))

    for (x,y,w,h) in faces:
        cv2.rectangle(video,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow('video',video)
    k=cv2.waitKey(1)

    if k & 0xFF == ord('s'):
        sample_number = sample_number + 1
        print("Saving face " + str(sample_number) + "...")
        cv2.imwrite(r"C:\Users\Student\Desktop\SGTS006_SGTS039\Face_Recognition\data_set\user_" + face_id + "_face" + str(sample_number) + ".jpg", grey_video[y:y+h, x:x+w])
    elif  sample_number>49:
          print("Saving completed.  Press q to exit program.")
          sample_number = 0
    
    if k & 0xFF== ord('q'):
        print("Turning off camera...")
        print("Camera off.")
        break


camera.release()
cv2.destroyAllWindows
