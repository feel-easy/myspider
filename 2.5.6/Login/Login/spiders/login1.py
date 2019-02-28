# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['xxx']
    start_urls = ['https://github.com/1596930226'] # 这个起始的url需要登陆后/携带cookie才能获取

    def parse(self, response):
        with open('login1.html', 'w') as f:
            f.write(response.body.decode())

