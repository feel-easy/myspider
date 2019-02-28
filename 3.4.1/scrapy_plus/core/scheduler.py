# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 上午10:19 GMT+8

import six
import hashlib
from w3lib.url import canonicalize_url

from scrapy_plus.conf.settings import SCHEDULER_PERSIST

from six.moves.queue import Queue
# 与from queue import Queue相同,只是为了兼容Py2Py3使用six模块
from scrapy_plus.utils.queue import Queue as RedisQueue
from scrapy_plus.utils.set import RedisFilterContainer, NoramlFilterContainer
from scrapy_plus.utils.log import logger


class Scheduler():

    def __init__(self, collector):
        if SCHEDULER_PERSIST:
            self.q = RedisQueue()
            self.fp_container = RedisFilterContainer()
        else:
            self.q = Queue()
            self.fp_container = NoramlFilterContainer()
        # self.fp_set = set()
        # self.total_repeat_nums = 0
        self.collector = collector # 统计计数器类对象, 从引擎传入!

    def add_request(self, request):
        # 把request放入请求队列
        # 判断指纹是否在集合中,如果不在就入队
        if self._filter_request(request):
            self.q.put(request)

    def get_request(self):
        # 取出一个request;取不出就返回none
        try:
            request = self.q.get_nowait()
        except:
            request = None
        return request

    def _filter_request(self, request):
        '''请求去重: 判断指纹是否在集合中,如果不在就指纹进集合,返回True'''
        fp = self._gen_fp(request)
        # if fp not in self.fp_set:
        if not self.fp_container.exists(fp):
            self.fp_container.add_fp(fp)
            return True
        # self.total_repeat_nums += 1 # 重复的请求数 +1
        self.collector.incr(self.collector.repeat_request_nums_key)
        logger.info("发现重复的请求：<{} {}>".format(request.method, request.url))
        return False

    def _gen_fp(self, request):
        # 返回request的fp指纹字符串

        url = canonicalize_url(request.url)
        method = request.method.upper()
        data = request.data if request.data else {}
        data = sorted(data.items(), key=lambda x:x[0])
        # 把data字典按(k,v)进行迭代,按照k作为排序的依据
        # 默认就是用k作为排序的依据
        # key=lambda x:x[0] x就是每次迭代的(k,v), x[0]就是排序的依据
        # 最终返回 [('a', 1), ('b', 2)]

        sha1 = hashlib.sha1()
        sha1.update(self._to_bytes(url))
        sha1.update(self._to_bytes(method))
        sha1.update(self._to_bytes(str(data)))
        fp = sha1.hexdigest()
        return fp

    def _to_bytes(self, string):
        """py2 py3 正好相反!"""
        if six.PY2: # 判断当前是否是python2
            if isinstance(string, str):
                return string
            else:
                return string.encode()
        elif six.PY3: # 判断当前是否是python3
            if isinstance(string, str):
                return string.encode()
            else:
                return string


