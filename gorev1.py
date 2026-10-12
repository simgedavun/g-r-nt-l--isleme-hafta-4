import cv2
import numpy as np

# ---------------------------------------------------------
# ADIM 1: Görüntüyü Gri Tonlamalı (Grayscale) Olarak Yükleme
# ---------------------------------------------------------
# cv2.IMREAD_GRAYSCALE, görüntünün renk (RGB) kanallarını tek bir parlaklık kanalına (0-255) indirger.
img = cv2.imread('resim.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Hata: 'resim.jpg' bulunamadı! Lütfen aynı klasörde olduğundan emin olun.")
else:
    # ---------------------------------------------------------
    # ADIM 2: Gauss Filtresi ile Hafif Yumuşatma (Gaussian Blur)
    # ---------------------------------------------------------
    # ksize=(3, 3): Çekirdek boyutu (3x3 piksellik pencere ile yumuşat).
    # sigmaX=0: Gauss fonksiyonunun standart sapması (0 verilirse boyuta göre otomatik hesaplanır).
    img_blurred = cv2.GaussianBlur(img, (3, 3), sigmaX=0)

    # ---------------------------------------------------------
    # ADIM 3: 3x3 Dikey Prewitt Çekirdeğini (Kernel) Tanımlama
    # ---------------------------------------------------------
    # Eğitmeninizin verdiği matris:
    # Sol sütun -1, orta sütun 0, sağ sütun +1
    prewitt_v = np.array([
        [-1,  0,  1],
        [-1,  0,  1],
        [-1,  0,  1]
    ], dtype=np.float32)

    # ---------------------------------------------------------
    # ADIM 4: Filtreyi Görüntü Üzerinde Gezdirme (Konvolüsyon)
    # ---------------------------------------------------------
    # Yumuşatılmış görüntü (img_blurred) üzerine filtre uygulanır.
    # ddepth=cv2.CV_64F: Çıkarma işleminden dolayı negatif değerler oluşabilir.
    # Standart 8-bit resimler negatif değer tutamadığından (0'a yuvarlar), 
    # hassas 64-bit float formatı kullanılır.
    edges_float = cv2.filter2D(src=img_blurred, ddepth=cv2.CV_64F, kernel=prewitt_v)

    # ---------------------------------------------------------
    # ADIM 5: Negatif Değerleri Düzenleme ve 8-bit'e Çevirme
    # ---------------------------------------------------------
    # Kenar, koyudan açığa veya açıktan koyuya geçiş olabilir (biri pozitif, biri negatif çıkar).
    # Her iki kenarı da görebilmek için mutlak değer alınır (|x|) ve 0-255 aralığına getirilir.
    prewitt_result = cv2.convertScaleAbs(edges_float)

    # ---------------------------------------------------------
    # ADIM 6: Sonuçları Ekranda Gösterme
    # ---------------------------------------------------------
    cv2.imshow('1. Orijinal Gri Goruntu', img)
    cv2.imshow('2. Gauss ile Yumusatilmis', img_blurred)
    cv2.imshow('3. Dikey Prewitt Kenarlar', prewitt_result)

    # Bir tuşa basılmasını bekle ve ardından pencereleri kapat
    cv2.waitKey(0)
    cv2.destroyAllWindows()