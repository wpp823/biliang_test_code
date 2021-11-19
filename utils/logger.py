__author__ = 'commissar'

import logging
import logging.config
import os
from app.util.logging_timed_rotating_file_handler import MultiProcessTimedRotatingFileHandler

def get_logger( name="daredevil",config_file="conf/log.conf"):
    '''
    获取日志对象，
    :param name:            [string]日志对象名。
    :param config_file:     [string]日志配置文件。
    :return:
    '''

    logger = logging.getLogger(name)
    if logger.handlers:
        # or else, as I found out, we keep adding handlers and duplicate messages
        pass
    else:
        logging.config.fileConfig(config_file)
        logger = logging.getLogger(name)

    return logger


def get_logger_obj(name, level=logging.INFO, log_root='/var/log', day_rotating=True):
    '''

    :param name:    [string]日志名称
    :param level:       [string]日志等级
    :param conf_file:   [string]配置文件根数据 。
    :param in_spark_worker:     [bool]标志是否在spark的工作进程中使用些log.
    :param day_rotating:    [bool]是否按天滚动。
    :return:
    '''

    log_format = '%(asctime)s - %(name)s:%(filename)s:%(lineno)d:%(process)d - %(levelname)s - %(message)s'

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.handlers:
        # or else, as I found out, we keep adding handlers and duplicate messages
        pass
    else:

        if not os.path.exists(log_root):
            os.mkdir(log_root)

        file_log_path = os.path.join(log_root, name)

        if day_rotating:  # 按天滚动。
            # 增加文件输出。
            trf_param = {
                "filename": file_log_path,
                "when": 'MIDNIGHT',
                "encoding": "utf8",
                "backupCount": 30
            }
            file_handle = MultiProcessTimedRotatingFileHandler(**trf_param)
            file_handle.setLevel(level)
            formatter = logging.Formatter(log_format)
            file_handle.setFormatter(formatter)
            logger.addHandler(file_handle)
        else:
            rf_param = {
                "maxBytes": 100 * 1024 * 1024,  # 每个日志文件100M
                "backupCount": 9,
                "encoding": "utf8",
                "filename": file_log_path
            }
            file_handle = logging.handlers.RotatingFileHandler(**rf_param)
            file_handle.setLevel(level)
            formatter = logging.Formatter(log_format)
            file_handle.setFormatter(formatter)
            logger.addHandler(file_handle)

        # 增加控制台输出。
        # sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
        # ch = logging.StreamHandler(sys.stdout)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

# if __name__ == '__main__':
#     l = Logger('/users/zz/test.log')
#     b = l.get_logger()
#     b.info('abc')
