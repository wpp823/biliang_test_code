# -*- coding:utf-8 -*-
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def img_author():
    # 创建掩膜
    img = cv2.imread('./header.png')

    x = 140
    y = 100
    r = 80
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask = cv2.circle(mask, (x, y), r, (255, 255, 255), -1)

    image2 = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)

    cv2.imshow("image", image2)



# 安装库：pip install Pillow

n = int((420 - 4 - 3) / 20)  # 背景宽度/字体大小， # 行字数
articles = "  （1）尽可能追寻病因，隔绝致敏原，避免再刺激。去除病灶，治疗全身慢性疾患，如消化不良、肠寄生虫病、糖尿病、精神神经异常、小腿静脉曲张等。"
articles_list = [articles[i:i + n] for i in range(0, len(articles), n)]

# 图片名称
img = 'background.png'  # 图片模板
new_img = 'text123.png'  # 生成的图片
compress_img = 'compress.png'  # 压缩后的图片

# 设置字体样式
font_type = '/System/Library/Fonts/PingFang.ttc'
# font_medium_type = '/System/Library/Fonts/STHeiti Medium.ttc'
# header_font = ImageFont.truetype(font_medium_type, 55)
# title_font = ImageFont.truetype(font_medium_type, 45)
font = ImageFont.truetype(font_type, 20)
color = "#333333"

# 打开图片
image = Image.open(img)
draw = ImageDraw.Draw(image)
width, height = image.size

print(image.size)

# 文章内容
articles_x = 4
articles_y = 336 - 59
summary_line = 23
# draw.multiline_textbbox()
for num, summary in enumerate(articles_list):
    y = articles_y - num * summary_line
    draw.text((articles_x, height - y), u'%s' % summary, color, font)

# 头像
heard_image = Image.open('./header.png')
print(heard_image.size)
draw = ImageDraw.Draw(image)
header_x = 11
header_y = 45
box = (4, 4, 39, 39)  # 底图上需要P掉的区域 头像的位置

# 将头像裁切成圆形
img_author()
# image.show()

# 加载需要P上去的图片
# tmp_img = Image.open(ur'D:\Desktop\2.png')
# 这里可以选择一块区域或者整张图片
# region = tmp_img.crop((0,0,304,546)) #选择一块区域
# 或者使用整张图片
region = heard_image

region = region.resize((box[2] - box[0], box[3] - box[1]))

image.paste(region, box)

# doctor_name
doctor_name_x = 54
doctor_name_y = 15

doctor_name = "张大海"
doctor_font_type = '/System/Library/Fonts/PingFang.ttc'
# font_medium_type = '/System/Library/Fonts/STHeiti Medium.ttc'
# header_font = ImageFont.truetype(font_medium_type, 55)
# title_font = ImageFont.truetype(font_medium_type, 45)
doctor_font = ImageFont.truetype(doctor_font_type, 17)

draw.text((doctor_name_x, doctor_name_y), u'%s' % doctor_name, color, doctor_font)

# 生成图片
image.save(new_img, 'png')

# 压缩图片
sImg = Image.open(new_img)
w, h = sImg.size
width = int(w / 2)
height = int(h / 2)
dImg = sImg.resize((width, height), Image.ANTIALIAS)
dImg.save(compress_img)
