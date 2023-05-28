"""A script that creates a collage of images from a folder."""
from email.mime import image
import os
from typing import Any
import cv2
import numpy as np
from numpy import ndarray, generic, dtype

COLUMNS_CONST = 3
ROWS_CONST = 2
H_MARGIN = 10
V_MARGIN = 20

images = os.listdir("Section 12_Image processing/images/collage")
image_objects = [
    cv2.imread(f"Section 12_Image processing/images/collage/{image}")
    for image in images
]
print(images)

# this requires all images to be the same size
shape = cv2.imread(f"Section 12_Image processing/images/collage/{images[0]}").shape
print(shape)

outer_image: ndarray[Any, dtype[generic]] = np.zeros(
    shape=(
        shape[0] * ROWS_CONST + V_MARGIN * (ROWS_CONST + 1),
        shape[1] * COLUMNS_CONST + H_MARGIN * (COLUMNS_CONST + 1),
        3,
    ),
    dtype=np.uint8,
)

outer_image.fill(255)

positions = [(x, y) for x in range(COLUMNS_CONST) for y in range(ROWS_CONST)]

for (pos_x, pos_y), image in zip(positions, image_objects):
    x = pos_x * (shape[1] + (H_MARGIN)) + H_MARGIN
    y = pos_y * (shape[0] + (V_MARGIN)) + V_MARGIN
    outer_image[y : y + shape[0], x : x + shape[1]] = image

cv2.imwrite("Section 12_Image processing/images/collage/collage.jpg", outer_image)
