import numpy as np
import cv2
img = cv2.imread('C:\data science\classes\multimedia\photo-1608848461950-0fe51dfc41cbcat.jpeg')
# Change in Image color
# syntax : cv2.cvtColor(src, dst, code)
window_name = 'Image'
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
cv2.imshow(window_name, image) 
cv2.waitKey(0)

cv2.destroyAllWindows() 
