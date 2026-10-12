# Prewitt ve Sobel Kenar Belirleme Operatörlerinin Karşılaştırmalı Analizi

## 1. Giriş ve Teorik Altyapı
Görüntü işlemede kenarlar, piksel yoğunluklarındaki ani ve belirgin değişimleri temsil eder. Bu değişimler matematiksel olarak birinci dereceden türev (gradyan) operatörleri ile hesaplanır. İki boyutlu uzayda bir görüntünün gradyanı şu şekilde tanımlanır:

$$\nabla f = \begin{bmatrix} G_x \\ G_y \end{bmatrix} = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$

Bu çalışmada, gürültü etkisini minimize etmek amacıyla gri tonlamalı görüntüye öncelikle **Gauss (Gaussian)** yumuşatma filtresi uygulanmış; ardından **Prewitt** ve **Sobel** operatörleri test edilmiştir.

---

## 2. Çekirdek (Kernel) Yapıları

### Prewitt Operatörü
Prewitt filtresi, komşu piksellere eşit ağırlık veren basit bir sonlu farklar yaklaşımı kullanır:

* **Dikey ($G_x$):**
  $$\begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}$$
* **Yatay ($G_y$):**
  $$\begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$

### Sobel Operatörü
Sobel filtresi ise merkeze daha yakın piksellere ağırlık vererek yumuşatma ve türev alma işlemlerini birleştirir:

* **Dikey ($G_x$):**
  $$\begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$
* **Yatay ($G_y$):**
  $$\begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

---

## 3. Karşılaştırmalı Değerlendirme

| Kriter | Prewitt Operatörü | Sobel Operatörü |
| :--- | :--- | :--- |
| **Katsayı Dağılımı** | Homojen / Eşit katsayılar ([-1, 0, 1]) | Merkez ağırlıklı katsayılar ([-1, -2, -1] / [1, 2, 1]) |
| **Gürültüye Direnç** | Orta düzey; eşit ağırlıklandırma nedeniyle gürültüye daha hassastır | Yüksek; merkezdeki 2 katsayısı yerel yumuşatma sağlar |
| **Kenar Belirginliği** | Kenarlar daha ince ancak kontrast geçişlerinde daha zayıf kalabilir | Kenarlar daha net, parlak ve süreklidir |
| **Hesaplama Yükü** | Çarpma işlemlerinde sadece 1 katsayısı kullanıldığı için daha hafiftir | 2 ile çarpım içerir, donanımda bit kaydırma ile optimize edilebilir |

---

## 4. Ön İşleme (Gauss Filtresi) Etkisi
Türev temelli operatörler yüksek frekanslı bileşenlere (dolayısıyla gürültüye) aşırı tepki verir. Uygulanan $3 \times 3$ Gauss çekirdeği:
1. Görüntüdeki yüksek frekanslı gren ve sensör gürültülerini bastırmıştır.
2. Sahte (yanıltıcı) kenar tespitlerini engelleyerek her iki filtrenin de ana kenar hatlarına odaklanmasını sağlamıştır.

---

## 5. Sonuç
Test edilen görüntüler üzerinde Sobel operatörü, merkez piksellere verdiği ekstra ağırlık sayesinde Prewitt operatörüne kıyasla daha kesintisiz, belirgin ve gürültüden arındırılmış kenar çizgileri üretmiştir. Prewitt operatörü ise hesaplama karmaşıklığının kısıtlı olduğu gömülü sistemler için iyi bir alternatif sunarken, genel kenar kalitesi ve süreklilik açısından Sobel operatörü daha başarılı bir performans sergilemektedir.
## Laplacian Operatörünün Prewitt ve Sobel ile Kıyaslanması

### 1. Türev Mertebesi ve Yön Bağımsızlığı (İzotropi)
* **Prewitt ve Sobel:** 1. dereceden türev operatörleridir. Yatay ($G_y$) ve dikey ($G_x$) kenarları ayrı ayrı hesaplarlar. Kenarın yönü (gradient angle) tespit edilebilir.
* **Laplacian:** 2. dereceden türev operatörüdür ($\nabla^2 f$). İzotropiktir; kenarın hangi yönde (yatay, dikey, çapraz) olduğuna bakılmaksızın tüm yönlerdeki kenarları tek bir filtre matrisiyle aynı anda bulur. Kenar doğrultusu bilgisi vermez.

### 2. Gürültü Hassasiyeti
* 1. derece türev filtreleri (Prewitt/Sobel) gürültüye orta/düşük hassasiyet gösterirken, 2. derece türev alan Laplacian filtresi piksel farklarının karesel türevini aldığı için gürültüye **aşırı derecede hassastır**. Bu nedenle Laplacian uygulanmadan önce mutlaka Gauss gibi bir yumuşatma filtresi uygulanmalıdır.

### 3. Çıktı Özellikleri
* Sobel ve Prewitt filtreleri kenar bölgelerinde parlak ve kalın geçiş bantları üretirken; Laplacian filtresi kenar geçişlerinde sıfır geçişi (zero-crossing) mantığıyla çalıştığından daha ince kenar çizgileri ve belirgin çift hat etkisi oluşturur.
Doğruluk ve Kenar Kalitesi:
Prewitt ve Sobel: Kenarları kalın bantlar halinde tespit eder; gürültüye karşı hassastır.
Laplacian ve LoG: Yönsüz kenarları bulur fakat kenar etrafında çift hat (halo) etkisi ve gürültü hassasiyeti oluşturur.
Canny: Uyguladığı Non-Maximum Suppression (NMS) adımı sayesinde kenarları tam 1 piksele indirger. Histerezis eşikleme ile zayıf gürültüleri tamamen temizleyip gerçek kenarları kesintisiz bağlar. Doğruluk açısından en üstün algoritmadır.
Çalışma Zamanı:
Tek adımlı çekirdekler (Prewitt/Sobel/Laplacian) yalnızca tek bir 2D konvolüsyon çalıştırdığı için teorik olarak çok hızlıdır (~1-2 ms).
Canny; Gauss yumuşatma, gradyan hesabı, NMS ve eşikleme gibi çok aşamalı bir boru hattı (pipeline) çalıştırmasına rağmen C++ ile optimize edilmiş OpenCV motorunda son derece yüksek bir hızda (~3.6 ms) çalışarak gerçek zamanlı sistemler için ideal dengeyi sağlar.