# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8

import six
import hashlib
from w3lib.url import canonicalize_url
# 利用six模块实现py2和py3兼容
from six.moves.queue import Queue
# 与from queue import Queue相同

from scrapy_plus.utils.log import logger


class Scheduler():

    def __init__(self):
        self.q = Queue()
        self.fp_set = set()
        self.total_repeat_nums = 0

    def add_request(self, request):
        # 请求入队的函数: 指纹不在集合中self._filter_request(request)返回True
        if self._filter_request(request):
            self.q.put(request)

    def get_request(self):
        # 取出request并返回
        try:
            request = self.q.get_nowait()
        except:
            request = None
        return request

    def _filter_request(self, request):
        '''请求去重: request的指纹不在集合中,指纹入集合,返回true'''
        fp = self._gen_fp(request)
        if fp not in self.fp_set:
            self.fp_set.add(fp)
            return True
        self.total_repeat_nums += 1
        logger.info("发现重复的请求：<{} {}>".format(request.method, request.url))
        return False

    def _gen_fp(self, request):
        """返回request的fp"""

        url = canonicalize_url(request.url)
        method = request.method.upper()
        data = request.data if request.data else {}
        data = sorted(data.items(), key=lambda x:x[0])
        # data.items() 返回dict_items([('b', 2), ('a', 1)]) 迭代对象
        # sorted(dict.items()) # [('a', 1), ('b', 2)]
        # key参数接收一个lambda函数 表示按照返回的对象进行排序
        # x就是 dict.items()中每次迭代返回的 对象 (k, v)
        # x[0] 就是 dict中的k
        # data = sorted(data.items(), key=lambda x:x[0])表示对data.items()依照字典的k进行排序

        sha1 = hashlib.sha1()
        sha1.update(self._to_bytes(url))
        sha1.update(self._to_bytes(method))
        sha1.update(self._to_bytes(str(data)))
        fp = sha1.hexdigest()
        return fp

    def _to_bytes(self, string):
        """py2和py3字符串类型正好相反"""
        if six.PY2: # 判断当前是不是python2
            if isinstance(string, str):
                return string
            else:
                return string.encode()
        elif six.PY3:
            if isinstance(string, str):
                return string.encode()
            else:
                return string
