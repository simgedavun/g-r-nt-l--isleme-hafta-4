import cv2
import numpy as np

# 1. Resmi gri tonlamalı oku
resim = cv2.imread('resim.jpg', 0)

# 2. Öncesinde Gauss ile hafif yumuşatma yap
yumusatilmis = cv2.GaussianBlur(resim, (3, 3), 0)

# 3. 3x3 Dikey ve Yatay Sobel Çekirdekleri
sobel_dikey = np.array([
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1]
], dtype=np.float32)

sobel_yatay = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

# 4. Filtreleri konvolüsyonla gezdir
kenar_dikey = cv2.filter2D(yumusatilmis, cv2.CV_64F, sobel_dikey)
kenar_yatay = cv2.filter2D(yumusatilmis, cv2.CV_64F, sobel_yatay)

# 5. Negatifleri mutlak değere çevirip 8-bit yap
sonuc_dikey = np.uint8(np.abs(kenar_dikey))
sonuc_yatay = np.uint8(np.abs(kenar_yatay))

# Hem dikey hem yatay kenarların birleşimi (Toplam Kenar)
toplam_kenar = cv2.addWeighted(sonuc_dikey, 0.5, sonuc_yatay, 0.5, 0)

# 6. Sonuçları ekranda göster
cv2.imshow('Sobel Dikey Kenarlar', sonuc_dikey)
cv2.imshow('Sobel Yatay Kenarlar', sonuc_yatay)
cv2.imshow('Sobel Toplam Kenarlar', toplam_kenar)

cv2.waitKey(0)
cv2.destroyAllWindows()