# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午5:04 GMT+8

from scrapy_plus.core.engine import Engine

from spider import BaiduSpider


if __name__ == '__main__':

    spider = BaiduSpider()

    engine = Engine(spider)
    engine.start()