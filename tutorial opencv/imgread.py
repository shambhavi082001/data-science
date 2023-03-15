import cv2

img = cv2.imread('C:\data science\classes\multimedia\photo-1608848461950-0fe51dfc41cbcat.jpeg',1)

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows() 

status = cv2.imwrite('C:\data science\classes\multimedia\photo-1608848461950-0fe51dfc41cbcat.jpeg',img)

print("image written to file system:",status)

