import cv2
import numpy as np

def mean_filter(image, kernel_size):
    #Mean filtresi uygulama
    image = np.array(image, dtype=np.float32)
    height, width, channels = image.shape
    pad = kernel_size // 2   
    # Pad the image
    padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image)
    # Mean filtresi kernel oluşturma
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size**2)
    # Meaan filtresi uygulama
    for y in range(height):
        for x in range(width):
            for c in range(channels):  # For each channel
                region = padded_image[y:y + kernel_size, x:x + kernel_size, c]
                filtered_image[y, x, c] = np.sum(region * kernel)

    # Clip values to valid range [0, 255] and convert to uint8
    filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
    return filtered_image

# Read the image using OpenCV
input_image_path = "Images/Lenna.png"
image = cv2.imread(input_image_path)

# Apply mean filter with kernel size 3x3
kernel_size = 3
filtered_image = mean_filter(image, kernel_size)

# Write the filtered image to disk and display
output_image_path = "Images/mean.png"
cv2.imwrite(output_image_path, filtered_image)

cv2.imshow("Original Image", image)
cv2.imshow("Mean Filtresi Uygulanmis Goruntu", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
