# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-1 下午3:49 GMT+8

from scrapy_plus.core.spider import Spider


# 继承框架的爬虫基类
class BaiduSpider(Spider):
    name = 'baidu'
    start_urls = ['http://www.baidu.com']    # 设置初始请求url