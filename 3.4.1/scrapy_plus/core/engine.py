# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 上午10:19 GMT+8

import importlib
import time
from datetime import datetime

from scrapy_plus.conf.settings import SPIDERS, \
    PIPELINES, SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES, \
    MAX_ASYNC_THREAD_NUMBER, ASYNC_TYPE, SCHEDULER_PERSIST

if ASYNC_TYPE == 'coroutine':
    from scrapy_plus.async.coroutine import Pool
elif ASYNC_TYPE == 'thread':
    from multiprocessing.dummy import Pool
else:
    raise Exception("不支持的异步类型：{}, 只能是'thread'或者'coroutine'".format(ASYNC_TYPE))
# 注意：
# 由于打patch补丁是为了替换掉socket为非阻塞的
# 而下载器中正好使用了requests模块，如果在这之后导入协程池，会导致requests中使用的socket没有被替换成功
# 从而有可能导致使用出现问题
# 所以在导入并发池对象之后再导入框架的各种类对象

from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.downloader import Downloader
from scrapy_plus.http.request import Request
from scrapy_plus.utils.log import logger # 导入已经实例化的日志对象,使用单例对象
from scrapy_plus.utils.stats_collector import NormalStatsCollector, ReidsStatsCollector


class Engine():
    def __init__(self):
        self.spiders = self._auto_import_instances(path=SPIDERS, isspider=True) # 爬虫字典
        self.pipelines = self._auto_import_instances(path=PIPELINES)
        self.spider_mids = self._auto_import_instances(path=SPIDER_MIDDLEWARES)
        self.downloader_mids = self._auto_import_instances(path=DOWNLOADER_MIDDLEWARES)

        if SCHEDULER_PERSIST:
            self.collector = ReidsStatsCollector()
        else:
            self.collector = NormalStatsCollector()
        # self.total_response_nums = 0
        # self.total_request_nums = 0

        self.scheduler = Scheduler(self.collector)
        self.downloader = Downloader()
        self.pool = Pool(5) # os.cpu_count() or 1
        self.is_running = True

    def _auto_import_instances(self, path=[], isspider=False):
        """传入项目配置中爬虫,管道,中间件配置变量(list),返回爬虫字段 或 包含管道类中间件对象的list"""

        results = {} if isspider else []

        for p in path: # p == 'spiders.baidu.BaiduSpider' or 'pipelines.BaiduPipeline'
            py_name_str = p.rsplit('.', 1)[0] # 'spiders.baidu' or 'pipelines'
            cls_name_str = p.rsplit('.', 1)[1] # 'BaiduSpider' or 'BaiduPipeline'
            # 动态导入py文件模块对象
            # importlib.import_module(模块/py文件名字的字符串) == 模块/py文件对象
            py_obj = importlib.import_module(py_name_str)
            # getattr(模块/py文件对象, 类名称字符串) == 类对象 # 还没有实例化
            cls_obj = getattr(py_obj, cls_name_str)

            if isspider:
                results[cls_obj.name] = cls_obj()
            else:
                results.append(cls_obj())
        return results


    def start(self):
        # 框架启动的入口函数
        start = datetime.now()  # 起始时间
        logger.info("开始运行时间：%s" % start)  # 使用日志记录起始运行时间
        self._start_engine()
        stop = datetime.now()  # 结束时间
        logger.info("结束运行时间：%s" % stop)  # 使用日志记录结束运行时间
        logger.info("耗时：%.2f" % (stop - start).total_seconds())  # 使用日志记录运行耗时
        logger.info("总的请求数量:{}".format(self.collector.request_nums))
        logger.info("总的响应数量:{}".format(self.collector.response_nums))
        logger.info("重复请求数量:{}".format(self.collector.repeat_request_nums))
        self.collector.clear() # 清除计数统计!

    def _start_requests(self):
        """专门处理爬虫起始url:构造request,加入队列"""
        for spider_name,spider in self.spiders.items():
            # 1. 爬虫模块发出初始请求
            for start_request in spider.start_requests():
                # 给request添加spider_name属性
                start_request.spider_name = spider_name
                # 利用爬虫中间件预处理请求对象
                for spider_mid in self.spider_mids:
                    start_request = spider_mid.process_request(start_request, spider)
                # 2. 把初始请求添加给调度器
                self.scheduler.add_request(start_request)
                # 总请求数 +1
                # self.total_request_nums += 1
                self.collector.incr(self.collector.request_nums_key)

    def _execute_request_response_item(self):
        """只处理一个请求对象:从队列取出一个request->response->item进管道/request入队"""
        # 3. 从调度器获取请求对象，交给下载器发起请求，获取一个响应对象
        request = self.scheduler.get_request()
        if request is None: # 此时队列取空了
            return # 提前终止函数
        # 根据爬虫的名字来获取爬虫类对象 # 爬虫名字在请求对象进入队列之前已经赋值了!
        spider = self.spiders[request.spider_name]

        # 利用下载器中间件预处理请求对象
        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request, spider)
        # 4. 利用下载器发起请求
        response = self.downloader.get_response(request)
        # meta属性的传递!!!
        response.meta = request.meta
        # 利用下载器中间件预处理响应对象
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(request, response, spider)
        # 利用爬虫中间件预处理响应对象
        for spider_mid in self.spider_mids:
            response = spider_mid.process_response(request, response, spider)

        # 5. 利用爬虫的解析响应的方法，处理响应，得到结果
        # 利用getattr函数和爬虫类中构造的request指定的解析函数名称字符串 获取指定解析函数对象
        # func = getattr(类, 类中函数的字符串) # func还没有执行被调用
        parse_func = getattr(spider, request.parse)
        # 调用request.parse指定的解析函数
        results = parse_func(response) # 解析函数有可能返回可迭代对象或None
        if results is None: # 如果解析函数返回None就提前return
            # 总响应数 +1
            # self.total_response_nums += 1
            self.collector.incr(self.collector.response_nums_key)
            return

        for result in results:
            # 6. 判断结果对象
            if isinstance(result, Request):
                # 给request添加spider_name属性
                result.spider_name = request.spider_name
                # 利用爬虫中间件预处理请求对象
                for spider_mid in self.spider_mids:
                    result = spider_mid.process_request(result, spider)
                # 6.1 如果是请求对象，那么就再交给调度器
                self.scheduler.add_request(result)
                # 总请求数 +1
                # self.total_request_nums += 1
                self.collector.incr(self.collector.request_nums_key)
            else:
                # 6.2 否则，就交给管道处理
                for pipeline in self.pipelines:
                    result = pipeline.process_item(result, spider)
        # 总响应数 +1
        # self.total_response_nums += 1
        self.collector.incr(self.collector.response_nums_key)

    def _error_callback(self, exception):
        try:
            raise exception    # 抛出异常后，才能被日志进行完整记录下来
        except Exception as e:
            logger.exception(e)

    def _callback(self, xxx):
        if self.is_running:
            # print(self.total_response_nums, self.total_request_nums, self.scheduler.total_repeat_nums)

            self.pool.apply_async(self._execute_request_response_item,
                                  callback=self._callback,
                                  error_callback=self._error_callback)

    def _start_engine(self):
        """引擎执行的逻辑"""
        self._start_requests() # 把所有起始url构造request入队

        for i in range(MAX_ASYNC_THREAD_NUMBER):
            # 不断 处理一个请求对象,直到该request处理完毕
            self.pool.apply_async(self._execute_request_response_item,
                                  callback=self._callback,
                                  error_callback=self._error_callback)
        while True: # 退出条件
            time.sleep(0.01)
            # 总响应数 + 重复的请求数 == 总请求数
            if self.collector.response_nums + self.collector.repeat_request_nums == self.collector.request_nums:
                self.is_running = False
                # print(self.total_response_nums, self.total_request_nums, self.scheduler.total_repeat_nums)
                break
