# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8

from scrapy_plus.core.spider import Spider
from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.downloader import Downloader
from scrapy_plus.core.pipeline import Pipeline
from scrapy_plus.http.request import Request


class Engine():

    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

    def start(self):
        # 被调用执行引擎逻辑的入口函数
        self._start_engine()

    def _start_engine(self):
        # 框架运行的逻辑

        # 1. 爬虫模块发出初始请求
        start_request = self.spider.start_request()

        # 2. 把初始请求添加给调度器
        self.scheduler.add_request(start_request)

        # 3. 从调度器获取请求对象
        request = self.scheduler.get_request()

        # 4. 利用下载器发起请求
        response = self.downloader.get_response(request)

        # 5. 利用爬虫的解析响应的方法，处理响应，得到结果
        result = self.spider.parse(response)

        # 6. 判断结果对象
        if isinstance(result, Request):

            # 6.1 如果是请求对象，那么就再交给调度器
            self.scheduler.add_request(result)

        else:

            # 6.2 否则，就交给管道处理
            self.pipeline.process_item(result)
