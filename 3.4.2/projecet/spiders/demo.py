# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-2 上午11:47 GMT+8
import time
from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request

class DemoSpider(Spider):

    name = 'baidu'

    start_urls = ['https://www.360.cn/']    # 设置初始请求url

    def start_requests(self):
        time.sleep(2)
        print(111)
        yield Request(self.start_urls[0], parse='start_requests', filter=False)




