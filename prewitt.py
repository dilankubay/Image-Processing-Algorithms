import cv2
import numpy as np

# Görüntüyü oku
input_image_path = "Images/Lenna.png"
image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

# Prewitt Yatay Çekirdeği (x yönü)
prewitt_x_kernel = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])

# Görüntü boyutları
height, width, _ = image.shape

# Prewitt filtresinin uygulanacağı boş çıktı görüntüsü oluştur
output_image = np.zeros_like(image, dtype=np.float32)

# Konvolüsyon işlemi
for y in range(1, height - 1):
    for x in range(1, width - 1):
        # R, G, B kanallarına ayrı ayrı filtre uygula
        r_pixel = 0
        g_pixel = 0
        b_pixel = 0
        for ky in range(3):  # 3x3 çekirdek boyutunda
            for kx in range(3):
                r_pixel += image[y + ky - 1, x + kx - 1, 0] * prewitt_x_kernel[ky, kx]
                g_pixel += image[y + ky - 1, x + kx - 1, 1] * prewitt_x_kernel[ky, kx]
                b_pixel += image[y + ky - 1, x + kx - 1, 2] * prewitt_x_kernel[ky, kx]

        # Yeni piksel değerlerini atanacak
        output_image[y, x, 0] = r_pixel
        output_image[y, x, 1] = g_pixel
        output_image[y, x, 2] = b_pixel

# Normalize et (0-255 arası)
output_image = np.clip(output_image, 0, 255).astype(np.uint8)

# Sonuçları görüntüle
cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Prewitt Filtresi Uygulanmis Goruntu", output_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
