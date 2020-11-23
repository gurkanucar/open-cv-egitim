"""
Input / Output İşlemleri
•	Resim okuma ve yazma
•	Video gösterme
•	Kameradan görüntü alma
•	İp kameradan görüntü alma

"""
import cv2

print("Kutuphane yuklemesi basarili")

# Resim okuma
img = cv2.imread("res/face.png")
cv2.imshow("Resim", img)
cv2.waitKey(0)

# Resim yazma
img = cv2.imread("res/face.png")
cv2.imwrite("res/yuzResmi.png", img)
cv2.waitKey(0)

# Video okuma kaynaktan
video = cv2.VideoCapture("res/video.mp4")
while 1:
    ret, img = video.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video okuma kameradan
video = cv2.VideoCapture(0)
while 1:
    ret, img = video.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# IP kameradan okuma
url = "http://192.168.0.14:8080/video"
video = cv2.VideoCapture(url)
while 1:
    ret, img = video.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
