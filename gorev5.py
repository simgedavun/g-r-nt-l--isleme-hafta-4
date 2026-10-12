import cv2
import numpy as np

# 1. Resmi gri tonlamalı okuyoruz
resim = cv2.imread('resim.jpg', 0)

# 2. Laplacian 2. derece türev olduğu için gürültüden çok etkilenir
# Bu yüzden hocanın dediği gibi önce Gauss ile hafifçe yumuşatıyoruz
yumusatilmis = cv2.GaussianBlur(resim, (3, 3), 0)

# 3. 3x3 Laplacian Çekirdeği
# Sobel ve Prewitt gibi yatay/dikey ayrı değil, tek matrisle tüm kenarları bulur
laplacian_matrisi = np.array([
    [0,  1,  0],
    [1, -4,  1],
    [0,  1,  0]
], dtype=np.float32)

# 4. Filtreyi resme uyguluyoruz (Konvolüsyon)
# Eksi değerler kırpılmasın diye float formatında tutuyoruz
kenarlar = cv2.filter2D(yumusatilmis, cv2.CV_64F, laplacian_matrisi)

# 5. Eksi çıkan kenar değerlerini artıya çevirip 8-bit piksele dönüştürüyoruz
sonuc = np.abs(kenarlar)
sonuc = np.uint8(sonuc)

# 6. Ekranda gösterip tuş bekliyoruz
cv2.imshow('Orijinal Resim', resim)
cv2.imshow('Gorev 5 - Laplacian Kenarlar', sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()