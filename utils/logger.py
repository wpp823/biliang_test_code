__author__ = 'commissar'

import logging
import logging.config
import os
# from app.util.logging_timed_rotating_file_handler import MultiProcessTimedRotatingFileHandler

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


