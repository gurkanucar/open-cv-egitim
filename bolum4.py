"""

Video İşlemleri:
•	Video boyutlandırma
•	Video döndürme
•	Video siyah beyaz yapma
•	Video bulanıklaştırma

"""
import cv2

video = cv2.VideoCapture(0)
while 1:
    ret, img = video.read()
    img = cv2.resize(img, (300, 300))

    dondur = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    aynala = cv2.flip(img, -1)
    siyahbeyaz = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    bulanik = cv2.blur(img,(20,20))
    kenarAlgilama = cv2.Canny(img, 50, 100)

    cv2.imshow("normal", img)
    cv2.imshow("dondur", dondur)
    cv2.imshow("aynala", aynala)
    cv2.imshow("siyahbeyaz", siyahbeyaz)
    cv2.imshow("bulanik", bulanik)
    cv2.imshow("kenarAlgilama", kenarAlgilama)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)