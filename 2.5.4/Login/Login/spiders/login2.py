# -*- coding: utf-8 -*-
import scrapy


class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # 获取参数
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()

        # 构造post登录请求的字典
        data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': authenticity_token,
            'login': '1596930226@qq.com',
            'password': 'yao556696'
        }

        # 构造登录的post请求对象并返回
        yield scrapy.FormRequest(url='https://github.com/session',
                                 formdata=data,
                                 callback=self.check1)

    def check1(self, response):
        url = 'https://github.com/1596930226'
        yield scrapy.Request(url, callback=self.check2)

    def check2(self, response):
        with open('login2.html', 'w') as f:
            f.write(response.body.decode())

