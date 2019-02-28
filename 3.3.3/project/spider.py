# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-1 下午2:47 GMT+8

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request

class BaiduSpider(Spider):

    start_urls = ['http://www.itcast.cn'] * 2

    def parse(self, response):
        print(111)
        yield Request(self.start_urls[0])