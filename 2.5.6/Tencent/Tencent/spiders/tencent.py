# -*- coding: utf-8 -*-
import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # 提取数据
        tr_list = response.xpath('//table[@class="tablelist"]//tr')[1:-1]
        for tr in tr_list:
            item = {}
            item['title'] = tr.xpath('.//a/text()').extract_first()
            yield item

        # 翻页
        next_href = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_href != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_href
            """构造并返回request"""
            yield scrapy.Request(next_url, callback=self.parse)