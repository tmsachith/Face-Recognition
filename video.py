import cv2

video = cv2.VideoCapture("video.mp4") # use any video file

while True:
    success,img=video.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break