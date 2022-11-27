import cv2
img = cv2.imread('C:\data science\classes\multimedia\cat image processing using opencv\photo-1608848461950-0fe51dfc41cbcat.jpeg')
# syntax : cv2.getRotationMatrix2D(center, angle, scale rotated = cv2.warpAfifne(img,M,(w,h))  
h,w = img.shape[:2] ## get image height, width
center = (w/2,h/2) # calculate the center of the image
angle90 = 90
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w)) 
 
  
cv2.imshow('Image rotated by 90 degrees', rotated90)  
cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image

