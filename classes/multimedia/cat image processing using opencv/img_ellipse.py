import numpy as np  
import cv2  
#cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])   
 
img = cv2.imread('C:\data science\classes\multimedia\cat image processing using opencv\photo-1608848461950-0fe51dfc41cbcat.jpeg')
cv2.ellipse(img, (250, 150), (80, 20), 5, 0, 360, (0,0,255), -1) 
  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  

"""
- Drawing lines:
syntax : cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) 
import numpy as np  
import cv2  
cv2.line(img,(10,0),(150,150),(0,0,0),15)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  


- write text on image
syntax: cv2.putText(img, text, org, font, color)
import numpy as np  
import cv2  
font = cv2.FONT_HERSHEY_SIMPLEX  
# Create a black image.  
cv2.putText(img,'Hack Projects',(10,500), font, 1,(255,255,255),2)  
#Display the image  
cv2.imshow("image",img)  
cv2.waitKey(0)  


-Drawing Polylines
syntax:cv2.polyLine(img, polys, is_closed, color, thickness=1, lineType=8, shift=0)
import numpy as np  
import cv2    
#defining points for polylines  
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)  
# pts = pts.reshape((-1,1,2))  
cv2.polylines(img, [pts], True, (0,255,255), 3)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
"""