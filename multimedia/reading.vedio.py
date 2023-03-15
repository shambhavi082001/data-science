import cv2

video = cv2.VideoCapture('vedio.mp4')

while True:
    state,img = video.read()
    print (state)
    if state:
        cv2.imshow("video output",img)
        if cv2.waitKey(1) == 27:
            break

    else:
        break
video.release()
cv2.destroyAllWindows()