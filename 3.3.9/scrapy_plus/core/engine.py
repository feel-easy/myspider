# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8
import time
import importlib
from datetime import datetime

from scrapy_plus.core.spider import Spider
from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.downloader import Downloader
from scrapy_plus.core.pipeline import Pipeline
from scrapy_plus.http.request import Request
from scrapy_plus.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_plus.middlewares.downloader_middlewares import DownloaderMiddleware
from scrapy_plus.conf.settings import SPIDERS, PIPELINES, SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES

from scrapy_plus.utils.log import logger # 使用单例日志对象


class Engine():

    def __init__(self):
        self.spiders = self._auto_import_instances(path=SPIDERS, isspider=True)
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipelines = self._auto_import_instances(path=PIPELINES)
        self.spider_mids = self._auto_import_instances(path=SPIDER_MIDDLEWARES)
        self.downloader_mids = self._auto_import_instances(path=DOWNLOADER_MIDDLEWARES)

        self.total_response_nums = 0
        self.total_request_nums = 0

    def _auto_import_instances(self, path=[], isspider=False):
        """根据项目配置动态返回爬虫字典 或管道中间件列表"""
        instances = {} if isspider else []
        for p in path: # p = 'pipelines.BaiduPipeline'
            py_name_str = p.rsplit('.', 1)[0] # 'spipelines'
            cls_name_str = p.rsplit('.', 1)[1] # 'BaiduPipeline'
            py_obj = importlib.import_module(py_name_str) # 获取py文件对象
            cls_obj = getattr(py_obj, cls_name_str) # 获取py文件中的类对象,此时没有实例化!
            if isspider:
                instances[cls_obj.name] = cls_obj()
            else:
                instances.append(cls_obj())
        return instances

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
        logger.info("重复请求数量:{}".format(self.scheduler.total_repeat_nums))

    def _start_requests(self):
        """把爬虫中所有起始的url构造request并添加到请求队列中"""
        for spider_name, spider in self.spiders.items():
            for start_request in spider.start_requests():
                # 1. 爬虫模块发出初始请求
                # 利用爬虫中间件预处理请求对象
                for spider_mid in self.spider_mids:
                    start_request = spider_mid.process_request(start_request, spider)
                # 给request对象增加spider_name的属性
                start_request.spider_name = spider_name
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
        # 根据爬虫名获取爬虫类对象
        spider = self.spiders[request.spider_name]
        # 利用下载器中间件预处理请求对象
        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request, spider)
        # 4. 利用下载器发起请求
        response = self.downloader.get_response(request)
        # 传递meta
        response.meta = request.meta
        # 利用下载器中间件预处理响应对象
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(request, response, spider)
        # 利用爬虫中间件预处理响应对象
        for spider_mid in self.spider_mids:
            response = spider_mid.process_response(request, response, spider)
        # 5. 利用爬虫的解析响应的方法，处理响应，得到结果
        # request.parse指定的解析函数 = getattr(爬虫类对象, 指定的解析函数的字符串)
        parse_func = getattr(spider, request.parse)
        results = parse_func(response)
        if results is None: # 兼容解析函数中不写yield
            return
        for result in results:
            # 6. 判断结果对象
            if isinstance(result, Request):
                # 利用爬虫中间件预处理请求对象
                for spider_mid in self.spider_mids:
                    result = spider_mid.process_request(result, spider)
                # 给request对象增加spider_name的属性
                result.spider_name = request.spider_name
                # 6.1 如果是请求对象，那么就再交给调度器
                self.scheduler.add_request(result)
                # 总请求数 + 1
                self.total_request_nums += 1
            else:
                # 6.2 否则，就交给管道处理
                for pipeline in self.pipelines:
                    result = pipeline.process_item(result, spider)
        # 总响应数 +1
        self.total_response_nums += 1

    def _start_engine(self):
        # 框架运行的逻辑

        self._start_requests() # 把所有初始request放入队列

        while True:
            time.sleep(0.1)
            self._execute_request_response_item() # 处理一个从队列中取出的request

            # 程序退出的条件
            # if self.scheduler.q.empty():
            #     break # 判断队列为空
            if self.total_response_nums + self.scheduler.total_repeat_nums == self.total_request_nums:
                # print(self.total_request_nums, self.total_response_nums, self.scheduler.total_repeat_nums)
                # print(self.scheduler.q.empty())
                break

