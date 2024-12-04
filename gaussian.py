import cv2

# Resim yolunu belirtiyoruz.
input_image_path = "Images/Lenna.png"

# Fotoğrafı açıyoruz (renkli olarak).
image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

# Gauss bulanıklaştırma işlemi
# (5, 5) kernel boyutu ve 0 standart sapma değeri kullanıyoruz.
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Orijinal ve bulanıklaştırılmış fotoğrafı ekranda gösteriyoruz.
cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Gaussian Blur Goruntu", gaussian_blur)

# Bulanıklaştırılmış fotoğrafı belirtilen bir dosya adıyla kaydediyoruz.
cv2.imwrite("Images/gaussian_blur.png", gaussian_blur)

# Çıkış için bir tuşa basmayı bekleme
cv2.waitKey(0)
cv2.destroyAllWindows()