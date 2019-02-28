# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午12:24 GMT+8


from scrapy_plus.conf.default_settings import * # 框架配置
# DEFAULT_LOG_FILENAME = 'log.log'    # 默认日志文件名称

# 在框架的配置文件的最后导入!!!!一定要最后!让项目配置覆盖框架配置
# 从哪里执行就从哪里导包
# 下面的settings就是项目路径下settings.py模块!
from settings import * # 项目配置
# DEFAULT_LOG_FILENAME = '日志.log'

