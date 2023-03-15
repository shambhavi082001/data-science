import numpy as np
import cv2
#cv2.circle(img, center, radius, color[,thickness [, lineType[,shift]]])
img = cv2.imread('C:\data science\classes\multimedia\cat image processing using opencv\photo-1608848461950-0fe51dfc41cbcat.jpeg')
cv2.circle(img,(90,90), 55, (0,155,0), -1,)
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  