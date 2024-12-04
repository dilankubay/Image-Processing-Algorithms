import cv2

# Resim yolunu belirtiyoruz.
resim_yolu = "Images/Lenna.png"

# Fotoğrafı açıyoruz (renkli olarak).
image = cv2.imread(resim_yolu, cv2.IMREAD_COLOR)

# Açılan fotoğrafı ekranda gösteriyoruz.
cv2.imshow("Orijinal Goruntu", image)

# RGB değerlerini kullanarak negatifini alıyoruz.
negative_image = 255 - image

# Negatif alınmış fotoğrafı ekranda gösteriyoruz.
cv2.imshow("Negatif Goruntu", negative_image)

# Negatif alınmış fotoğrafı belirtilen bir dosya adıyla kaydediyoruz.
cv2.imwrite("Images/negatif_goruntu.png", negative_image)

# Çıkış için bir tuşa basmayı bekleme
cv2.waitKey(0)
cv2.destroyAllWindows()