"""
Program: Adaptative Thresholding Image
Course: PDSI
Author: Esther de Freitas
Description:
    This program

Libraries used:
    - OpenCV (cv2): for image manipulation and mask operations.
    - NumPy (np): for mathematical operations and array manipulation.
"""

import cv2

image = cv2.imread('./img/booksonthetable.jpeg', 0)
cv2.imshow('Original', image)
cv2.waitKey(0)

image = cv2.GaussianBlur(image, (3, 3), 0)
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
cv2.imshow('Adaptive Mean Thresholding', thresh)
cv2.imwrite('./img/out/adaptative-thresholding-image.jpg', thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()