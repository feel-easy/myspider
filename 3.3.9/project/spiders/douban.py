# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-1 下午3:49 GMT+8

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request


class DoubanSpider(Spider):
    name = 'douban'
    start_urls = []  # 重写start_requests方法后，这个属性就没有设置的必要了

    def start_requests(self):
        # 重写start_requests方法，返回多个请求
        base_url = 'http://movie.douban.com/top250?start='
        for i in range(0, 250, 25):    # 逐个返回第1-10页的请求属相
            url = base_url + str(i)
            yield Request(url)

    def parse(self, response):
        '''解析豆瓣电影top250列表页'''
        for li in response.xpath("//ol[@class='grid_view']/li"):    # 遍历每一个li标签
            item = {}
            item["title"] =  li.xpath(".//span[@class='title'][1]/text()")[0]    # 提取该li标下的 标题
            item["detail_url"] = li.xpath(".//div[@class='info']/div[@class='hd']/a/@href")[0]
            yield item
            # yield Request(detail_url, parse="parse_detail", meta={"item":item})    # 发起详情页的请求，并指定解析函数是parse_detail方法

    # def parse_detail(self, response):
    #     '''解析详情页'''
    #     item = response.meta["item"]
    #     item["url"] = response.url
    #     yield item

        # print('item：', item)    # 打印一下响应的url
        # return []    # 由于必须返回一个容器，这里返回一个空列表
        # yield Item(item)  #或者yield Item对象