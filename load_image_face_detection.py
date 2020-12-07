# load image and draw rectangle on faces #

from cv2 import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread ('group_photo.jpg')
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5,minSize=(100,100))

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

resized_img = cv2.resize(img,(700,467))
cv2.imshow('image',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()