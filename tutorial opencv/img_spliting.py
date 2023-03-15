import numpy as np
import cv2
img = cv2.imread('C:\data science\classes\multimedia\photo-1608848461950-0fe51dfc41cbcat.jpeg')
b,g,r = cv2.split(img)
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows() 
