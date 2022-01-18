import cv2
import numpy as np
import PIL
from PIL import Image


def trans2non(a):
    b = a.convert('RGBA')
    L, H = b.size
    color_0 = b.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = b.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                b.putpixel(dot, color_1)
    return b


new_mask = Image.open("img.png")
new_mask = trans2non(new_mask)
new_mask.save('new_mask.png')
