import cv2

im = cv2.imread('sample.png')
print(im.shape)
cv2.imshow('Image window', im)
cv2.waitKey(0)