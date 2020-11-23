# pip install numpy==1.19.3
# pip install opencv-python
import cv2
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')
while (1):
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)

        face = cv2.blur(frame[y: y + h, x: x + w], (50, 50))
        frame[y:y + h, x:x + w] = face

    cv2.imshow("Yuz Takip", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
