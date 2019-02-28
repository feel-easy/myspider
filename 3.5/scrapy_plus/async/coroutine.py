# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-2 上午9:55 GMT+8


import gevent.monkey
gevent.monkey.patch_all()

from gevent.pool import Pool as BasePool

"""重新封装gevent.pool.Pool: 为了和线程池的Pool类的接口一致!"""
class Pool(BasePool):

    def apply_async(self, func, args=None, kwds=None, callback=None, error_callback=None):
        # 可以在这里去调用_error_callback函数,注意:要把该函数单独拿出来,不要放在引擎中
        return super().apply_async(func, args=args, kwds=kwds, callback=callback)

    def close(self):
        pass