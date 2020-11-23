"""

Resme metin ekleme ve metin özellikleri
Resme çizgi ekleme
Resme dörtgen ekleme
Resme daire ekleme

"""
import cv2

img = cv2.imread("res/kopek.jpg")
cv2.imshow("Resim",img)

cv2.putText(img, "IEEE CS", (30, 30), cv2.cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 0, 0), 2)

cv2.putText(img, "PYTHON", (30, 90), cv2.cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 255, 255), 2)

cv2.putText(img, "OPENCV", (30, 250), cv2.cv2.FONT_HERSHEY_SIMPLEX, 2,
            (0, 0, 255), 2)

cv2.line(img, (0, 0), (620, 350), (255, 255, 255), 2)
cv2.line(img, (620, 0), (0, 350), (0, 255, 0), 10)

cv2.rectangle(img, (220, 20), (380, 160), (0, 255, 255), 3)
# cv2.rectangle(img, (220,20), (380,160), (0, 255, 255), -1) # içi dolu

cv2.circle(img, (300, 100), 100, (0, 0, 255), 2)

cv2.imshow("Resim", img)
cv2.waitKey(0)
