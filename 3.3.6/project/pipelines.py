# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-1 下午4:02 GMT+8

from spiders.douban import DoubanSpider


class BaiduPipeline(object):

    # 这里有所不同的是，需要增加一个参数，也就是传入爬虫对象
    # 以此来判断当前item是属于那个爬虫对象的
    def process_item(self, item, spider):
        '''处理item'''
        if spider.name == 'baidu':
            print("百度爬虫的数据：", item)
        return item    # 最后必须返回item


class DoubanPipeline(object):

    # 这里有所不同的是，需要增加一个参数，也就是传入爬虫对象
    # 以此来判断当前item是属于那个爬虫对象的
    def process_item(self, item, spider):
        '''处理item'''
        if isinstance(spider, DoubanSpider):
            print("豆瓣爬虫的数据：", item)
        return item    # 最后必须返回item