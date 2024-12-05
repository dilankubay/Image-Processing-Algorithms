import cv2
import numpy as np
import random

def add_salt_and_pepper_noise(image, amount):
    """Görüntüye tuz biber görüntüsü ekliyor"""
    noisy_image = image.copy()
    h, w = noisy_image.shape
    num_noise_pixels = int((h * w) / amount)

    for _ in range(num_noise_pixels):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        # Salt (white pixel)
        if random.random() < 0.5:
            noisy_image[y, x] = 255
        else:  # Pepper (black pixel)
            noisy_image[y, x] = 0

    return noisy_image

def apply_median_filter(image, kernel_size):
    """Apply a median filter to an image."""
    h, w = image.shape
    padded_image = cv2.copyMakeBorder(image, kernel_size // 2, kernel_size // 2, kernel_size // 2, kernel_size // 2, cv2.BORDER_REFLECT)
    filtered_image = np.zeros_like(image)

    # Apply the median filter
    for y in range(h):
        for x in range(w):
            # Extract the neighborhood
            region = padded_image[y:y + kernel_size, x:x + kernel_size]
            # Compute the median and assign it to the output pixel
            filtered_image[y, x] = np.median(region)

    return filtered_image

# Read image using OpenCV
input_image_path = "Images/Lenna.png"
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale

# Add salt and pepper noise
noisy_image = add_salt_and_pepper_noise(image, amount=25)

# Apply median filter
kernel_size = 3
filtered_image = apply_median_filter(noisy_image, kernel_size)

# Save and display results
cv2.imwrite("Images/photo_noisy.png", noisy_image)
cv2.imwrite("Images/photo_median_filtered.png", filtered_image)

cv2.imshow("Original Goruntu", image)
cv2.imshow("Tuz Biberli Goruntu", noisy_image)
cv2.imshow("Median Filtresi Uygulanmis Goruntu", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
