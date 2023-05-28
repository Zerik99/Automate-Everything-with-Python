"""an app that replaces the green background of an image with another image"""
from typing import Any
import cv2
import numpy as np
from numpy import ndarray, generic, dtype

foreground: ndarray[int, dtype[generic]] = cv2.imread(
    "Section 12_Image processing/images/giraffe.jpeg"
)
background: ndarray[int, dtype[generic]] = cv2.imread(
    "Section 12_Image processing/images/safari.jpeg"
)


width: int = foreground.shape[1]
width_iter = [i for i in range(width)]

height: int = foreground.shape[0]
height_iter = [i for i in range(height)]

screen_color: list[int] = [28, 255, 76]

background_resized: ndarray[int, dtype[generic]] = cv2.resize(
    background, (width, height), interpolation=cv2.INTER_AREA
)

# I keep getting an index error here. I'm not sure why.
# update: the index error was because I was using the wrong index for the width and height.
# Version using list comprehension below.
# for i in range(width):
#     for j in range(height):
#         if np.any(foreground[j, i] == screen_color):
#             foreground[j, i] = background_resized[j, i]

# Was able to figure this out with Chat GPT and a lot of trial and error.
# list comprehension can be used. Once the list is created, it can be reshaped into the original shape of the foreground.
giraffe_greenscreened: list[Any] = [
    background_resized[j, i]
    if foreground[j, i][1] > screen_color[1] - 2
    and foreground[j, i][1] < screen_color[1] + 2
    else foreground[j, i]
    for j in height_iter
    for i in width_iter
]
foreground = np.array(giraffe_greenscreened).reshape(foreground.shape)

cv2.imwrite("Section 12_Image processing/images/giraffe_greenscreened.jpg", foreground)
