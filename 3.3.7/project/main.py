# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-30 下午5:04 GMT+8

from scrapy_plus.core.engine import Engine

from spiders.baidu import BaiduSpider
from spiders.douban import DoubanSpider
from pipelines import BaiduPipeline, DoubanPipeline
from middlewares.spider_middlewares import TestSpiderMiddleware1, TestSpiderMiddleware2
from middlewares.downloader_middlewares import TestDownloaderMiddleware1, TestDownloaderMiddleware2

if __name__ == '__main__':

    douban = DoubanSpider()
    baidu = BaiduSpider()
    spiders = {baidu.name:baidu, douban.name:douban}
    pipelines = [DoubanPipeline(), BaiduPipeline()]
    spider_mids = [TestSpiderMiddleware1(), TestSpiderMiddleware2()]
    downloader_mids = [TestDownloaderMiddleware1(), TestDownloaderMiddleware2()]

    engine = Engine(spiders=spiders,
                    pipelines=pipelines,
                    spider_mids=spider_mids,
                    downloader_mids=downloader_mids)
    engine.start()