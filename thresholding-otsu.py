"""
Program: OTSU Thresholding Image
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

_, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Otsu 's_Thresholding", thresh)
cv2.imwrite('./img/out/otsu-thresholding-image.jpg', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

