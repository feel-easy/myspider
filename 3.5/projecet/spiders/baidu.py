# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-1 上午10:03 GMT+8

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request

# 继承框架的爬虫基类
class BaiduSpider(Spider):

    name = 'baidu'

    start_urls = ['https://www.360.cn/']    # 设置初始请求url

    def parse(self, response):
        print(444)
        yield Request(self.start_urls[0], parse='parse2', filter=False)

    def parse2(self, response):
        print(1111)