# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午12:26 GMT+8


DEFAULT_LOG_FILENAME = '日志.log'


# 启用的爬虫类
SPIDERS = [
    # 'spiders.baidu.BaiduSpider',
    'spiders.douban.DoubanSpider',
    'spiders.demo.DemoSpider'
]

# 启用的管道类
PIPELINES = [
    # 'pipelines.BaiduPipeline',
    'pipelines.DoubanPipeline'
]

# 启用的爬虫中间件类
# SPIDER_MIDDLEWARES = []

# 启用的下载器中间件类
# DOWNLOADER_MIDDLEWARES = []


# ASYNC_TYPE = 'coroutine'


# SCHEDULER_PERSIST = True