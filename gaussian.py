import cv2
import numpy as np

def gaussian_kernel(size, sigma=1):
    #Generate a Gaussian kernel.
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma**2)) * np.exp(
            -((x - (size - 1) / 2)**2 + (y - (size - 1) / 2)**2) / (2 * sigma**2)
        ),
        (size, size)
    )
    return kernel / np.sum(kernel)

def apply_convolution(image, kernel):
    """Apply convolution to an image using a given kernel."""
    image = np.array(image, dtype=np.float32)
    height, width, _ = image.shape
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2

    # Pad the image with zeros to handle border pixels
    padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='constant')

    # Create an output image of the same size
    new_image = np.zeros_like(image)

    # Apply convolution
    for y in range(height):
        for x in range(width):
            for c in range(3):  # Iterate over the color channels
                region = padded_image[y:y + kernel_size, x:x + kernel_size, c]
                new_image[y, x, c] = np.sum(region * kernel)

    # Clip the values to ensure they are within 0-255
    new_image = np.clip(new_image, 0, 255).astype(np.uint8)

    return new_image

# Read the image using OpenCV
input_image_path = "Images/Lenna.png"  # Change this to the path of your image
image = cv2.imread(input_image_path)

# Generate a 3x3 Gaussian kernel
kernel = gaussian_kernel(3, sigma=1)

# Apply the Gaussian filter
filtered_image = apply_convolution(image, kernel)

# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
