# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 上午10:20 GMT+8

from scrapy_plus.conf.settings import HEADERS

class Request():

    def __init__(self, url, method='GET', data=None,
                 headers=HEADERS, meta={}, parse='parse',
                 filter=True):

        self.url = url
        self.method = method
        self.data = data
        self.headers = headers

        self.meta = meta
        self.parse = parse

        self.filter = filter # 默认为True表示过滤重复请求!