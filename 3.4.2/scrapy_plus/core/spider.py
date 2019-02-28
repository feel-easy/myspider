# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 上午10:19 GMT+8

from scrapy_plus.http.request import Request
from scrapy_plus.item import Item


class Spider():

    name = ''

    start_urls = []


    def start_requests(self):
        # 对起始url构造request并返回
        for url in self.start_urls:
            yield Request(url)


    def parse(self, response):
        yield Item(response)