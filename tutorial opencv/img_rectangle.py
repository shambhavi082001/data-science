import numpy as np  
import cv2  
# syntax: cv2.rectangle(img, pt1, pt2, color[, thickness[,lineType[,shift]]]) 
img = cv2.imread('C:\data science\classes\multimedia\cat image processing using opencv\photo-1608848461950-0fe51dfc41cbcat.jpeg')
cv2.rectangle(img,(15,25),(200,150),(0,255,255),15)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  