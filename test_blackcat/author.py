import cv2

import numpy as np
from PIL import Image

imgName = './header.png'

img = cv2.imread(imgName)

# 展示原图

# cv2.imshow("img", img)

# 创建掩膜

x = int(1024/2)

y = int(1024/2)

r = int(1024/2)

mask = np.zeros(img.shape[:2], dtype=np.uint8)

mask = cv2.circle(mask, (x, y), r, (255, 255, 255), -1)

image = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)

# print(image)

# 展示掩膜图片
heard_image = Image.fromarray(image)
# image.save("header_autr.png")
heard_image.save("111.png", 'RGB')
# cv2.imshow("mask", mask)
#
# # 展示添加掩膜效果图片
#
# cv2.imshow("image", image)
#
# cv2.waitKey()
#
# cv2.destroyAllWindows()