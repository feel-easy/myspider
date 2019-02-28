# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
# 从哪执行就从哪导入
from Tencent.settings import USER_AGENTS_LIST


class UA():
    def process_request(self, request, spider):
        if spider.name == 'tencent':
            ua = random.choice(USER_AGENTS_LIST)
            request.headers['User-Agent'] = ua
            # 不能写return

class CheckUa():
    def process_response(self, response, request, spider):
        # print(response.request.headers['User-Agent']) # 这是坑
        print(request.headers['User-Agent'])
        return response