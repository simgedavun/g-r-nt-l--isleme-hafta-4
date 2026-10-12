import cv2
import time

# 1. Resmi gri tonlamalı okuyoruz
resim = cv2.imread('resim.jpg', 0)

# 2. Çalışma süresini ölçmek için zamanlayıcıyı başlatıyoruz
baslangic = time.time()

# 3. OpenCV Canny fonksiyonunu çağırıyoruz
# minVal=100, maxVal=200 standart ve en iyi sonuç veren eşik değerleridir
kenarlar_canny = cv2.Canny(resim, threshold1=100, threshold2=200)

bitis = time.time()
gecen_sure = (bitis - baslangic) * 1000  # Milisaniye cinsinden

print(f"Canny algoritmasi calisma suresi: {gecen_sure:.4f} ms")

# 4. Sonuçları ekranda gösterip tuş bekliyoruz
cv2.imshow('Orijinal Resim', resim)
cv2.imshow('Gorev 7 - Canny Kenar Tespiti', kenarlar_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()