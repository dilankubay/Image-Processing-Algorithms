import cv2
import numpy as np

def histogram_equalization(image):
    # Histogramı hesaplama
    hist = [0] * 256
    height, width = image.shape
    for y in range(height):
        for x in range(width):
            hist[image[y, x]] += 1

    # Kümülatif dağılım fonksiyonu (CDF) hesaplama
    cdf = [0] * 256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    # CDF'yi normalize etme
    cdf_min = min(cdf)
    total_pixels = height * width
    cdf_normalized = [(val - cdf_min) / (total_pixels - cdf_min) * 255 for val in cdf]

    # Yeni piksel değerlerini atama
    equalized_image = np.zeros_like(image)
    for y in range(height):
        for x in range(width):
            equalized_image[y, x] = int(cdf_normalized[image[y, x]])

    return equalized_image

# Görüntüyü yükleme
input_image_path = "Images/Lenna.png"
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme
equalized_image = histogram_equalization(image)

# Görüntüleri kaydetme
cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Histogrami Esitlenmis Goruntu.png", equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()