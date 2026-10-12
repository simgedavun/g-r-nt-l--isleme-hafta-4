import cv2
import numpy as np

# 1. Resmi gri tonlamalı (siyah-beyaz) olarak okuyoruz
resim = cv2.imread('resim.jpg', 0)  # 0 parametresi doğrudan gri tonlamalı okur

# 2. Hocanın istediği gibi filtre öncesi Gauss ile yumuşatma yapıyoruz
# 3x3 çekirdek gürültüyü hafifçe azaltmak için yeterli
yumusatilmis = cv2.GaussianBlur(resim, (3, 3), 0)

# 3. İkinci görevdeki 3x3 Yatay Prewitt Çekirdeği
# Üst satır negatif, alt satır pozitif -> Yatay kenarları bulur
cekirdek_yatay = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
], dtype=np.float32)

# 4. Çekirdeği resim üzerinde gezdiriyoruz (Konvolüsyon işlemi)
# Negatif piksel farklarını kaybetmemek için float64 kullanıyoruz
kenarlar = cv2.filter2D(yumusatilmis, cv2.CV_64F, cekirdek_yatay)

# 5. Negatif çıkan değerlerin mutlak değerini alıp 0-255 arasına çekiyoruz
sonuc = np.abs(kenarlar)
sonuc = np.uint8(sonuc)

# 6. Sonuçları ekranda gösterip bir tuşa basılmasını bekliyoruz
cv2.imshow('Orijinal Resim', resim)
cv2.imshow('Gorev 2 - Yatay Prewitt', sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()
