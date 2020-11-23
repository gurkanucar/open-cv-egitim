# pip install numpy==1.19.3
# pip install opencv-python
import cv2
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')
xler = []
yler = []

while (1):
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (600, 600))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        xler.append(x + w // 2)
        yler.append(y + h // 2)
    for i in range(0, len(xler)):
        cv2.circle(frame, (xler[i], yler[i]), 5, (0, 0, 255), -1)
    cv2.imshow("Yuz Takip", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
