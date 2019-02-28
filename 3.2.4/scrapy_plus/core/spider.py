# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8

from scrapy_plus.http.request import Request
from scrapy_plus.item import Item

class Spider():

    start_url = 'http://www.itcast.cn'

    def start_request(self):
        return Request(self.start_url)

    def parse(self, response):
        return Item(response.body)