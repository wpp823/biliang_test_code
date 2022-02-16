import logging
import os
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

# if not os.path.exists(f'{os.getcwd()}\\bin'):
#     os.mkdir(f'{os.getcwd()}\\bin')

# 日志文件夹
if not os.path.exists(f'{os.getcwd()}/logs/'): os.mkdir(f'{os.getcwd()}/logs/')
log_path = os.getcwd() + '/logs'
print(f"log_path：{log_path}")
# # 日志格式
formatter = '%(asctime)s-%(filename)s-[line]: %(lineno)d-%(levelname)s-%(message)s'

# 日志文件按时间切分
# interval： 指定日志文件轮转的周期，如 when='S', interval=10，表示每10秒轮转一次，when='D', interval=7，表示每周轮转一次。
# backupCount： 指定日志文件保留的数量，指定一个整数，则日志文件只保留这么多个，自动删除旧的文件
time_rotate_file = TimedRotatingFileHandler(filename=f'{log_path}log', when='D', interval=1, backupCount=20)
time_rotate_file.setFormatter(logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M'))
time_rotate_file.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(level=logging.INFO)
console_handler.setFormatter(logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M'))

logger.addHandler(time_rotate_file)
logger.addHandler(console_handler)
