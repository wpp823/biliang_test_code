from PIL import Image

# width: 420px;
# height: 336px;
# background: #FFFFFF;

# 卡片总大小
car_total_with = 420
car_total_height = 336
car_background = (255, 255, 255)
image = Image.new('RGB',size=(car_total_with,car_total_height),color=car_background)

image.save('background.png')

# 内容============
# 文字内容
"""
width: 412.71px;
height: 137.08px;
font-family: PingFangSC-Regular;
font-size: 2188px;
color: #333333;
text-align: justify;
line-height: 3354px;
font-weight: 400;
"""


# 图片内容
# 头像 悬浮效果
image.show()