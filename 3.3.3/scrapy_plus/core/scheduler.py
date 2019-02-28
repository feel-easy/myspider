# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午4:03 GMT+8

# 利用six模块实现py2和py3兼容
from six.moves.queue import Queue
# 与from queue import Queue相同


class Scheduler():

    def __init__(self):
        self.q = Queue()

    def add_request(self, request):
        # 请求入队的函数
        self.q.put(request)

    def get_request(self):
        # 取出request并返回
        try:
            request = self.q.get_nowait()
        except:
            request = None
        return request

    def _filter_request(self):
        '''请求去重'''
        # 暂时不实现
        pass