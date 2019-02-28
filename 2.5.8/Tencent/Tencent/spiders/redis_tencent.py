# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_redis.spiders import RedisCrawlSpider


class RedisTencentSpider(RedisCrawlSpider):
    name = 'redis_tencent'
    allowed_domains = ['hr.tencent.com']
    # start_urls = ['https://hr.tencent.com/position.php']
    redis_key = 'tencent'
    # scrapy crawl redis_tencent
    # lpush tencent 'https://hr.tencent.com/position.php'

    rules = (
        # 提取处理列表页
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), follow=True),
        # 提取处理详情页
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = {}
        item['title'] = response.xpath('//td[@id="sharetitle"]/text()').extract_first()
        item['content'] = response.xpath('//ul[@class="squareli"]/li/text()').extract()
        return item
