import cv2
import numpy as np

# Görüntüyü okuma (gri tonlamalı olarak)
input_image_path = "Images/Lenna.png"
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Görüntü boyutlarını al
height, width = image.shape

# Eşik değeri belirleme
esikDeger = 100

# Yeni bir çıktı görüntüsü oluştur
output_image = np.zeros((height, width), dtype=np.uint8)

# Eşikleme işlemi
for y in range(height):
    for x in range(width):
        if image[y, x] > esikDeger:
            output_image[y, x] = 255  # Beyaz
        else:
            output_image[y, x] = 0    # Siyah

# Orijinal ve işlenmiş görüntüyü gösterme
cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Islenmis Goruntu", output_image)

# Çıkış için bir tuşa basmayı bekleme
cv2.waitKey(0)
cv2.destroyAllWindows()
