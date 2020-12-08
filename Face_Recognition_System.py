# Face Recognition System incorporating OpenCV and tkinter #

import tkinter
import os
import numpy as np
from cv2 import cv2
from PIL import Image

window = tkinter.Tk()
window.title("Face recognition system")
window.geometry("900x500")
window.configure(bg="gold")

face_detector=cv2.CascadeClassifier(r"C:\Users\Student\Desktop\SGTS006_SGTS039\GUI\haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def data_collection():
    
    face_id = input("Please enter the name of the face ID: ")
    sample_number = 0
    assure_path_exists("data_set/")
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
            cv2.imwrite(r"C:\Users\Student\Desktop\SGTS006_SGTS039\GUI\data_set\user_" + face_id + "_face" + str(sample_number) + ".jpg", grey_video[y:y+h, x:x+w])
        elif  sample_number>49:
            print("Saving completed.  Press q to exit program.")
            sample_number = 0
        
        if k & 0xFF== ord('q'):
            print("Turning off camera...")
            print("Camera off.")
            break
    
    # Stop the camera
    camera.release()
    cv2.destroyWindow("video")


def training():
    # Get the faces and IDs
    faces,ids = getImagesAndLabels(r'C:\\Users\Student\Desktop\SGTS006_SGTS039\GUI\data_set')

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    assure_path_exists('data_trainer3/')
    recognizer.save('data_trainer3/trainer.yml')

def face_recognition():
    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    assure_path_exists("data_trainer3/")

    # Load the trained mode
    recognizer.read('data_trainer3/trainer.yml')

    # Load prebuilt model for Frontal Face
    cascadePath = "haarcascade_frontalface_default.xml"

    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath)

    # Set the font style
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Initialize and start the video frame capture
    camera = cv2.VideoCapture(0)

    # Loop
    while True:
        # Read the video frame
        ret, im =camera.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

            # Recognize the face belongs to which ID
            Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check the ID if exist 
            #if(confidence<50):
            if(Id == 1):
                Id = "Handsome {0:.2f}%".format(round(100 - confidence, 2))

            elif(Id == 2):
                Id = "YanDao {0:.2f}%".format(round(100 - confidence, 2))

            else:
                Id = "Unknown"

            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)


        # Display the video frame with the bounded rectangle
        cv2.imshow('im',im) 

        # If 'q' is pressed, close program
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Stop the camera
    camera.release()
    cv2.destroyWindow("im")

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,files) for files in os.listdir(path)] 
    faceSamples=[]
    ids = []

    # Loop all the file path
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img,'uint8')

        # Get the image id
        id = int(os.path.split(imagePath)[-1].split("_")[1])

        # Get the face from the training images
        faces = face_detector.detectMultiScale(img_numpy)

        # Loop for each face, append to their respective ID
        for (x,y,w,h) in faces:

            # Add the image to face samples
            faceSamples.append(img_numpy[y:y+h,x:x+w])

            # Add the ID to IDs
            ids.append(id)

    # Pass the face array and IDs array
    return faceSamples,ids

def close_window():
    window.destroy()

label_1=tkinter.Label(window,text="Notice: This System is for Authorized Personnel Only",bg="gold",fg="blue",font=('Helvetica',20,'bold'))
label_1.pack(anchor = "center")

button1=tkinter.Button(window,text="Data Collection",bg="green",fg="yellow",width=22,height=3,font=('Helvetica',12, 'bold'),command=data_collection)
button1.place(x=90,y=100)

button2=tkinter.Button(window,text="Training",bg="green",fg="yellow",width=22,height=3,font=('Helvetica',12, 'bold'),command=training)
button2.place(x=340,y=100)

button3=tkinter.Button(window,text="Face Recognizer",bg="green",fg="yellow",width=22,height=3,font=('Helvetica',12, 'bold'),command=face_recognition)
button3.place(x=590,y=100)

window.mainloop()

# Stop the camera
camera.release()

# Close all windows
cv2.destroyAllWindows()