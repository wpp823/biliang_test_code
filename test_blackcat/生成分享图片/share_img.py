from io import BytesIO
from typing import Tuple

import cv2
import numpy as np
import requests
from PIL import Image, ImageFont, ImageDraw


def header_img_author(header_img_url, width, height):
    """
    将医生头像转化为圆形

    :return: ndarray 类型数组
    """

    img = cv2.imread(header_img_url)
    # 创建掩膜

    if width > height:
        x = y = r = int(height / 2)
    else:
        x = y = r = int(width / 2)
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask = cv2.circle(mask, (x, y), r, (255, 255, 255), thickness=-1)
    mask2 = cv2.circle(mask, (x, y), r, (255, 255, 255), thickness=2)

    cv2.imshow("mask2",mat=mask2)
    image_array = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)

    img2 = Image.fromarray(image_array)
    img2 = cv2.imdecode(img2)

    image_array2 = cv2.add(img2, np.zeros(np.shape(img), dtype=np.uint8), mask=mask2)


    # 转化颜色
    image_array = cv2.cvtColor(image_array2, cv2.COLOR_BGR2RGB)

    return image_array


def create_background(width, height, car_background: Tuple = None):
    """
    创建背景大小区域

    :param width:
    :param height:
    :param car_background:
    :return:
    """
    car_total_with = width
    car_total_height = height
    if not car_background:
        car_background = (255, 255, 255, 255)

    return Image.new('RGBA', size=(car_total_with, car_total_height), color=car_background)


def trans2non(img):
    """
    将黑色背景转为透明

    :param img:
    :return:
    """
    b_img = img.convert('RGBA')
    L, H = b_img.size
    color_0 = b_img.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = b_img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                b_img.putpixel(dot, color_1)
    return b_img


# image.save('background.png')


if __name__ == "__main__":
    # 图片总大小
    b_width = 420  # 背景宽度
    b_height = 336  # 背景高度



    # 医生姓名
    doctor_name_x = 53
    doctor_name_y = 310

    doctor_name = "张大海"
    doctor_font_type = '/System/Library/Fonts/PingFang.ttc'
    doctor_name_font_color = "#333333"
    doctor_name_font_size = 17  # 医生姓名字体大小
    doctor_font = ImageFont.truetype(doctor_font_type, doctor_name_font_size)

    # 创建背景图
    background_img = create_background(b_width, b_height)

    background_draw = ImageDraw.Draw(background_img)

    # 创建封面图
    cover_img_url = "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/limit/xlkk/2021-12-30/1640852220_AwVWGaPr_1.png"

    cover_img_box = (0, 0, 420, 310)
    # 获取图片
    response = requests.get(cover_img_url)
    cover_img = Image.open(BytesIO(response.content)).convert("RGB")

    # 图片等比例缩小
    cover_img = cover_img.resize((cover_img_box[2], cover_img_box[3]))
    # cover_img.show("cover_img")
    background_img.paste(cover_img, cover_img_box)
    background_img.save("background_img1.png", 'png')


    # 头像处理
    header_img_url = './header.png'
    heard_image = Image.open('./header.png')

    heard_width = heard_image.width
    heard_height = heard_image.height

    # 将头像转化圆形头像
    heard_author_array = header_img_author(width=heard_width, header_img_url=header_img_url, height=heard_height)

    # 添加头像
    # 医生头像设置
    img_size = (46,46)
    header_box = (1, 286, 1+int(img_size[0]),286+int(img_size[1]))  # 底图上需要P掉的区域 头像的位置

    heard_author_image = Image.fromarray(heard_author_array)
    # heard_author_image.save("18.png", "png")
    # heard_draw = ImageDraw.Draw(heard_author_image)
    new_header_image = trans2non(heard_author_image).convert('RGBA')
    new_header_image.save("19.png", "png")
    # heard_region = new_header_image
    heard_region = new_header_image.resize(img_size)
    # heard_region.show("heard_region")
    # heard_region.save("20.png", "png")

    background_img.paste(heard_region, header_box, heard_region)
    background_img.save("background_img2.png", 'png')

    #  添加医生名称
    background_draw.text((doctor_name_x, doctor_name_y), u'%s' % doctor_name, doctor_name_font_color, doctor_font)
    background_img.show("test_main")
    background_img.save("test_main.png", 'png')
