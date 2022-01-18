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
    mask = cv2.circle(mask, (x, y), r, (255, 255, 255, 0), -1)
    image_array = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)
    # 转化颜色
    image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)

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

    # 文章区域配置
    article_font_size = 20  # 文章字体大小
    article_x = 4  # 文章内容坐标x
    article_y = 336 - 59  # 文章内容坐标y
    article_font_type = '/System/Library/Fonts/PingFang.ttc'  # 字体类型
    article_line = 23  # 行间距
    article_font_color = "#333333"
    # 计算文本最大行数

    article_font = ImageFont.truetype(article_font_type, article_font_size)
    line_char_num = int((b_width - article_x) / article_font_size)  # 行字数
    rows_num = int(article_y / article_font_size) - 1  # 行数
    print(f"行数{rows_num}")
    # 测试内容
    article_text = "  （1）尽可能追寻病因，隔绝致敏原，时代撒打扫打扫打扫打扫未发起方为人飞飞飞是否，废弃物废弃物，浮球阀，起违法违规去外地却无法发起违反签完到期未付清我发的，我的钱未付钱我都却无法，去外地却无法去外地，且歌且舞，当前我国前，我都签完非官方个外人，额，费，费，违法，违法全文，分期未发生想吃，的，吴青峰，千万人，犬瘟热，驱蚊器无付群无热群无，大声地奥术大师大或多撒阿萨德爱仕达多撒所大所大萨达萨达硕大的撒大，的，阿萨德，奥德赛，阿萨德，阿萨德欠发达，司法所发生大萨达十大事发地，阿萨德，阿萨法，萨达，手法是否，避免再刺激。去除病灶，治疗全身慢性疾患，如消化不良、肠寄生虫病、糖尿病、精神神经异常、小腿静脉曲张等。"
    # 处理文章过长，多余内容省略
    article_position_list = []
    for i in range(0, len(article_text), line_char_num):
        row_num = (i / article_font_size) + 1
        print(f"行数{row_num}")
        # article_position_list.append(text_content)
        if row_num >= rows_num:
            article_position_list.append(article_text[i:i + line_char_num - 3] + "  ......")
            break
        article_position_list.append(article_text[i:i + line_char_num])

    print(article_position_list)
    # article_position_list = [ article_text[i:i + line_char_num] if i > rows_num else article_text[i:i + line_char_num-3]+"..."
    #                           for i in range(0, len(article_text), line_char_num)]

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
    heard_author_image = Image.fromarray(heard_author_array)
    # heard_author_image.save("18.png", "png")
    # heard_draw = ImageDraw.Draw(heard_author_image)
    new_header_image = trans2non(heard_author_image).convert('RGBA')
    new_header_image.save("19.png", "png")
    # heard_region = new_header_image
    heard_region = new_header_image.resize((header_box[2] - header_box[0], header_box[3] - header_box[1]))
    heard_region.save("20.png", "png")
    # mouse_mask = mouse.convert("L")

    background_img.paste(heard_region, header_box, heard_region)

    #  添加医生名称
    background_draw.text((doctor_name_x, doctor_name_y), u'%s' % doctor_name, doctor_name_font_color, doctor_font)

    # 添加文字内容
    for num, text_content in enumerate(article_position_list):
        y = article_y - num * article_line
        background_draw.text((article_x, b_height - y), u'%s' % text_content, article_font_color, article_font,align='center')
        print(b_height - y)
        print(text_content)

    background_img.save("test_main.png", 'png')

    # # 压缩图片
    # sImg = Image.open(new_img)
    # w, h = sImg.size
    # width = int(w / 2)
    # height = int(h / 2)
    # dImg = sImg.resize((width, height), Image.ANTIALIAS)
    # dImg.save(compress_img)
