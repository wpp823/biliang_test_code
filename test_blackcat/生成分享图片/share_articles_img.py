from typing import Tuple

import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw


def header_img_author(header_img_url, width, height):
    """
    将医生头像转化为圆形

    :return: ndarray 类型数组
    """

    img = cv2.imread(header_img_url)
    # 创建掩膜
    # image = Image.open(img)
    # width, height = image.size
    if width > height:
        x = y = r = int(height / 2)
    else:
        x = y = r = int(width / 2)
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask = cv2.circle(mask, (x, y), r, (255, 255, 255), -1)
    image = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)

    return image


def create_background(width, height, car_background: Tuple = None):
    """
    创建背景大小区域

    :param width:
    :param height:
    :param color:
    :return:
    """
    car_total_with = width
    car_total_height = height
    if not car_background:
        car_background = (255, 255, 255)

    return Image.new('RGB', size=(car_total_with, car_total_height), color=car_background)
    # image.save('background.png')


if __name__ == "__main__":

    # 图片总大小
    b_width = 420  # 背景宽度
    b_height = 336  # 背景高度

    # 文章区域配置
    article_font_size = 20  # 文章字体大小
    article_x = 4  # 文章内容坐标x
    article_y = 336 - 59  # 文章内容坐标y
    article_font_type = '/System/Library/Fonts/PingFang.ttc'  # 字体类型
    article_line = 23  # 行间距
    article_font_color = "#333333"

    article_font = ImageFont.truetype(article_font_type, article_font_size)
    line_char_num = int((b_width - article_x) / article_font_size)  # 行字数
    # 测试内容
    article_text = "  （1）尽可能追寻病因，隔绝致敏原，避免再刺激。去除病灶，治疗全身慢性疾患，如消化不良、肠寄生虫病、糖尿病、精神神经异常、小腿静脉曲张等。"
    article_position_list = [article_text[i:i + line_char_num] for i in range(0, len(article_text), line_char_num)]

    # 医生头像设置
    header_x = 11
    header_y = 45
    header_box = (4, 4, 39, 39)  # 底图上需要P掉的区域 头像的位置

    # 医生姓名
    doctor_name_x = 54
    doctor_name_y = 15

    doctor_name = "张大海"
    doctor_font_type = '/System/Library/Fonts/PingFang.ttc'
    doctor_name_font_color = "#333333"
    doctor_name_font_size = 17  # 医生姓名字体大小
    doctor_font = ImageFont.truetype(doctor_font_type, doctor_name_font_size)

    # 创建背景图
    background_img = create_background(b_width, b_height)

    background_draw = ImageDraw.Draw(background_img)

    # 头像处理
    header_img_url = './header.png'
    heard_image = Image.open('./header.png')

    heard_width = heard_image.width
    heard_height = heard_image.height

    # 将头像转化圆形头像
    heard_author_array = header_img_author(width=heard_width, header_img_url=header_img_url, height=heard_height)

    # 添加头像
    # im_color = cv2.applyColorMap(heard_author_array,  cv2.COLOR_BGR2RGBA)
    # im_color = im_color[:, :, ::-1]
    # img1 = Image.fromarray(im_color, mode='RGB')
    heard_author_image = Image.fromarray(heard_author_array, mode='RGB')
    heard_author_image.save("heard_author_image.png", "png")
    # heard_draw = ImageDraw.Draw(heard_author_image)
    heard_region = heard_author_image
    heard_region = heard_region.resize((header_box[2] - header_box[0], header_box[3] - header_box[1]))

    background_img.paste(heard_region, header_box)

    #  添加医生名称
    background_draw.text((doctor_name_x, doctor_name_y), u'%s' % doctor_name, doctor_name_font_color, doctor_font)

    # 添加文字内容
    for num, summary in enumerate(article_position_list):
        y = article_y - num * article_line
        background_draw.text((article_x, b_height - y), u'%s' % summary, article_font_color, article_font)

    background_img.save("test_main.png", 'png')

    # # 压缩图片
    # sImg = Image.open(new_img)
    # w, h = sImg.size
    # width = int(w / 2)
    # height = int(h / 2)
    # dImg = sImg.resize((width, height), Image.ANTIALIAS)
    # dImg.save(compress_img)
