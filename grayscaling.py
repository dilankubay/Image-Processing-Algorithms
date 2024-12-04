import cv2

# Gri tonlamaya dönüştürülecek resmin dosya yolunu belirt
resim_yolu = "Images/Lenna.png"

# Resmi aç (renkli olarak)
image = cv2.imread(resim_yolu, cv2.IMREAD_COLOR)

# Resmi ekranda göster
cv2.imshow("Orijinal Goruntu", image)

# Resmi gri tonlamalı hale getirme
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Her pikseli döngü ile gez
height, width = gray_image.shape
for y in range(height):
    for x in range(width):
        # Her pikselin gri değerini al
        gri_deger = gray_image[y, x]
        # Orijinal resmin pikselini gri tonlamaya dönüştür
        image[y, x] = (gri_deger, gri_deger, gri_deger)

# Gri tonlama işlemi tamamlandıktan sonra resmi ekranda göster
cv2.imshow("Gri Tonlama Goruntu", image)

# Gri tonlamalı resmi Images klasörüne kaydet
cv2.imwrite("Images/griton.png", image)

# Çıkış için bir tuşa basmayı bekleme
cv2.waitKey(0)
cv2.destroyAllWindows()