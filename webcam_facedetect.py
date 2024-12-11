import cv2

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    success,img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detect = face.detectMultiScale(imgGray, 1.3, 5)

    for(x,y,w,h) in detect:
        cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Face Detection",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break

cap.release()
