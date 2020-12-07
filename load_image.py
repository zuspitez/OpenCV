#load a photo in grayscale #

from cv2 import cv2

img=cv2.imread("group_photo.jpg",0)

cv2.imshow("group_photo",img)
cv2.waitKey()
cv2.destroyAllWindows()