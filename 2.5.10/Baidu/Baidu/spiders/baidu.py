# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy_splash import SplashRequest


class BaiduSpider(RedisSpider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    # start_urls = ['https://www.baidu.com/s?wd=python']
    redis_key = 'baidu'

    # scrapy_redis两个爬虫类不能重写start_requests函数
    # def start_requests(self):

    def parse(self, response):
        url = 'https://www.baidu.com'
        yield SplashRequest(url,
                            callback=self.parse2,
                            args={'wait': 3},
                            endpoint='render.html')
        yield scrapy.Request(url,
                            callback=self.parse3)

    def parse2(self, response):
        with open('baidu.html', 'w') as f:
            f.write(response.body.decode())

    def parse3(self, response):
        with open('baidu2.html', 'w') as f:
            f.write(response.body.decode())