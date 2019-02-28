# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


class ProxyMid():
    def process_request(self, request, spider):
        proxy = 'http://58.53.128.83:3128'
        request.meta['proxy'] = proxy
