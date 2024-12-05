import cv2
import numpy as np

def contrast_stretching(image):

    #Görüntüdeki maks ve min değerleri bulur
    min_val = np.min(image)
    max_val = np.max(image)

    # Kontrast germe formülü uygulanması
    stretched = (image - min_val) * (255.0 / (max_val - min_val))
    return np.clip(stretched, 0, 255).astype(np.uint8)

# Read the image
input_image_path = "Images/Lenna.png"
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale for simplicity

# Kontrast germe uygulanması
stretched_image = contrast_stretching(image)

# Save and display the results
cv2.imwrite("Images/contrast.png", stretched_image)
cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Kontrasti Gerilmis Goruntu", stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
