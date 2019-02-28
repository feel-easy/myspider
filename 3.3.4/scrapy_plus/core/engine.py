# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8
import time
from datetime import datetime

from scrapy_plus.core.spider import Spider
from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.downloader import Downloader
from scrapy_plus.core.pipeline import Pipeline
from scrapy_plus.http.request import Request

from scrapy_plus.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_plus.middlewares.downloader_middlewares import DownloaderMiddleware

from scrapy_plus.utils.log import logger # 使用单例日志对象


class Engine():

    def __init__(self, spider):
        self.spider = spider
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

        self.spider_mid = SpiderMiddleware()
        self.downloader_mid = DownloaderMiddleware()

        self.total_response_nums = 0
        self.total_request_nums = 0

    def start(self):
        # 被调用执行引擎逻辑的入口函数

        start = datetime.now()  # 起始时间
        logger.info("开始运行时间：%s" % start)  # 使用日志记录起始运行时间
        self._start_engine()
        stop = datetime.now()  # 结束时间
        logger.info("结束运行时间：%s" % stop)  # 使用日志记录结束运行时间
        logger.info("耗时：%.2f" % (stop - start).total_seconds())  # 使用日志记录运行耗时
        logger.info("总的请求数量:{}".format(self.total_request_nums))
        logger.info("总的响应数量:{}".format(self.total_response_nums))

    def _start_requests(self):
        """把爬虫中所有起始的url构造request并添加到请求队列中"""
        for start_request in self.spider.start_requests():
            # 1. 爬虫模块发出初始请求
            # 利用爬虫中间件预处理请求对象
            start_request = self.spider_mid.process_request(start_request)
            # 2. 把初始请求添加给调度器
            self.scheduler.add_request(start_request)
            # 总请求数 + 1
            self.total_request_nums += 1

    def _execute_request_response_item(self):
        """队列中取出一个request,直到处理完毕"""
        # 3. 从调度器获取请求对象
        request = self.scheduler.get_request()
        # 判断队列是否取空
        if request is None:
            return # 提前终止
        # 利用下载器中间件预处理请求对象
        request = self.downloader_mid.process_request(request)
        # 4. 利用下载器发起请求
        response = self.downloader.get_response(request)
        # 传递meta
        response.meta = request.meta
        # 利用下载器中间件预处理响应对象
        response = self.downloader_mid.process_response(response)
        # 利用爬虫中间件预处理响应对象
        response = self.spider_mid.process_response(response)
        # 5. 利用爬虫的解析响应的方法，处理响应，得到结果
        # request.parse指定的解析函数 = getattr(爬虫类对象, 指定的解析函数的字符串)
        parse_func = getattr(self.spider, request.parse)
        results = parse_func(response)
        for result in results:
            # 6. 判断结果对象
            if isinstance(result, Request):
                # 利用爬虫中间件预处理请求对象
                result = self.spider_mid.process_request(result)
                # 6.1 如果是请求对象，那么就再交给调度器
                self.scheduler.add_request(result)
                # 总请求数 + 1
                self.total_request_nums += 1
            else:
                # 6.2 否则，就交给管道处理
                self.pipeline.process_item(result)
        # 总响应数 +1
        self.total_response_nums += 1

    def _start_engine(self):
        # 框架运行的逻辑

        self._start_requests() # 把所有初始request放入队列

        while True:
            time.sleep(0.1)
            self._execute_request_response_item() # 处理一个从队列中取出的request

            # 程序退出的条件
            if self.scheduler.q.empty():
                break # 判断队列为空
            # if self.total_response_nums == self.total_request_nums:
            #     break

