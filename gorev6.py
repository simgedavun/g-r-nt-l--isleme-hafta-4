import cv2
import numpy as np

# 1. Resmi gri tonlamalı okuyoruz
resim = cv2.imread('resim.jpg', 0)

# 2. 7x7 boyutunda LoG (Laplacian of Gaussian) Çekirdeği
# Bu matris Gauss yumuşatması ile Laplacian türevini tek seferde yapar
log_cekirdek = np.array([
    [ 0,  0,  1,   2,  1,  0,  0],
    [ 0,  1,  3,   5,  3,  1,  0],
    [ 1,  3,  0,  -7,  0,  3,  1],
    [ 2,  5, -7, -24, -7,  5,  2],
    [ 1,  3,  0,  -7,  0,  3,  1],
    [ 0,  1,  3,   5,  3,  1,  0],
    [ 0,  0,  1,   2,  1,  0,  0]
], dtype=np.float32)

# 3. Çekirdeği resmin üzerinde gezdiriyoruz (Konvolüsyon)
kenarlar = cv2.filter2D(resim, cv2.CV_64F, log_cekirdek)

# 4. Eksi değerlerin mutlak değerini alıp 0-255 piksel aralığına çeviriyoruz
sonuc = np.abs(kenarlar)
sonuc = np.uint8(sonuc)

# 5. Sonuçları ekranda gösterip tuş bekliyoruz
cv2.imshow('Orijinal Resim', resim)
cv2.imshow('Gorev 6 - 7x7 LoG Kenarlar', sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()