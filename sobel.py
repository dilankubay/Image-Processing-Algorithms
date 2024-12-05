import cv2
import numpy as np

# Görüntüyü oku
input_image_path = "Images/Lenna.png"
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Sobel X ve Y çekirdekleri
sobel_x_kernel = np.array([[1, 0, -1],
                           [2, 0, -2],
                           [1, 0, -1]])

sobel_y_kernel = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

# Görüntü boyutları
height, width = image.shape

# Filtre uygulamak için boş çıktı görüntüsü oluştur
sobel_x = np.zeros_like(image, dtype=np.float32)
sobel_y = np.zeros_like(image, dtype=np.float32)

# Konvolüsyon işlemi (Sobel X ve Y)
for y in range(1, height - 1):
    for x in range(1, width - 1):
        # Sobel X
        region_x = image[y-1:y+2, x-1:x+2]
        sobel_x[y, x] = np.sum(region_x * sobel_x_kernel)
        
        # Sobel Y
        region_y = image[y-1:y+2, x-1:x+2]
        sobel_y[y, x] = np.sum(region_y * sobel_y_kernel)

# Kenarları birleştir
sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)

# Görüntüyü normalize et ve uint8'e dönüştür
sobel_combined = np.clip(sobel_combined, 0, 255).astype(np.uint8)

# Sonuçları görüntüle
cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Sobel Yonunde Kenar Tespiti", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
