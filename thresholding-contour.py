"""
Program: Thresholding Image Contour
Course: PDSI
Author: Esther de Freitas
Description:
    This program

Libraries used:
    - OpenCV (cv2): for image manipulation and mask operations.
    - NumPy (np): for mathematical operations and array manipulation.
"""

import cv2
import numpy as np

image = cv2.imread('./img/me.jpg')
cv2.imshow('Original', image)

# Máscara inicial
mask = np.zeros(image.shape[:2], np.uint8)
background_model = np.zeros((1,65), np.float64)
foreground_model = np.zeros((1,65), np.float64)

rect = (10, 10, image.shape[1]-30, image.shape[0]-30)  # região da pessoa
cv2.grabCut(image, mask, rect, background_model, foreground_model, 5, cv2.GC_INIT_WITH_RECT)

# Cria máscara binária (pessoa=1, fundo=0)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype("uint8")

# Achar contornos
contours, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar só a linha do contorno
outline = np.zeros_like(image)
cv2.drawContours(outline, contours, -1, (255,255,255), thickness=2)  # linha branca

cv2.imwrite('./img/out/outline.jpg', outline)
cv2.imshow("Contorno", outline)
cv2.waitKey(0)
cv2.destroyAllWindows()
