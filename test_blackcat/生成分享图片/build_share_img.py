import textwrap
from io import BytesIO
from typing import Tuple

import requests
from PIL import ImageFont, Image, ImageDraw

# from app.conf.setting import DOC_NAME_FONT_TYPE, COVER_IMG_DOC_NAME_FONT_TYPE
# from app.conf.setting_base import ART_FONT_TYPE
# from app.util.logger import get_logger

# 背景配置
from utils.logger import get_logger

B_WIDTH = 420  # 背景宽度
B_HEIGHT = 336  # 背景高度

# 文章区域配置
ART_FONT_SIZE = 21  # 文章字体大小
ART_POSITION_X = 4  # # 文章内容坐标x
ART_POSITION_Y = 336 - 59  # # 文章内容坐标y
ART_FONT_TYPE = '/System/Library/Fonts/PingFang.ttc'  # 字体类型
ART_LINE = 20  # 行间距
ART_FONT_COLOR = "#333333"  # 文章字体颜色
ART_FONT_OBJ = ImageFont.truetype(ART_FONT_TYPE, ART_FONT_SIZE)  # 文章字体对象
ART_LINE_WORDS = int((B_WIDTH - ART_POSITION_X) / ART_FONT_SIZE)  # 行字数
ART_ROWS = int(ART_POSITION_Y / ART_FONT_SIZE) - 1  # 行数
# 医生头像区域配置
DOC_HEADER_PIC_SIZE = (39, 39)
DOC_HEADER_PIC_BOX = (4, 4, 4 + DOC_HEADER_PIC_SIZE[0], 4 + DOC_HEADER_PIC_SIZE[1])  # 底图上需要P掉的区域 头像的位置

# 医生姓名区域配置
DOC_NAME_POSITION_X = 54  # 医生姓名坐标x
DOC_NAME_POSITION_Y = 15  # 医生姓名坐标y
DOC_NAME_FONT_TYPE = '/System/Library/Fonts/PingFang.ttc'  # 医生姓名字体
DOC_NAME_FONT_COLOR = "#333333"  # 医生姓名字体颜色
DOC_NAME_FONT_SIZE = 17  # 医生姓名字体大小
DOC_NAME_FONT_OBJ = ImageFont.truetype(DOC_NAME_FONT_TYPE, DOC_NAME_FONT_SIZE)

# 图片内容的配置
# 医生姓名
COVER_IMG_DOC_POSITION_X = 53
COVER_IMG_DOC_POSITION_Y = 310

COVER_IMG_DOC_NAME_FONT_TYPE = '/System/Library/Fonts/PingFang.ttc'
COVER_IMG_DOC_NAME_FONT_COLOR = "#333333"
COVER_IMG_DOC_NAME_FONT_SIZE = 17  # 医生姓名字体大小
COVER_IMG_DOC_NAME_FONT_OBJ = ImageFont.truetype(COVER_IMG_DOC_NAME_FONT_TYPE, COVER_IMG_DOC_NAME_FONT_SIZE)

# 封面图片配置
COVER_IMG_SIZE = (420, 310)
COVER_IMG_POSITION_BOX = (0, 0, 0 + COVER_IMG_SIZE[0], 0 + COVER_IMG_SIZE[1])

# 医生头像配置
COVER_IMG_HEADER_SIZE = (46, 46)
COVER_IMG_HEADER_RING_WIDTH = 4  # 头像边框的宽度  非px，未缩放之前的大小
COVER_IMG_HEADER_BOX = (1, 286, 1 + int(COVER_IMG_HEADER_SIZE[0]), 286 + int(COVER_IMG_HEADER_SIZE[1]))  # 底图上需要P掉的区域 头像的位置


class BuildShareImgTools():

    def __init__(self,log):
        self.log = log

    def header_img_author(self, header_img_url):
        """
        将头像转换为圆形头像

        @param header_img_url: 头像地址
        @return:
        """
        img_req = requests.get(url=header_img_url)

        ima = Image.open(BytesIO(img_req.content)).convert("RGBA")
        # ima = Image.frombytes(img_req.content)
        size = ima.size
        # 因为是要圆形，所以需要正方形的图片
        r2 = min(size[0], size[1])
        if size[0] != size[1]:
            ima = ima.resize((r2, r2), Image.ANTIALIAS)
        imb = Image.new('RGBA', (r2, r2), (255, 255, 255, 0))
        pima = ima.load()
        pimb = imb.load()
        r = float(r2 / 2)  # 圆心横坐标
        for i in range(r2):
            for j in range(r2):
                lx = abs(i - r + 0.5)  # 到圆心距离的横坐标
                ly = abs(j - r + 0.5)  # 到圆心距离的纵坐标
                l = pow(lx, 2) + pow(ly, 2)
                if l <= pow(r, 2):
                    pimb[i, j] = pima[i, j]
        # imb.show("header_img_author")
        return imb
        # imb.save("test_circle.png")

    def header_img_author_ring(self, header_img_url):
        """
        带圆环的圆形头像

        @param header_img_url: 头像地址
        @return:
        """
        img_author = self.header_img_author(header_img_url)

        # ima = Image.open("test_circle.png").convert("RGBA")
        size = img_author.size
        # # 因为是要圆形，所以需要正方形的图片
        r2 = min(size[0], size[1])
        if size[0] != size[1]:
            img_author = img_author.resize((r2, r2), Image.ANTIALIAS)

        pima = img_author.load()
        r = float(r2 / 2)  # 圆心横坐标
        for i in range(r2):
            for j in range(r2):
                lx = abs(i - r)  # 到圆心距离的横坐标
                ly = abs(j - r)  # 到圆心距离的纵坐标
                l = pow(lx, 2) + pow(ly, 2)
                # print(pima[i, j])
                if pow(r, 2) >= l > pow(r - COVER_IMG_HEADER_RING_WIDTH, 2):
                    pima[i, j] = (255, 255, 255, 255)

        # img_author.show("header_img_author_ring")
        return img_author
        # ima.save("test_circle1.png")

    def create_background(self, width, height, car_background: Tuple = None):
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

    def build_content_img(self, doc_avatar_url, doc_name, article_text):
        """
        生成文本分享内容图片

        @param doc_avatar_url:
        @param doc_name:
        @param article_text:
        @return:
        """

        img_content = None
        try:
            # 创建背景图
            background_img = self.create_background(B_WIDTH, B_HEIGHT)
            background_draw = ImageDraw.Draw(background_img)

            # 头像处理
            # response = requests.get(doc_avatar_url)
            # 将头像转化圆形头像
            new_header_image = self.header_img_author(header_img_url=doc_avatar_url)  # 进行圆形遮罩
            heard_region = new_header_image.resize(DOC_HEADER_PIC_SIZE)  # 等比例缩放
            background_img.paste(heard_region, DOC_HEADER_PIC_BOX, heard_region)  # 粘贴头像
            #  添加医生名称
            background_draw.text((DOC_NAME_POSITION_X, DOC_NAME_POSITION_Y), u'%s' % doc_name, DOC_NAME_FONT_COLOR, DOC_NAME_FONT_OBJ)

            # 添加文字内容
            # 处理文章过长，多余内容省略

            article_position_list = self.get_duanluo(article_text).split('\n')
            if len(article_position_list) >= ART_ROWS:
                article_position_list = article_position_list[:ART_ROWS]
                article_position_list[-1] = article_position_list[-1][:-3]+ " ......"

            # 将文字画上画布
            for num, text_content in enumerate(article_position_list):
                w, h = background_draw.textsize(text_content, font=ART_FONT_OBJ)
                y = ART_POSITION_Y - num * ART_LINE
                if num == len(article_position_list)-1:
                    background_draw.text((ART_POSITION_X, B_HEIGHT - y), text_content, ART_FONT_COLOR, font=ART_FONT_OBJ, spacing=0)
                else:
                    background_draw.text(((B_WIDTH - w) / 2, B_HEIGHT - y), text_content, ART_FONT_COLOR, font=ART_FONT_OBJ, spacing=0)

            # background_img.show("完成图片")
            bytes_io = BytesIO()
            background_img.save(bytes_io, format='PNG')
            img_content = bytes_io.getvalue()

        except Exception as e:
            self.log.exception("[ArticlesContentImgHandler.get._build_content_img_fail][article_text:{},doc_name:{},doc_avatar_url:{}]"
                               .format(article_text, doc_name, doc_avatar_url))

        return img_content

    def get_duanluo(self, text):
        """
        获取段落排版

        :param text:
        :return:
        """
        txt = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
        txt_draw = ImageDraw.Draw(txt)
        # 所有文字的段落
        duanluo = ""
        # 宽度总和
        sum_width = 0
        # 几行
        line_count = 1
        for char in text:
            width, height = txt_draw.textsize(char, ART_FONT_OBJ)
            sum_width += width
            if sum_width > B_WIDTH-20:  # 超过预设宽度就修改段落 以及当前行数
                line_count += 1
                sum_width = 0
                duanluo += '\n'
            duanluo += char
            if line_count > int(B_HEIGHT/25):
                break
        return duanluo

    def build_cover_content_img(self, doc_avatar_url, doc_name, cover_url):
        """
        生成封面分享的文章图片

        @param doc_avatar_url:
        @param doc_name:
        @param cover_url:
        @return:
        """
        img_content = None
        try:
            # 创建背景图
            background_img = self.create_background(B_WIDTH, B_HEIGHT)
            background_draw = ImageDraw.Draw(background_img)
            # 背景图处理
            cover_response = requests.get(cover_url)

            # cover_img_box = (0, 0, 420, 310)
            cover_img = Image.open(BytesIO(cover_response.content)).convert("RGB")
            # 图片等比例缩小
            cover_img = cover_img.resize(COVER_IMG_SIZE)
            # cover_img.show("cover_img")
            background_img.paste(cover_img, COVER_IMG_POSITION_BOX)
            # 头像处理
            # response = requests.get(doc_avatar_url)
            # 将头像转化圆形头像
            new_header_image = self.header_img_author_ring(header_img_url=doc_avatar_url)  # 进行圆形遮罩
            heard_region = new_header_image.resize(COVER_IMG_HEADER_SIZE)  # 等比例缩放
            background_img.paste(heard_region, COVER_IMG_HEADER_BOX, heard_region)  # 粘贴头像

            #  添加医生名称
            background_draw.text((COVER_IMG_DOC_POSITION_X, COVER_IMG_DOC_POSITION_Y), u'%s' % doc_name, COVER_IMG_DOC_NAME_FONT_COLOR, COVER_IMG_DOC_NAME_FONT_OBJ)

            # background_img.show("build_cover_content_img")
            bytes_io = BytesIO()
            background_img.save(bytes_io, format='PNG')
            img_content = bytes_io.getvalue()
        except Exception as e:
            self.log.exception("[ArticlesContentImgHandler.get._build_content_img_fail][article_text:{},doc_name:{}]"
                               .format(doc_name, doc_avatar_url))

        return img_content


if __name__ == "__main__":
    # log = get_logger("blackcat_build_share_img.log")
    build_tool = BuildShareImgTools(log=None)
    doc_avatar_url_s = "https://allmark.oss-cn-shenzhen.aliyuncs.com/xlkk/%E7%94%B72-100.jpg"
    doc_name_s = "张大仙"
    article_text_s = "血脂包括甘油三酯、胆固醇、低密度脂蛋白与高密度脂蛋白。血脂6.8mmol/L较为笼统，对于甘油三酯在1.7mmol/L以上，称之为高血脂症，血脂6.8mmol/L则为较高数值，存在诱发胰腺炎的危险。胆固醇的上限在5.0mmol/L，6.8mmol/L则属于轻度升高。 "
    cover_url_s = "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/limit/xlkk/2021-12-30/1640852220_AwVWGaPr_1.png"
    # 文字内容分享图片
    img = build_tool.build_content_img(doc_avatar_url=doc_avatar_url_s, doc_name=doc_name_s, article_text=article_text_s)
    # 封面图内容分享图片

    # img = build_tool.build_cover_content_img(doc_avatar_url=doc_avatar_url_s, doc_name=doc_name_s, cover_url=cover_url_s)

    img_obj = Image.open(BytesIO(img))
    img_obj.show("ddd")