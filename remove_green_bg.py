"""
Program: Green background removal from specific image
Course: PDSI
Author: Esther de Freitas
Description:
    This program removes green areas from an image (chroma key) and generates a new
    image with an alpha channel, preserving the rest of the image. It also displays
    intermediate and final images resized to fit the user's screen.

Libraries used:
    - OpenCV (cv2): for image manipulation and mask operations.
    - NumPy (np): for mathematical operations and array manipulation.
    - screeninfo: to get monitor dimensions and resize images accordingly.
"""

import cv2
import numpy as np
from screeninfo import get_monitors


#Displays images resized to fit the screen
def show_image(img, label):
    # Get main monitor dimensions
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height

    # Get image height and width
    h, w = img.shape[:2]

    # Calculate scale to fit screen while keeping aspect ratio
    scale_w = screen_width / w
    scale_h = screen_height / h
    scale = min(scale_w, scale_h) * 0.5
    new_w = int(w * scale)
    new_h = int(h * scale)

    # Resize and display the image
    img_resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    # scale = 0.25  # 50% do tamanho
    # img_resized = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    cv2.imshow(label, img_resized)

# Load the image
img = cv2.imread('womansmile.jpg')
if img is None:
    print("Erro: imagem não encontrada")
    exit()
# cv2.imshow("Original", img)

# Define reference green color for removal (BGR)
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
hsv_green_transform = np.array(hsv_green)
hsv_green_array = hsv_green_transform.reshape(-1, hsv_green_transform.shape[-1])[0]
# print(hsv_green_array)

# Convert the image to HSV for easier color detection
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define green range for mask
lower = np.array([40, 30, 20], dtype=np.uint8)
upper = np.array(hsv_green_array)

# Create mask for green background color
mask = cv2.inRange(hsv, lower, upper)

# Apply inverted mask to remove green background
res = cv2.bitwise_not(img, img, mask=mask)

# Display mask and intermediate result
# cv2.imshow("Mascara", mask)
show_image(mask, "mask")
# cv2_imshow(hsv)
# cv2.imshow("SemVerde", res)
show_image(res, "res")

# Create final image with transparent background
alpha_channel = cv2.bitwise_not(mask)
b, g, r = cv2.split(img)
img_without_bg = cv2.merge([b, g, r, alpha_channel])

# Display final image and save as PNG with transparency
# cv2.imshow("SemBG", img_without_bg)
show_image(img_without_bg, "img_without_bg")
cv2.imwrite('img_without_bg.png', img_without_bg)

# Wait for ESC key to close all windows
while k := cv2.waitKey(5) & 0xFF:
    if k == 27:
        break
cv2.destroyAllWindows()
