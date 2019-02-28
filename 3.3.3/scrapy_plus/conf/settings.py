# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午6:17 GMT+8


from scrapy_plus.conf.default_settings import *
# DEFAULT_LOG_FILENAME = 'log.log'

# 从哪里执行就从哪里导包
from settings import * # 这个settings是项目中的settings.py
# DEFAULT_LOG_FILENAME = '日志.log'    # 日志文件名称
# 此时项目中的配置就覆盖了框架中的配置!
# 注意 一定要在框架配置文件的最后 导入项目中的配置!


