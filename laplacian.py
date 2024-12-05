from PIL import Image
import cv2
def pixelsSum(image, matrix, sayi, x, y):
    pixelSum = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            pixelSum += image.getpixel((x + j, y + i))[sayi] * matrix[i][j]
    return pixelSum

def Conv3x3(image, matrix, factor, offset):
    width, height = image.size
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            color = (pixelsSum(image, matrix, 0, x, y) / factor) + offset

            image.putpixel((x, y), (int(color), int(color), int(color)))

    return image

matrix = ((-1,0,-1),
          (0,4,0),
          (-1,0,-1))
factor = 9
offset = 127

input_image_path = "Images/Lenna.png"
image = Image.open(input_image_path)
image.show("Orijinal Goruntu")
output_image = Conv3x3(image, matrix, factor, offset)
output_image.show("Laplacian Goruntu")

