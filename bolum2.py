"""
Resim özellikleri
•	Resim boyutu öğrenme
•	Resmi boyutlandırma
•	Resmi aynalama
•	Resmi çevirme
•	Resmi gri yapma
•	Resmi blurlama
•	Resimdeki bir alanı seçip alma
•	Resmi kırpma
•	Resimdeki pixelin rengini öğrenme
•	Resimdeki pixelin rengini değiştirme
•	Resimdeki bir alanı seçip tekrar başka bir yere yapıştırma
•   2 resmi birlestirme
"""
import cv2
import numpy as np

# Resim okuma ve gosterme
img = cv2.imread("res/face.png")
# cv2.imshow("Resim",img)

# resim boyutu gorme
print(img.shape)

# resim boyutu degistirme
buyuk = cv2.resize(img, (700, 700))
kucuk = cv2.resize(img, (200, 200))

# cv2.imshow("buyuk",buyuk)
# cv2.imshow("kucuk",kucuk)

# resim dondurme
# cv2.ROTATE_180     cv2.ROTATE_90_COUNTERCLOCKWISE
dondur = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow("donmus",dondur)

# resim aynalama
aynala1 = cv2.flip(img, -1)
aynala2 = cv2.flip(img, 0)
aynala3 = cv2.flip(img, 1)

# cv2.imshow("aynala1",aynala1)
# cv2.imshow("aynala2",aynala2)
# cv2.imshow("aynala3",aynala3)


# Resim filtreleri
siyahBeyaz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurlu = cv2.blur(img, (20, 20))
kenarAlgilama = cv2.Canny(img, 100, 200)

# cv2.imshow("siyahBeyaz",siyahBeyaz)
# cv2.imshow("blurlu",blurlu)
# cv2.imshow("kenarAlgilama",kenarAlgilama)

# resimden alan seçme / kırpma
# [y:y+h, x:x+w]
imgSecilmis = img[100:220, 100:260]
# cv2.imshow("imgSecilmis",imgSecilmis)

# resimdeki pixelin rengini bulma
b = img.item(10, 10, 0)
g = img.item(10, 10, 1)
r = img.item(10, 10, 2)
print(r, b, g)

# resimdeki pixelin rengini değiştirme
pixelDegis = img
pixelDegis.itemset((10, 10, 0), 255)  # b
pixelDegis.itemset((10, 10, 1), 255)  # g
pixelDegis.itemset((10, 10, 2), 255)  # r

b = pixelDegis.item(10, 10, 0)
g = pixelDegis.item(10, 10, 1)
r = pixelDegis.item(10, 10, 2)
print(r, b, g)
# cv2.imshow("pixelDegis",pixelDegis)


# Resimdeki bir şeyi kopyalama
img2 = cv2.imread("res/manzara.jpg")
# cv2.imshow("manzara1",img2)
imgKopyala = img2[300:400, 80:200]
img2[300:400, 200:320] = imgKopyala
img2[300:400, 380:500] = imgKopyala

# cv2.imshow("manzara2",imgKopyala)
# cv2.imshow("manzara3",img2)

# 2 resmi birlestirme
koyun = cv2.imread("res/koyun.jpg")
bekci = cv2.imread("res/bekci.jpg")

yatay = np.hstack((koyun, bekci))
dikey = np.vstack((koyun, bekci))

# cv2.imshow("yatay",yatay)
# cv2.imshow("dikey",dikey)


# Renk filtreleme
kirmizi = cv2.imread("res/kirmizi.jpeg")
hsv = cv2.cvtColor(kirmizi, cv2.COLOR_BGR2HSV)
alt = np.array([150, 30, 30])
ust = np.array([190, 255, 255])
maske = cv2.inRange(hsv, alt, ust)
maskeli = cv2.bitwise_and(kirmizi, kirmizi, mask=maske)

karsilastir = np.hstack((kirmizi, maskeli))
# cv2.imshow("maske",karsilastir)


cv2.waitKey(0)
